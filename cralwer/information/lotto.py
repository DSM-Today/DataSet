from requests import get
from bs4 import BeautifulSoup as bs


class Lotto:

    def crawl(self):
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
