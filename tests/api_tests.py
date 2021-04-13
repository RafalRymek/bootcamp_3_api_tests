import unittest
import requests
import datetime
import time


class TestApiReqRes(unittest.TestCase):

    def test_get_list_users(self):
        # setup
        get_list_users_url = "https://reqres.in/api/users?page=2"
        # actions
        response = requests.get(url=get_list_users_url)
        # results
        print("Status code:", response.status_code)
        print("Body:", response.json())
        assert response.status_code == 200
        assert response.json()["data"][0]["email"] == "michael.lawson@reqres.in"
        assert response.json()["data"][1]["email"] == "lindsay.ferguson@reqres.in"
        assert response.json()["data"][0]["first_name"] == "Michael"
        assert response.json()["data"][0]["last_name"] == "Lawson"
        assert response.json()["data"][5]["id"] == 12

    def test_get_single_user(self):
        # setup
        get_single_user_url = "https://reqres.in/api/users/2"
        # actions
        response = requests.get(url=get_single_user_url)
        # results
        print("Status code:", response.status_code)
        print("Body:", response.json())
        assert response.status_code == 200
        assert response.json()["data"]["email"] == "janet.weaver@reqres.in"
        assert response.json()["data"]["first_name"] == "Janet"
        assert response.json()["data"]["last_name"] == "Weaver"

    def test_get_user_not_found(self):
        # setup
        get_user_not_found_url = "https://reqres.in/api/users/23"
        # actions
        response = requests.get(url=get_user_not_found_url)
        # results
        print("Status code:", response.status_code)
        print("Body:", response.json())
        assert response.status_code == 404
        assert response.json() == {}

    def test_post_create_user(self):
        # setup
        post_url = "https://reqres.in/api/users?page=2"
        post_body = {"name": "user", "job": "tester"}
        # actions
        response = requests.post(url=post_url, json=post_body)
        # results
        print("Status code:", response.status_code)
        assert response.status_code == 201
        assert response.json()["name"] == "user"
        assert response.json()["job"] == "tester"
        assert int(response.json()["id"]) > 0
        assert response.json()["createdAt"] is not None
        assert str(response.json()["createdAt"])[0:4] == str(datetime.date.today().year)

    def test_put_update_user(self):
        # setup
        put_url = "https://reqres.in/api/users/2"
        put_body = {"name": "user_two", "job": "tester_two"}
        # actions
        response = requests.put(url=put_url, json=put_body)
        # results
        print("Status code:", response.status_code)
        assert response.status_code == 200
        assert response.json()["name"] == "user_two"
        assert response.json()["job"] == "tester_two"
        assert response.json()["updatedAt"] is not None
        assert str(response.json()["updatedAt"])[0:4] == str(datetime.date.today().year)

    def test_delete_user(self):
        # setup
        delete_url = "https://reqres.in/api/users/2"
        # actions
        response = requests.delete(delete_url)
        # results
        print("Status code:", response.status_code)
        assert response.status_code == 204
        assert response.text == ""

    def test_post_register_successful(self):
        # setup
        post_register_successful_url = "https://reqres.in/api/register"
        post_body = {"email": "eve.holt@reqres.in", "password": "pistol"}
        # actions
        response = requests.post(url=post_register_successful_url, json=post_body)
        # results
        print("Status code:", response.status_code)
        print(response.status_code)
        assert response.status_code == 200
        assert int(response.json()["id"]) > 0
        assert len(response.json()["token"]) == 17

    def test_post_register_unsuccessful(self):
        # setup
        post_register_unsuccessful_url = "https://reqres.in/api/register"
        post_body = {"email": "eve.holt@test.com"}
        # actions
        response = requests.post(url=post_register_unsuccessful_url, json=post_body)
        # results
        print(response.status_code)
        assert response.status_code == 400
        assert response.json() == {"error": "Missing password"}

    def test_get_delay_response(self):
        # setup
        get_delay_url = "https://reqres.in/api/users?delay=3"
        # actions
        start_time = time.time()
        response = requests.get(url=get_delay_url)
        # results
        print(response.json())
        end_time = time.time()
        delay_time = float("%.2g" % (end_time - start_time))
        assert delay_time >= 3.0
        assert response.json()["data"][0]["email"] == "george.bluth@reqres.in"
        assert response.json()["data"][5]["email"] == "tracey.ramos@reqres.in"


if __name__ == '__main__':
    unittest.main()
