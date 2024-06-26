from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

driver = webdriver.Firefox()

url = 'https://www.divan.ru/krasnodar/category/svet'
driver.get(url)

# Ожидание загрузки элементов
wait = WebDriverWait(driver, 10)
product = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'LlPhw')))

parsed_data = []

for item in product:
    try:
        title = item.find_element(By.CSS_SELECTOR, 'span.ui-GPFV8.qUioe').text
        price = item.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH').text
        link = item.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8.qUioe').get_attribute('href')
        parsed_data.append([title, price, link])
    except Exception as e:
        print(f"Произошла ошибка парсинга: {e}")
        continue

driver.quit()

with open('divan.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)