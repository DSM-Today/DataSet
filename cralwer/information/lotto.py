from requests import get
from bs4 import BeautifulSoup as bs


class Lotto:

    def crawl(self):
        '''
        :return {
                0: 1번 로또 번호,
                1: 1번 로또 번호,
                2: 1번 로또 번호,
                3: 1번 로또 번호,
                4: 1번 로또 번호,
                5: 1번 로또 번호,
                6: 1번 로또 번호,
                prize: 상금
            }:
        '''

        html = self._get_html()

        return self._parse(html)

    @staticmethod
    def _get_html():
        return get('https://search.naver.com/search.naver?query=로또').text

    @staticmethod
    def _parse(html):
        result, winner_info = {}, bs(html, 'lxml').find(class_='win_number_box')

        for i, j in enumerate(winner_info.select('span')):
            result[i] = j.get_text()

        result['prize'] = winner_info.find('strong').get_text() + '원'

        return result
