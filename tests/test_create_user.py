from cores.my_request import Request
from cores.asserts import Assert
class TestCreateUser:

    def test_create_user_with_valid_data(self):
        data = {
            "name":"Ajay",
            "job":"SDE"
        }

        response = Request.post("/api/users",data)
        Assert.assert_code_status(response,201)
        json_response = response.json()
        Assert.assert_equals(json_response['name'],data['name'])
        Assert.assert_equals(json_response['job'],data['job'])