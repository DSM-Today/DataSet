from requests import get
from bs4 import BeautifulSoup as bs

from datetime import datetime, timedelta
from random import randrange

from pprint import pprint


def get_weeday():
    return (datetime.utcnow() + timedelta(hours=9)).weekday()


class WebToon:

    def __init__(self):
        self._basic_uri = 'https://comic.naver.com'
        self._list_uri = self._basic_uri + '/webtoon/weekday'

    def get_today_toon_list(self):
        content = bs(get(self._list_uri).text, 'lxml')

        today_content = content.findAll(class_='col_inner')[get_weeday()].ul

        return self.parse_today_toon_list([today_content.li] + today_content.li.find_next_siblings())

    @staticmethod
    def get_toon_detail(web_toon_list: list):
        rank = randrange(0, len(web_toon_list))
        chosen_toon = web_toon_list[rank]
        content = bs(get(chosen_toon['direct_url']).text, 'lxml').find(class_='detail')

        return {
            'status': chosen_toon['status'],
            'rank': rank,
            'published': chosen_toon['published'],
            'direct_url': chosen_toon['direct_url'],
            'title': chosen_toon['title'],
            'image_path': chosen_toon['image_path'],
            'writer': content.find(class_='wrt_nm').text.strip(),
            'introduction': content.find('p').text.strip(),
            'genre': content.find(class_='genre').text.strip()
        }

    def parse_today_toon_list(self, html_content_list):
        toon_list = []

        for val in html_content_list:
            toon_list.append(
                {
                    'status': val.find('span',{'class':'mark_adult_thumb'}).text if val.find('span',{'class':'mark_adult_thumb'}) is not None else None,
                    'published': '연재' if val.find('em') is None or '' else '휴재',
                    'title': val.img['alt'],
                    'direct_url': self._basic_uri + val.a.attrs['href'],
                    'image_path': val.img['src']
                }
            )

        return toon_list

