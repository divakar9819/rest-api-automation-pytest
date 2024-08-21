import os


class Environment:
    DEV = "dev"
    PROD = "prod"

    URLS = {
        DEV: 'https://dev.reqres.in',
        PROD: 'https://reqres.in'
    }

    def __init__(self):
        self.name = self._get_environment_variable()

    def _get_environment_variable(cls) -> str:
        try:
            return os.environ['ENVIRONMENT']
        except KeyError:
            return cls.PROD

    def base_url(self) -> str:
        return self.URLS[self.name]


env = Environment()
print(env.name)
print(env.base_url())
