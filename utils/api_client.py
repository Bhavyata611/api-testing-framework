import requests
from utils.config import BASE_URL, TIMEOUT
from utils.logger import logger


class APIClient:
    def __init__(self):
        self.base_url = BASE_URL

    def get(self, endpoint):
        logger.info(f"GET Request: {self.base_url}{endpoint}")
        response = requests.get(
            f"{self.base_url}{endpoint}",
            timeout=TIMEOUT
        )
        logger.info(f"Response Status Code: {response.status_code}")
        return response

    def post(self, endpoint, data):
        logger.info(f"POST Request: {self.base_url}{endpoint}")
        response = requests.post(
            f"{self.base_url}{endpoint}",
            json=data,
            timeout=TIMEOUT
        )
        logger.info(f"Response Status Code: {response.status_code}")
        return response

    def put(self, endpoint, data):
        logger.info(f"PUT Request: {self.base_url}{endpoint}")
        response = requests.put(
            f"{self.base_url}{endpoint}",
            json=data,
            timeout=TIMEOUT
        )
        logger.info(f"Response Status Code: {response.status_code}")
        return response

    def patch(self, endpoint, data):
        logger.info(f"PATCH Request: {self.base_url}{endpoint}")
        response = requests.patch(
            f"{self.base_url}{endpoint}",
            json=data,
            timeout=TIMEOUT
        )
        logger.info(f"Response Status Code: {response.status_code}")
        return response

    def delete(self, endpoint):
        logger.info(f"DELETE Request: {self.base_url}{endpoint}")
        response = requests.delete(
            f"{self.base_url}{endpoint}",
            timeout=TIMEOUT
        )
        logger.info(f"Response Status Code: {response.status_code}")
        return response