import jsonpickle
import requests
from requests import Response


class HttpClient:

    @staticmethod
    def post(url, data=None) -> Response:
        headers = {
            'Content-Type': 'application/json'
        }
        data_json = None
        if data is not None:
            data_json = jsonpickle.encode(data, unpicklable=False)

        return requests.post(url, data=data_json, headers=headers)
