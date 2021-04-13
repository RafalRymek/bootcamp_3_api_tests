import pytest
from hamcrest import *
import requests
import datetime
import time


def test_get_list_users():
    # setup
    get_list_users_url = "https://reqres.in/api/users?page=2"
    # actions
    response = requests.get(url=get_list_users_url)
    data = response.json()["data"][0]
    # results
    assert_that(response.status_code, is_(equal_to(200)), reason="Wrong status code")
    assert_that(data["email"], is_(equal_to("michael.lawson@reqres.in")), reason="Wrong email")
    assert_that(data["first_name"], has_string("Michael"), reason="Wrong name")
    assert_that(data["last_name"], has_string("Lawson"), reason="Wrong surname")
    assert_that(data[5]["id"], is_(equal_to(12)))


def test_get_single_user():
    # setup
    get_single_user_url = "https://reqres.in/api/users/2"
    # actions
    response = requests.get(url=get_single_user_url)
    # results
    assert_that(response.status_code, is_(equal_to(200)), reason="Wrong status code")
    assert_that(response.json()["data"]["email"], is_(equal_to("janet.weaver@reqres.in")), reason="Wrong email")
    assert_that(response.json()["data"]["first_name"], has_string("Janet"), reason="Wrong name")
    assert_that(response.json()["data"]["last_name"], has_string("Weaver"), reason="Wrong surname")


def test_get_user_not_found():
    # setup
    get_user_not_found_url = "https://reqres.in/api/users/23"
    # actions
    response = requests.get(url=get_user_not_found_url)
    # results
    assert_that(response.status_code, is_(equal_to(404)), reason="Wrong status code")
    assert_that(response.json(), is_(equal_to({})), reason="Wrong response")


def test_post_create_user():
    # setup
    post_url = "https://reqres.in/api/users?page=2"
    post_body = {"name": "user", "job": "tester"}
    # actions
    response = requests.post(url=post_url, json=post_body)
    # results
    assert_that(response.status_code, is_(equal_to(201)), reason="Wrong status code")
    assert_that(response.json()["name"], is_(equal_to("user")), reason="Wrong name")
    assert_that(response.json()["job"], is_(equal_to("tester")), reason="Wrong job")
    assert_that(int(response.json()["id"]), greater_than(0), reason="Wrong id number")
    assert_that(response.json()["createdAt"], is_not(None), reason="User not created")
    assert_that(str(response.json()["createdAt"])[0:4], is_(equal_to(str(datetime.date.today().year))), reason="Wrong "
                                                                                                               "year")


def test_put_update_user():
    # setup
    put_url = "https://reqres.in/api/users/2"
    put_body = {"name": "user_two", "job": "tester_two"}
    # actions
    response = requests.put(url=put_url, json=put_body)
    # results
    assert_that(response.status_code, is_(equal_to(200)), reason="Wrong status code")
    assert_that(response.json()["name"], is_(equal_to("user_two")), reason="Wrong name")
    assert_that(response.json()["job"], is_(equal_to("tester_two")), reason="Wrong job")
    assert_that(response.json()["updatedAt"], is_not(None), reason="User not created")
    assert_that(str(response.json()["updatedAt"])[0:4], is_(equal_to(str(datetime.date.today().year))), reason="Wrong "
                                                                                                               "year")


def test_delete_user():
    # setup
    delete_url = "https://reqres.in/api/users/2"
    # actions
    response = requests.delete(delete_url)
    # results
    assert_that(response.status_code, is_(equal_to(204)), reason="Wrong status code")
    assert_that(response.text, is_(equal_to("")), reason="Wrong response")


def test_post_register_successful():
    # setup
    post_register_successful_url = "https://reqres.in/api/register"
    post_body = {"email": "eve.holt@reqres.in", "password": "pistol"}
    # actions
    response = requests.post(url=post_register_successful_url, json=post_body)
    # results
    assert_that(response.status_code, is_(equal_to(200)), reason="Wrong status code")
    assert_that(int(response.json()["id"]), greater_than(0), reason="Wrong id number")
    assert_that(len(response.json()["token"]), greater_than_or_equal_to(17), reason="Wrong token length")


def test_post_register_unsuccessful():
    # setup
    post_register_unsuccessful_url = "https://reqres.in/api/register"
    post_body = {"email": "eve.holt@test.com"}
    # actions
    response = requests.post(url=post_register_unsuccessful_url, json=post_body)
    # results
    assert_that(response.status_code, is_(equal_to(400)), reason="Wrong status code")
    assert_that(response.json(), is_(equal_to({"error": "Missing password"})), reason="Wrong response")


def test_get_delay_response():
    # setup
    get_delay_url = "https://reqres.in/api/users?delay=3"
    # actions
    start_time = time.time()
    response = requests.get(url=get_delay_url)
    data = response.json()["data"][0]
    # results
    end_time = time.time()
    delay_time = float("%.2g" % (end_time - start_time))
    assert_that(delay_time, greater_than(3.0), reason="Wrong delay time")
    assert_that(data["email"], is_(equal_to("george.bluth@reqres.in")), reason="Wrong email")
    assert_that(data[5]["email"], is_(equal_to("tracey.ramos@reqres.in")), reason="Wrong email")
