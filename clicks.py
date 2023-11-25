import json


class ClicksDatabase:
    def __init__(self, database_file):
        self.database_file = database_file
        self.database = self.load_database()

    def load_database(self):
        try:
            with open(self.database_file, "r") as file:
                database = json.load(file)
        except FileNotFoundError:
            database = {}

        return database

    def save_database(self):
        with open(self.database_file, "w") as file:
            json.dump(self.database, file, indent=4)

    def increase_clicks(self, letter):
        letter = letter.lower()

        if letter in self.database:
            self.database[letter] += 1
        else:
            self.database[letter] = 1

        self.save_database()

    def get_clicks(self, letter):
        letter = letter.lower()

        if letter in self.database:
            return self.database[letter]
        else:
            return 0

    def clear_database(self):
        self.database = {}
        self.save_database()

    def display_database(self):
        for letter, clicks in self.database.items():
            print(f"Буква: {letter}, Количество неправильных нажатий: {clicks}")


DATABASE_FILE = "clicks_database.json"
clicks_database = ClicksDatabase(DATABASE_FILE)
