from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import Keys
import time

# настройка драйвера
driver = webdriver.Chrome()
driver.implicitly_wait(10)


try:
    # 1. Авторизация
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.ID, 'user_name').send_keys('standart_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    # 2 Выбор товара
    driver.find_element(By.XPATH, '//div[text()='Sauce Labs Backpack']').click()
    driver.find_element(By.XPATH, '//button[text()='Add to cart']').click()

