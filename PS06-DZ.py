from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Firefox()

url = 'https://www.divan.ru/krasnodar/category/svet'

driver.get(url)

time.sleep(5)

product = driver.find_elements(By.CLASS_NAME, '_Ud0k')

parsed_data = []

for item in product:
    try:
        title = item.find_element(By.CSS_SELECTOR, 'span.name').text
        price = item.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU KIkOH').text
        link = item.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8 qUioe').get_attribute('href')
    except:
        print("Произошла ошибка парсинга")
        continue

    parsed_data.append([title.text, price.text, link])

driver.quit()

with open('divan.csv','w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)
