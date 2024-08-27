import allure

from cores.my_request import Request
from cores.asserts import Assert
from cores.base_test import BaseCase


class TestPytestDemo(BaseCase):
    @allure.story("Test example get endpoint")
    @allure.title("Verify the get API")
    @allure.description("verify the get API response status code and data")
    @allure.severity("blocker")
    def test_get_demo(self):
        config = BaseCase.get_config()
        host = config.get("host")
        get_api = config.get("getAPI")
        response = Request.get(f"{host}/{get_api}")
        Assert.assert_code_status(response, 200)
        actual_response = response.json()
        expected_response = BaseCase.get_response_data().get("getAPI")
        Assert.assert_equals(actual_response['userId'], expected_response['userId'])
        Assert.assert_equals(actual_response['id'], expected_response['id'])
        Assert.assert_equals(actual_response['title'], expected_response['title'])
        Assert.assert_equals(actual_response['body'], expected_response['body'])

    def test_post_demo(self):
        config = BaseCase.get_config()
        host = config.get("host")
        post_api = config.get("postAPI")
        request_data = BaseCase.get_request_data().get("postAPI")
        url = host + post_api
        response = Request.post(url, request_data)
        json_response = response.json()
        expected_response_data = BaseCase.get_response_data().get("postAPI")
        Assert.assert_code_status(response, 201)
        Assert.assert_equals(json_response['title'], expected_response_data['title'])
        Assert.assert_equals(json_response['body'], expected_response_data['body'])
        Assert.assert_equals(json_response['userId'], str(expected_response_data['userId']))
