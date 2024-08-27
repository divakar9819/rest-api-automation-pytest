from cores.my_request import Request
from cores.asserts import Assert
from cores.base_test import BaseCase


class TestCreateUser(BaseCase):

    def test_create_user_with_valid_data(self):
        config = BaseCase.get_config()
        host = config.get("reqresHost")
        post_user = config.get("postUser")
        url = host + post_user
        request_data = BaseCase.get_request_data().get("createUser")
        response = Request.post(url, request_data)
        Assert.assert_code_status(response, 201)
        actual_response = response.json()
        expected_response = BaseCase.get_response_data().get("createUserPostAPI")
        Assert.assert_equals(actual_response['name'], expected_response['name'])
        Assert.assert_equals(actual_response['job'], expected_response['job'])

    def test_create_user_with_invalid_data(self):
        data = {}
        config = BaseCase.get_config()
        host = config.get("reqresHost")
        post_user = config.get("postUser")
        url = host + post_user
        response = Request.post(url, data)
        print(response.status_code)
        json_response = response.json()
        print(json_response)
