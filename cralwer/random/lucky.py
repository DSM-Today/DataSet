from requests import get
from bs4 import BeautifulSoup as bs4


class Lucky:

    def __init__(self):
        self._date_list = [
            ['0120', '0218'],
            ['0219', '0320'],
            ['0321', '0419'],
            ['0420', '0520'],
            ['0521', '0621'],
            ['0622', '0722'],
            ['0723', '0822'],
            ['0823', '0923'],
            ['0924', '1022'],
            ['1023', '1122'],
            ['1123', '1224'],
            ['1225', '0119'],
        ]
        self._star_list = ['물병자리', '물고기자리', '양자리', '황소자리', '쌍둥이자리', '게자리', '사자자리', '처녀자리', '천칭자리', '전갈자리', '사수자리',
                           '염소자리']

    def crawl(self, mmdd: int):
        '''
        :param mmdd:
        :returns {
            name: 운세,
            period: 운세 기간,
            content: 운세 소개
        }:
        '''

        star = self._get_star(mmdd)

        response = self._get_response(star)

        return {
            'content': self._parse(response),
            'name': self._star_list[star],
            'index': star + 1
        }

    def _get_star(self, mmdd: int):
        for i, day in enumerate(self._date_list):
            s, e = day
            if int(s) <= mmdd <= int(e):
                return i
        raise IndexError

    def _get_response(self, sequence_num: int):
        return get(
            f'https://search.naver.com/search.naver?query={self._star_list[sequence_num] + " 운세"}'
        ).text

    def _parse(self, response_html: str):
        return bs4(response_html, 'lxml').find(class_='text _cs_fortune_text').contents[0]
