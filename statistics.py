import json
from datetime import datetime
import tkinter as tk1
from tkinter import ttk

class Statisics_Database:
    def __init__(self, filename):
        self.filename = filename

        # Проверка наличия файла базы данных
        try:
            with open(filename, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = []

    def add_statistics(self, sentence, errors, typing_time):
        entry = {
            "sentence": sentence,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time_added": datetime.now().strftime("%H:%M:%S"),
            "errors": errors,
            "typing_time": typing_time
        }
        self.data.append(entry)
        self.save()

    def clear_data(self):
        self.data = []
        self.save()

    def save(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)

    def print_data(self):
        for entry in self.data:
            print(f"Sentence: {entry['sentence']}")
            print(f"Date: {entry['date']}")
            print(f"Time Added: {entry['time_added']}")
            print(f"Errors: {entry['errors']}")
            print(f"Typing Time: {entry['typing_time']}")
            print("--------------------------")

class DatabaseApp(tk1.Tk):
    def __init__(self, database_file):
        super().__init__()
        self.title("Статистика упражений")

        self.database = Statisics_Database(database_file)

        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("sentence", "date", "time_added", "errors", "typing_time")
        self.tree.heading("sentence", text="Предложение")
        self.tree.heading("date", text="Дата")
        self.tree.heading("time_added", text="Время добавления")
        self.tree.heading("errors", text="Количество ошибок")
        self.tree.heading("typing_time", text="Скорость написания")
        self.tree.pack()

        self.load_data()

    def load_data(self):
        self.tree.delete(*self.tree.get_children())
        for entry in self.database.data:
            self.tree.insert("", tk1.END, values=(entry['sentence'], entry['date'], entry['time_added'], entry['errors'], entry['typing_time']))




statistics_database = Statisics_Database("data.json")

sentence = "Привет, мир!"
errors = 2
typing_time = 10

#statistics_database.add_sentence(sentence, errors, typing_time)

#statistics_database.print_data()
#statistics_database_app = DatabaseApp("data.json")



