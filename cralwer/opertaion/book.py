from requests import get
from bs4 import BeautifulSoup as bs

from random import randint


def get_random_index(max: int):
    return randint(1, max - 1)


class Book:

    def crawl(self):
        json = self.get_json()

        random_book = self.get_random_book(json)

        return self.get_book_information(random_book)

    @staticmethod
    def get_json():
        return get(
            'https://product.kyobobook.co.kr/api/gw/pub/pdt/best-seller/online?'
            'page=1&per=20&period=001&dsplDvsnCode=000&dsplTrgtDvsnCode=001'
        ).json()

    @staticmethod
    def get_random_book(json: dict):
        seller_list = json['data']['bestSeller']
        rand_int = get_random_index(len(seller_list))

        return seller_list[rand_int]

    @staticmethod
    def get_book_information(random_book_info: dict):
        return {
            'review_amount': random_book_info['buyRevwNumc'],
            'review_score': random_book_info['buyRevwRvgr'],
            'writer': random_book_info['chrcName'],
            'name': random_book_info['cmdtName'],
            'introduction': random_book_info['inbukCntt'],
            'publisher': random_book_info['pbcmName'],
            'published_at': random_book_info['rlseDate'],
            'page': random_book_info['upntAcmlAmnt'],
            'direct_url': 'https://product.kyobobook.co.kr/detail/' + random_book_info['saleCmdtid'],
            'image_path': f'https://contents.kyobobook.co.kr/sih/fit-in/100x0/pdt/{random_book_info["cmdtCode"]}.jpg'
        }
