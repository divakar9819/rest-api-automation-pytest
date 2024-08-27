import json

from requests import Response
from cores.logger import Logger


# with open("config/config.json", "r") as json_file:
#     if json_file.name is None:
#         raise Exception("File not found")
#     config = json.load(json_file)
#
# with open("data/request_data.json", "r") as json_file:
#     if json_file.name is None:
#         raise Exception("file not found")
#
#     request_data = json.load(json_file)
#
# with open("data/response_data.json", "r") as json_file:
#     if json_file.name is None:
#         raise Exception("file not found")
#
#     response_data = json.load(json_file)

class BaseCase:

    @staticmethod
    def tear_down():
        Logger.get_instance().write_log_to_file()

    @staticmethod
    def get_header(response: Response, headers_name):
        if headers_name in response.headers:
            return {headers_name: response.headers[headers_name]}
        else:
            raise Exception(f"Can't find header name with name {headers_name} in last response")

    @staticmethod
    def get_config():
        with open("config/config.json", "r") as json_file:
            if json_file.name is None:
                raise Exception("File not found")
            return json.load(json_file)

    @staticmethod
    def get_request_data():
        with open("data/request_data.json", "r") as json_file:
            if json_file.name is None:
                raise Exception("file not found")

            return json.load(json_file)

    @staticmethod
    def get_response_data():
        with open("data/response_data.json", "r") as json_file:
            if json_file.name is None:
                raise Exception("file not found")

            return json.load(json_file)
