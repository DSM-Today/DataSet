from requests import get
from bs4 import BeautifulSoup as bs

from datetime import datetime, timedelta
from random import randrange

import pprint


def get_weeday():
    return (datetime.utcnow() + timedelta(hours=9)).weekday()


class WebToon:

    def __init__(self):
        self._basic_uri = 'https://comic.naver.com/webtoon'
        self._list_uri = self._basic_uri + '/weekday'

    def get_today_toon_list(self):
        content = bs(get(self._list_uri).text, 'lxml')

        today_content = content.findAll(class_='col_inner')[0]# [get_weeday()]
        today = today_content.find_all_next('a')

        return self.parse_today_toon_list(today)


    def parse_today_toon_list(self, html_content):
        toon_list = []

        for ind, val in enumerate(html_content):
            if ind % 2 == 1:
                continue
            try:
                str_val = str(val)
                toon_info = {
                    'status': val.text.strip(),  # 휴재 & 18세 이상 이용 가능 & NEW
                    'direct_url': self._basic_uri + str_val[str_val.index('<a href="/webtoon') + 17: str_val.index(
                        '" onclick')],
                    'title': str_val[str_val.index('<img alt="') + 10: str_val.index('" height=')],
                    'image_path': str_val[str_val.index(" src=") + 6: str_val.index('" title=')]
                }

                toon_list.append(toon_info)
            except:
                pass
        return toon_list


if __name__ == '__main__':
    toon = WebToon()
    toon_list = toon.get_today_toon_list()

