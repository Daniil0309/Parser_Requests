from bs4 import BeautifulSoup
from googletrans import Translator
import requests

def get_english_word():
    url = 'https://randomword.com/'
    try:
        response = requests.get(url)


        soup = BeautifulSoup(response.content, 'html.parser')
        english_words = soup.find('div', id='random_word').text.strip()
        word_definition = soup.find('div', id='random_word_definition').text.strip()
        return {'english_words': english_words,
                'word_definition': word_definition}

    except:
        print('Error')

def world_game():
    print('Добро пожаловать в игру')
    while True:
        word_dict = get_english_word()
        word = word_dict.get('english_words')
        word_definition = word_dict.get('word_definition')

        translator = Translator()
        word = translator.translate(word, dest='ru').text
        word_definition = translator.translate(word_definition, dest='ru').text

        print(f"Значение слова - {word_definition}")
        user = input('Ваш ответ - ')
        if user == word:
            print('Все верно!')
        else:
            print(f"Неправильно. Правильное значение -{word}")

        play_again = input('Хотите сыграть еще? (Y/N) ')
        if play_again.lower() == 'y':
            continue
        else:
            print('Спасибо за игру!')
            break

world_game()

