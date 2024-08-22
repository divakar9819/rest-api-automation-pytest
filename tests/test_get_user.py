
from cores.my_request import Request
from cores.asserts import Assert
from cores.base_test import BaseCase, config


class TestGetUser(BaseCase):

    def test_get_user_list_with_page_id(self):
        data = {
            "page": "2"
        }

        response = Request.get("/api/users", data)
        Assert.assert_code_status(response,200)
        json_response = response.json()
        Assert.assert_equals(data['page'],str(json_response['page']))
        data = json_response['data']
        expected_id = 7
        for actual_data in data:
            Assert.assert_equals(actual_data['id'],expected_id)
            expected_id += 1

    def test_get_single_user_user_id(self,user_id=2):

        response = Request.get(f"/api/users/{user_id}")
        Assert.assert_code_status(response,200)
        json_response = response.json()
        data = json_response['data']
        Assert.assert_equals(data['id'],user_id)

    def test_get_single_user_not_fount(self):
        user_id = 23
        response = Request.get(f"/api/users/{user_id}")
        Assert.assert_code_status(response,404)

