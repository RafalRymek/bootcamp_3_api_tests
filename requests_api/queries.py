user_query = """query {
    user(login: "RafalRymek") {
    bio
    bioHTML
    createdAt
    company
    avatarUrl
    }
    }
    """

repo_owner_query = """query {
    repositoryOwner(login: "RafalRymek") 
    {
      repository(name: "bootcamp_3_api_tests") {
        url
        } 
    } 
    } 
    """

rate_limit_query = """
{
  viewer {
    login
    createdAt
  }
  rateLimit {
    limit
    cost
    remaining
    resetAt
  }
}
"""
