from requests import get
from bs4 import BeautifulSoup as bs

from datetime import datetime, timedelta
from random import randrange


def get_weekday():
    return (datetime.utcnow() + timedelta(hours=9)).weekday()


class WebToon:

    def __init__(self):
        self._basic_uri = 'https://comic.naver.com'
        self._list_uri = self._basic_uri + '/webtoon/weekday'

    def crawl(self):
        '''
        :return {
            is_adult: 18세 이상 판별 !문구!
            rank: 해당 요일에서의 순위
            is_working: '연재' 또는 '휴재' 라는 !문구!
            direct_url: 바로 가기
            title: 제목
            image_path: 이미지 경로
            writer: 작가
            introduction: 소개글
            genre: 장르
        }:
        '''

        today_toon_list = self._get_today_toon_list()

        return self.__get_toon_detail(today_toon_list)

    def _get_today_toon_list(self):
        content = bs(get(self._list_uri).text, 'lxml')

        today_content = content.findAll(class_='col_inner')[get_weekday()].ul

        return self._parse_today_toon_list([today_content.li] + today_content.li.find_next_siblings())

    @staticmethod
    def __get_toon_detail(web_toon_list: list):
        rank = randrange(0, len(web_toon_list))
        chosen_toon = web_toon_list[rank]
        content = bs(get(chosen_toon['direct_url']).text, 'lxml').find(class_='detail')

        return {
            'is_adult': chosen_toon['g_rated'],
            'rank': rank,
            'is_working': chosen_toon['published'],
            'direct_url': chosen_toon['direct_url'],
            'title': chosen_toon['title'],
            'image_path': chosen_toon['image_path'],
            'writer': content.find(class_='wrt_nm').text.strip(),
            'introduction': content.find('p').text.strip(),
            'genre': content.find(class_='genre').text.strip()
        }

    def _parse_today_toon_list(self, html_content_list):
        toon_list = []

        for val in html_content_list:
            toon_list.append(
                {
                    'g_rated': val.find('span',{'class':'mark_adult_thumb'}).text if val.find('span',{'class':'mark_adult_thumb'}) is not None else '18세 이하 이용 가능',
                    'published': '휴재' if val.em is not None and val.em.text == '휴재' else '연재',
                    'title': val.img['alt'],
                    'direct_url': self._basic_uri + val.a.attrs['href'],
                    'image_path': val.img['src']
                }
            )

        return toon_list

