from endpoints.GetUrlInfo import GetUrlInfo


def test_existing_url(create_short_url):
    short_code = create_short_url.short_url
    long_url = create_short_url.url_to_shorten
    url_info = GetUrlInfo(short_code)
    assert url_info.response_is_200()
    assert url_info.long_url_is_correct(long_url)


def test_missing_url(create_short_url):
    short_code = f'upd_{create_short_url.short_url}qw'
    url_info = GetUrlInfo(short_code)
    assert url_info.response_is_404()
    assert url_info.error_message_is_correct()
