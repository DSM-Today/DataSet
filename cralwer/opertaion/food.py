from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests
from bs4 import BeautifulSoup as bs


def fetch_food():
    driver = webdriver.Chrome("../chromedriver")
    driver.get("http://dogumaster.com/select/menu/")

    driver.find_element(By.XPATH, '//*[@id="section_search"]').find_element(By.ID, "input_submit").click()

    sleep(3)

    food_name = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[4]/p').text


    url = "https://www.google.co.kr/search?q={food_name}&sxsrf=ALiCzsZWgcEwVPp9s9R7qr0PdCdsKlPZqg:1665327432124&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjLrJqQtNP6AhVMtlYBHdSLBt8Q_AUoAXoECAEQAw&biw=1034&bih=839&dpr=2".format(food_name=food_name)
    html = requests.get(url)
    soup = bs(html.text, "html.parser")
    food_image = soup.find_all('img')[1]['src']


    return {
        "food_name": food_name,
        "food_image": food_image
    }