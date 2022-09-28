import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

class News:

    def __init__(self):
        url = 'https://news.naver.com/'

        response = requests.get(url)

        html_text = response.text

        self.soup = bs(html_text, "html.parser")

    def get_news(self):
        arr = self.soup.findAll("div", class_="cjs_journal_wrap _item_contents")
        link = arr[0].find_next("a", class_="cjs_news_a _cds_link _editn_link")['href']
        image = arr[0].find_next("img")['src']
        title = arr[0].find_next("div", class_="cjs_t").text
        content = arr[0].find_next("p", class_="cjs_d").text
        return {
            'link': link,
            'image': image,
            'title': title,
            'content': content
        }