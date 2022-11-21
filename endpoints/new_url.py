from endpoints.endpoints_handler import Endpoint

import constants
from utils.send_request import send


class PostNewUrl(Endpoint):
    def __init__(self, url_to_shorten: str = None, custom_short_url: str = None, generate_other_if_occupied: bool = True):
        self.__long = url_to_shorten
        self.__custom = custom_short_url
        self.__useFallback = generate_other_if_occupied

    @property
    def url_to_shorten(self) -> str:
        return self.__long

    @url_to_shorten.setter
    def url_to_shorten(self, value: str):
        self.__long = value

    @property
    def custom_short_url(self) -> str:
        return self.__custom

    @custom_short_url.setter
    def custom_short_url(self, value: str):
        self.__custom = value

    @property
    def strict_custom(self) -> bool:
        return self.__useFallback

    @strict_custom.setter
    def strict_custom(self, value: bool):
        self.__useFallback = value

    def shorten(self) -> dict:
        body = {
            'input': self.__long
        }
        if self.__custom:
            body['custom'] = self.__custom
            body['long'] = body['input']
            del body['input']
        if not self.__useFallback:
            body['useFallback'] = False
        response = send('POST', f'{constants.BASE_URL}{constants.API_URL}', body)
        self.status_code = response.status_code
        if 'error' not in response.json():
            self.response_body = response.json()[0]
            self.short_url = self.response_body['code']
        else:
            self.response_body = response.json()
        return self.response_body  # Можно не возвращать, но на всякий случай пусть будет

    def url_to_shorten_is_correct_in_response(self) -> bool:
        return self.__long == self.response_body['long']

    def short_code_is_not_empty(self) -> bool:
        return len(self.short_url) > 0

    def short_code_is_correct(self, short_code: str) -> bool:
        return self.short_url == short_code

    def error_message_returned(self) -> bool:
        return 'error' in self.response_body

    def error_message_is_correct(self) -> bool:
        return self.response_body['error']['message'] == f'Code already taken: {constants.OCCUPIED_SHORT_CODE}'
