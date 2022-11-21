from endpoints.new_url import PostNewUrl
import constants


def test_random_shortener(random_url):
    new_url = PostNewUrl()
    new_url.url_to_shorten = random_url
    new_url.shorten()
    assert new_url.response_is_200()
    assert new_url.url_to_shorten_is_correct_in_response()
    assert new_url.short_code_is_not_empty()


def test_custom_shortener_not_strict(random_url, random_custom_short_code):
    new_url = PostNewUrl(random_url, random_custom_short_code)
    new_url.shorten()
    assert new_url.response_is_200()
    assert new_url.url_to_shorten_is_correct_in_response()
    assert new_url.short_code_is_correct(random_custom_short_code)


def test_custom_shortener_not_strict_with_occupied_code(random_url):
    new_url = PostNewUrl(random_url, constants.OCCUPIED_SHORT_CODE)
    new_url.shorten()
    assert new_url.response_is_200()
    assert new_url.url_to_shorten_is_correct_in_response()
    assert new_url.short_code_is_not_empty()
    assert new_url.short_code_is_correct(constants.OCCUPIED_SHORT_CODE) is False


def test_custom_shortener_strict(random_url, random_custom_short_code):
    new_url = PostNewUrl(random_url, random_custom_short_code, False)
    new_url.shorten()
    assert new_url.response_is_200()
    assert new_url.url_to_shorten_is_correct_in_response()
    assert new_url.short_code_is_correct(random_custom_short_code)


def test_custom_shortener_strict_with_occupied_code(random_url):
    new_url = PostNewUrl(random_url, constants.OCCUPIED_SHORT_CODE, False)
    new_url.shorten()
    assert new_url.response_is_200()
    assert new_url.error_message_returned()
    assert new_url.error_message_is_correct()
