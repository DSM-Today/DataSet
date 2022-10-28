from time import sleep

import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver as webdriver
from selenium.webdriver.common.by import By

from config import get_chromedriver_path


class Food:

    def crawl(self):
        '''
        :return {
            name: 음식 이름,
            image_path: 사진 경로
        }:
        '''

        food_name = self._get_food_name()
        image_path = self._get_food_image_path(food_name)

        return {
            'name': food_name,
            'image_path': image_path
        }

    @staticmethod
    def _get_food_name():
        driver = webdriver.Chrome(get_chromedriver_path())
        driver.get("http://dogumaster.com/select/menu/")

        driver.find_element(By.XPATH, '//*[@id="section_search"]').find_element(By.ID, "input_submit").click()

        sleep(3)

        return driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[4]/p').text

    @staticmethod
    def _get_food_image_path(food_name):
        url = "https://www.google.co.kr/search?q={food_name}&sxsrf=ALiCzsZWgcEwVPp9s9R7qr0PdCdsKlPZqg:1665327432124&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjLrJqQtNP6AhVMtlYBHdSLBt8Q_AUoAXoECAEQAw&biw=1034&bih=839&dpr=2".format(
            food_name=food_name)
        html = requests.get(url)
        soup = bs(html.text, "html.parser")
        return soup.find_all('img')[1]['src']
