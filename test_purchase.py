from wsgiref.validate import assert_

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
    driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']").click()
    driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()

    # 3 оформление покупки
    driver.find_element(By.CLASS_NAME, "shoping_cart_link").click()
    driver.find_element(By.XPATH, "//button[text()='Checkout']").click()

    # Заполнение формы
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()

    # Завершение покупки
    driver.find_element(By.XPATH, "//button[text()='Finish']").click()

    # 4 Проверки успешной покупки/Завершение
    success_message = driver.find_element(By.CLASS_NAME, "complet-header").text
    assert "THANKS YOU FOR YOUR ORDER" in success_message

    print('Тест успешно завершен')

except Exception as e:
    print(f'Произошла ошибка: {e}')
finally:
    time.sleep(3) # Время ожидание для просмотра результата
    driver.quit()


