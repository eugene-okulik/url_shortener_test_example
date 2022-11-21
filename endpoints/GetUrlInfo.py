from utils.send_request import send
from endpoints.endpoints_handler import Endpoint
import constants


class GetUrlInfo(Endpoint):
    def __init__(self, short_code: str):
        self.short_url = short_code
        self.get_info()

    def get_info(self):
        response = send('GET', f'{constants.BASE_URL}{constants.API_URL}/{self.short_url}')
        self.status_code = response.status_code
        if self.status_code == 404:
            self.response_body = response.json()
        else:
            self.response_body = response.text

    def long_url_is_correct(self, long_url: str) -> bool:
        return self.response_body == long_url

    def error_message_is_correct(self) -> bool:
        return self.response_body['error']['message'] == 'GoTiny link not found'
