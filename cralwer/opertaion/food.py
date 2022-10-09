from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests
from bs4 import BeautifulSoup as bs

class Food:
    def fetchFood(self):
        driver = webdriver.Chrome("../chromedriver")
        driver.get("http://dogumaster.com/select/menu/")

        driver.find_element(By.XPATH, '//*[@id="section_search"]').find_element(By.ID, "input_submit").click()

        sleep(3)

        foodName = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[4]/p').text


        url = "https://www.google.co.kr/search?q={foodName}&sxsrf=ALiCzsZWgcEwVPp9s9R7qr0PdCdsKlPZqg:1665327432124&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjLrJqQtNP6AhVMtlYBHdSLBt8Q_AUoAXoECAEQAw&biw=1034&bih=839&dpr=2".format(foodName=foodName)
        html = requests.get(url)
        soup = bs(html.text, "html.parser")
        foodImage = soup.find_all('img')[1]['src']


        return {
            "foodName": foodName,
            "foodImage": foodImage
        }