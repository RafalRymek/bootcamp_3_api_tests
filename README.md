#Bootcamp API automated tests
Automated API tests to cover endpoints from https://reqres.in/{resource}

Following tech stack is using:
python  
unittest  
pytest 

#Setup:
open terminal
run `git clone https://github.com/RafalRymek/bootcamp_3_api_tests.git` to clone repository   
run `cd bootcamp_3_api_tests` to move to local repository folder  
run `pipenv install` to set up all necessary dependencies from Pipfile.lock  
run `pipenv shell` to be able to use all pipenv dependencies from terminal

#Execution:
to run API tests:  
`python3 tests/api_tests.py`

to run API tests with pytest:  
`pytest tests/test_api_tests_pytest.py`

to run graphql tests with pytest:
1. previously should create your own access token to authorization to GitHub 
   `https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)`
2. in utils.py add necessary parameters:  
   ACCESS_TOKEN = `GITHUB_ACCESS_TOKEN`  
   USERNAME = `GITHUB_USER_LOGIN`  
   API_URL = `https://api.github.com/graphql`
3. in queries.py add GitHub username in query (TBD later, right now "RafalRymek")
4. run `cd bootcamp_3_api_tests` to move to local repository folder  
5. run `export PYTHONPATH=`pwd`     
6. run `pytest graphql_tests/test_graphql_github.py`

