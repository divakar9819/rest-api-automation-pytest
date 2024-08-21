import logging
import os.path
import datetime
from requests import Response

import allure


class Logger:
    instance = None
    logger = None
    path = "logger.log"
    data = ""

    def __init__(self):
        # if os.path.exists(self.path):
        #     os.remove(self.path)

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        handler = logging.FileHandler(self.path)
        handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter()
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()

        return cls.instance

    @allure.step("{method} request to {url}")
    def add_request(self, url: str, data: dict, headers: dict, cookies: dict, method: str):
        data_to_add = f"\n----Request----\n"
        data_to_add += f"[{str(datetime.datetime.now())}] Request method: {method}\n"
        data_to_add += f"[{str(datetime.datetime.now())}] Request URL: {url}\n"
        data_to_add += f"[{str(datetime.datetime.now())}] Request data: {data}\n"
        data_to_add += f"[{str(datetime.datetime.now())}] Request headers: {headers}\n"
        data_to_add += f"[{str(datetime.datetime.now())}] Request cookies: {cookies}"
        data_to_add += "\n"

        self.data += data_to_add
        self.logger.info(data_to_add)

    def add_response(self, response: Response):
        cookies_as_dict = dict(response.cookies)
        headers_as_dict = dict(response.headers)

        data_to_add = f"\n----Response----\n"
        data_to_add += f"[{str(datetime.datetime.now())}] Response code: {response.status_code}\n"
        data_to_add += f"[{str(datetime.datetime.now())}] Response text: {response.text}\n"
        data_to_add += f"[{str(datetime.datetime.now())}] Response headers: {headers_as_dict}\n"
        data_to_add += f"[{str(datetime.datetime.now())}] Response cookies: {cookies_as_dict}"
        data_to_add += "\n-----\n"

        self.data += data_to_add
        self.logger.info(data_to_add)

    def clear_data(self):
        self.data = ""

    def show_all_data(self):
        if len(self.data) > 0:
            print("\n\nSTART OF LOG")
            print(self.data)
            print("END OF LOG\n\n")

    def write_log_to_file(self):
        with open(self.path, 'a', encoding='utf-8') as logger_file:
            test_name = os.environ.get('PYTEST_CURRENT_TEST')
            logger_file.write(f"START TEST {test_name}\n")
            logger_file.write(self.data)
            logger_file.write(f"\nEND TEST {test_name}\n\n")
            self.clear_data()
