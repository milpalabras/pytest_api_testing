from dataclasses import dataclass
import requests

from src.helpers.logging_helper import logHelper
from config import BASE_URI


@dataclass
class Response:
    status_code: int
    text: str
    as_dict: object
    headers: dict
    body: dict
    cookies: dict


class ApiRequest:
    def __init__(self):
        self.logger = logHelper().get_logger(__name__)
        self.session = requests.Session()
        # set proxy session
        self.session.proxies = {"http": "http://proxy:port"}
        

    def get(self, url, params):
        try:
            self.logger.info(
                f"Realizando request GET a {url} con los parametros {params}"
            )
            response = self.session.get(url, params=params)

            self.logger.info(f"Response Obtenido: {response.text}")
        except Exception as e:
            self.logger.error(f"Error al realizar el request {e}")
            raise e
        return self.__get_response(response)

    def post(self, url, params, payload):
        try:
            self.logger.info(
                f"Realizando request POST a {url} con los parametros {params} y payload {payload}"
            )
            response = self.session.post(url, params=params, data=payload)
            self.logger.info(f"Response Obtenido: {response.text}")
        except Exception as e:
            self.logger.error(f"Error al realizar el request {e}")
            raise e
        return self.__get_response(response)

    def delete(self, url, payload):
        response = self.session.delete(url, data=payload)
        return self.__get_response(response)

    def put(self, url, payload):
        response = self.session.put(url, data=payload)
        return self.__get_response(response)

    def __get_response(self, response):
        status_code = response.status_code
        text = response.text

        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        headers = response.headers
        body = response.request.body
        cookies = response.cookies.get_dict()
        return Response(status_code, text, as_dict, headers, body, cookies)
