# Bootcamp API automated tests

Automated API tests to cover endpoints from https://reqres.in/{resource}

### Following tech stack is using:

python  
unittest  
pytest

## Setup:  
1. open terminal
2. run `git clone https://github.com/RafalRymek/bootcamp_3_api_tests.git` to clone repository 
3. run `cd bootcamp_3_api_tests` to move to local repository folder
4. run `pipenv install` to set up all necessary dependencies from Pipfile.lock
5. run `pipenv shell` to be able to use all pipenv dependencies from terminal

## Execution:

to run API tests:  
`python3 tests/api_tests.py`

to run API tests with pytest  
`pytest tests/test_api_tests_pytest.py`
