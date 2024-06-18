# Задание 1
# import requests

# # Отправка GET-запроса к API GitHub для поиска репозиториев с кодом html
# response = requests.get('https://api.github.com/search/repositories', params={'q': 'html'})
#
# # Распечатка статус-кода ответа
# print(f"Статус-код ответа: {response.status_code}")
#
# # Распечатка содержимого ответа в формате JSON
# print("Содержимое ответа в формате JSON:")
# print(response.json())

# Отправка GET-запроса с параметром userId, равным 1
# Задание 2
# import requests
#
# response = requests.get('https://jsonplaceholder.typicode.com/posts', params={'userId': 1})
#
# # Распечатка полученных записей
# print("Полученные записи:")
# print(response.json())

# Создание словаря с данными для отправки
# Задание 3
import requests
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправка POST-запроса с данными
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)

# Распечатка статус-кода и содержимого ответа
print(f"Статус-код ответа: {response.status_code}")
print("Содержимое ответа:")
print(response.json())