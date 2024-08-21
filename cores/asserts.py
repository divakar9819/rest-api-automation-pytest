from requests import Response


class Assert:

    @staticmethod
    def assert_code_status(response: Response, expected_code: int, error_message: str = ""):
        assert response.status_code == expected_code, f"expected error code {expected_code} but received {response.status_code} {error_message}"

    @staticmethod
    def assert_equals(val1, val2, error_message: str=""):
        assert val1 == val2, f"Failed assertion that {val1} is equals {val2}. {error_message}"
