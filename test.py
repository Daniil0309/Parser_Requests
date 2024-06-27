import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Servicefrom webdriver_manager.chrome import ChromeDriverManager

# Настраиваем веб-драйвер
url = 'https://www.divan.ru/krasnodar/category/svet'
driver = webdriver.Firefox()

# Открываем страницу
driver.get(url)

# Ищем все карточки товаров
cards = driver.find_elements(By.CLASS_NAME, "lsooF")

data = []
for card in cards:
    try:
        name = card.find_element(By.CLASS_NAME, "ui-GPFV8").text
    except:
        name = "N/A"
    try:
        price = card.find_element(By.CLASS_NAME, "ui-LD-ZU").text
    except:
        price = "N/A"
    try:
        link = card.find_element(By.TAG_NAME, "a").get_attribute("href")
    except:
        link = "N/A"

    data.append([name, price, link])

# Сохраняем данные в CSV файл
with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Название", "Цена", "Ссылка"])
    writer.writerows(data)

# Закрываем драйвер
driver.quit()