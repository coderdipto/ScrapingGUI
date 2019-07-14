import requests
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from scrapy.http import TextResponse
from scrapyd_api import ScrapydAPI

from utils.constant import SCRAPYD_HOST


def is_valid_url(url):
    try:
        URLValidator(url)
        return True
    except ValidationError as e:
        return False


def scrapy_daemon():
    return ScrapydAPI(SCRAPYD_HOST)


def scrape_data(url, names, values, types):
    response = requests.get(url)
    response = TextResponse(body=response.content, url=url)
    data = {'url': response.url}
    for name in names:
        index = names.index(name)
        value = values[index]
        extract_type = types[index]

        if extract_type == 'list':
            data = {**data, **{name: response.xpath(value).extract()}}
        else:
            data = {**data, **{name: response.xpath(value).extract_first()}}

    return data
