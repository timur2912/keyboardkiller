import json
import random


class SentenceDatabase:
    def __init__(self, file_name):
        self.file_name = file_name
        self.database = self.load_database()

    def load_database(self):
        try:
            with open(self.file_name, "r") as file:
                database = json.load(file)
        except FileNotFoundError:
            database = []
        return database

    def save_database(self):
        with open(self.file_name, "w") as file:
            json.dump(self.database, file)

    def add_sentence(self, sentence):
        self.database.append(sentence)
        self.save_database()
        print("ADDED SENTENCE: " + sentence)

    def get_sentences(self):
        return self.database

    def get_random_sentence(self):
        if not self.database:
            return None
        random_sentence = random.choice(self.database)
        return random_sentence


# Пример использования класса SentenceDatabase
DATABASE_FILE = "sentences_database.json"

# Создаем объект базы данных
database = SentenceDatabase(DATABASE_FILE)
