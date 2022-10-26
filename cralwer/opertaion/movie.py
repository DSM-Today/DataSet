from selenium import webdriver
from selenium.webdriver.common.by import By


class Movie:

    def __init__(self):
        self._driver = webdriver.Chrome("../chromedriver")
        self._driver.get("https://www.megabox.co.kr/")

    def crawl(self):
        '''
        :return {
            name: 영화 이름,
            url: 바로 예매하러 가기 url,
            iamge_path: 사진 경로
        }:
        '''

        movie = self._driver.find_element(By.XPATH, '//*[@id="main_section01"]/div[2]/div[2]/ol/li[1]')

        image = movie.find_element(By.XPATH, '//*[@id="main_section01"]/div[2]/div[2]/ol/li[1]/a/img').get_attribute(
            'src')
        name = movie.find_element(By.XPATH, '//*[@id="main_section01"]/div[2]/div[2]/ol/li[1]/a/img').get_attribute(
            'alt')

        movie.find_element(By.XPATH, '//*[@id="main_section01"]/div[2]/div[2]/ol/li[1]/div/div/a').click()

        url = self._driver.current_url

        return {
            'name': name,
            'url': url,
            'image_path': image
        }
