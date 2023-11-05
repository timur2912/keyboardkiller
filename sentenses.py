import json
import random

DATABASE_FILE = "sentences_database.json"

# Функция для загрузки базы данных из файла JSON
def load_database():
    try:
        with open(DATABASE_FILE, "r") as file:
            database = json.load(file)
    except FileNotFoundError:
        database = []

    return database


# Функция для сохранения базы данных в файл JSON
def save_database(database):
    with open(DATABASE_FILE, "w") as file:
        json.dump(database, file)


# Функция для добавления предложения в базу данных
def add_sentence(sentence):
    database = load_database()
    database.append(sentence)
    save_database(database)
    print("ADDED SENTENSE:" + sentence)


# Функция для получения всех предложений из базы данных
def get_sentences():
    database = load_database()
    return database

# Функция для возвращения случайного предложения из базы данных
def get_random_sentence():
    database = load_database()
    if not database:
        return None
    random_sentence = random.choice(database)
    return random_sentence

# Добавляем предложения в базу данных
#add_sentence("Привет, как дела?")
#add_sentence("Какой сегодня день?")
#add_sentence("Какой ваш любимый цвет?")

# Получаем все предложения из базы данных
sentences = get_sentences()
for sentence in sentences:
    print(sentence)