from config import BASE_URI as BASE_URI
from src.helpers.request import ApiRequest


class BaseClient:
    def __init__(self):
        self.base_url = BASE_URI
        self.api_request = ApiRequest()
        self._token = None
