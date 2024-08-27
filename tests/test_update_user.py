# from cores.my_request import Request
# from cores.asserts import Assert


# class TestUpdateUser:
#
#     def test_update_user_with_valid_user_id(self):
#         data = {
#             "name": "Ajay",
#             "job": "SDE"
#         }
#
#         user_id = 2
#         response = Request.put(f"/api/users/{user_id}", data)
#         Assert.assert_code_status(response, 200)
#         json_response = response.json()
#         Assert.assert_equals(json_response['name'], data['name'])
#         Assert.assert_equals(json_response['job'], data['job'])
