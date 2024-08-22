import json

from requests import Response
from cores.logger import Logger

with open("config/config.json", "r") as json_file:
    if json_file.name is None:
        raise Exception("File not found")
    config = json.load(json_file)


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

    def print_config(self):
        print(config.get("prod_host"))



