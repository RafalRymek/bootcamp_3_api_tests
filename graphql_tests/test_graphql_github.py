import pytest
import requests
from hamcrest import *
from utils.utils import ACCESS_TOKEN, API_URL
from requests_api.queries import user_query, repo_owner_query, rate_limit_query

github_graphql_url = API_URL
headers = {"Authorization": "bearer " + ACCESS_TOKEN}


def test_run_bio_query():
    # request
    request = requests.post(url=github_graphql_url, json={'query': user_query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(f"Query failed to run by returning code of {request.status_code}. {user_query}")


# response
result = test_run_bio_query()
github_user_bio = result["data"]["user"]["bio"]
print(f"User bio information: {github_user_bio}")
assert_that(github_user_bio, has_string("QA Engineer "), reason="Wrong bio")


def test_run_repo_query():
    # request
    request = requests.post(url=github_graphql_url, json={'query': repo_owner_query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(f"Query failed to run by returning code of {request.status_code}. {repo_owner_query}")


# response
result = test_run_repo_query()
github_repo_url = result["data"]["repositoryOwner"]["repository"]["url"]
print(f"User repository url: {github_repo_url}")
assert_that(github_repo_url, starts_with("https:"), reason="Wrong url")


def test_run_limit_query():
    # request
    request = requests.post(url=github_graphql_url, json={'query': rate_limit_query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(f"Query failed to run by returning code of {request.status_code}. {rate_limit_query}")


# response
result = test_run_limit_query()
github_repo_limit = result["data"]["rateLimit"]["limit"]
github_repo_remaining = result["data"]["rateLimit"]["remaining"]
print(f"User rate limit: {github_repo_limit}")
print(f"User rate remaining: {github_repo_remaining}")
assert_that(github_repo_limit, is_(equal_to(5000)), reason="Wrong limit")
assert_that(github_repo_remaining, is_(greater_than(0)), reason="Limit reached")
