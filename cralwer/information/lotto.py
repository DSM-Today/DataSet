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
                prize: 상금,
                round: 몇 회차,
                date: 뽑은 날짜,
                winning_amount: 당첨 복권 개수
            }:
        '''

        html = self._get_html()

        winner_info = self._get_balls_and_prize(html)

        time_info = self._get_round_and_date(html)

        winner_info.update(time_info)

        return winner_info

    @staticmethod
    def _get_html():
        return get('https://search.naver.com/search.naver?query=로또').text

    @staticmethod
    def _get_round_and_date(html):
        round_scope = bs(html, 'lxml').find(class_='text _select_trigger _text')
        turn, date = round_scope.text.split()
        return {
            'round': turn,
            'date': date
        }

    @staticmethod
    def _get_balls_and_prize(html):
        result, winner_info = {}, bs(html, 'lxml').find(class_='win_number_box')

        for i, j in enumerate(winner_info.select('span')):
            result[i] = j.get_text()

        result['prize'] = winner_info.find('strong').get_text() + '원'

        winning_amount = winner_info.find('p').text

        result['winning_amount'] = winning_amount[winning_amount.find('('):]

        return result
