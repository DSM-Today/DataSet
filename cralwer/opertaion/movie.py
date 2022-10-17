from selenium import webdriver
from selenium.webdriver.common.by import By


def fetch_movie():
    driver = webdriver.Chrome("../chromedriver")
    driver.get("https://www.megabox.co.kr/")

    movie = driver.find_element(By.XPATH, '//*[@id="main_section01"]/div[2]/div[2]/ol/li[1]')

    image = movie.find_element(By.XPATH, '//*[@id="main_section01"]/div[2]/div[2]/ol/li[1]/a/img').get_attribute(
        'src')

    name = movie.find_element(By.XPATH, '//*[@id="main_section01"]/div[2]/div[2]/ol/li[1]/a/img').get_attribute(
        'alt')

    movie.find_element(By.XPATH, '//*[@id="main_section01"]/div[2]/div[2]/ol/li[1]/div/div/a').click()

    url = driver.current_url

    return {
        'image': image,
        'name': name,
        'url': url
    }
