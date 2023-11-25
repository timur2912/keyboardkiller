from sentenses import *
import tkinter as tk
from tkinter import font as tkfont
from clicks import *
from heatmap import *
from statistics import *
import time

class KeyboardKillerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('KeyboardKiller')
        self.root.configure(bg="black")
        self.custom_font = tkfont.Font(size=16)

        self.text_label = tk.Label(self.root, text="", font=self.custom_font, bg="black")
        self.text_label.pack()

        self.input_entry = tk.Entry(self.root, font=self.custom_font, width=40)
        self.input_entry.pack()

        self.button_frame1 = tk.Frame(self.root, bg="black")

        self.new_attempt_button = tk.Button(self.button_frame1, text="Новоя попытка", font=self.custom_font, command=self.new_attempt)
        self.new_attempt_button.config(width=15)
        self.new_attempt_button.pack(side=tk.LEFT)

        self.new_sentence_button = tk.Button(self.button_frame1, text="Добавить упражнение", font=self.custom_font, command=self.new_sentence)
        self.new_sentence_button.config(width=15)
        self.new_sentence_button.pack(side=tk.LEFT)
        self.button_frame1.pack()

        self.button_frame2 = tk.Frame(self.root, bg="black")
        self.heatmap_button = tk.Button(self.button_frame2, text="Heatmap", font=self.custom_font, command=clicks_analyzer.plot_heatmap)
        self.heatmap_button.config(width=15)
        self.heatmap_button.pack(side=tk.LEFT)

        self.delete_clicks_button = tk.Button(self.button_frame2, text="Очистить Heatmap", font=self.custom_font, command=clicks_database.clear_database)
        self.delete_clicks_button.config(width=15)
        self.delete_clicks_button.pack(side=tk.LEFT)
        self.button_frame2.pack()
        self.button_frame3 = tk.Frame(self.root, bg="black")
        self.statistics_button = tk.Button(self.button_frame3, text="Статистика", font=self.custom_font, command=self.show_statistics)
        self.statistics_button.config(width=15)
        self.statistics_button.pack(side=tk.LEFT)

        self.delete_statistics_button = tk.Button(self.button_frame3, text="Очистить Статистику", font=self.custom_font, command=statistics_database.clear_data)
        self.delete_statistics_button.config(width=15)
        self.delete_statistics_button.pack(side=tk.LEFT)
        self.button_frame3.pack()
        self.label_frame = tk.Frame(self.root, bg="black")
        self.mistakes_label = tk.Label(self.label_frame, text="Ошибки", font=self.custom_font, bg="black")
        self.mistakes_label.pack()

        self.timer_label = tk.Label(self.label_frame, text="Время", font=self.custom_font, bg="black")
        self.timer_label.pack()

        self.speed_label = tk.Label(self.label_frame, text="Скорость печати:", font=self.custom_font, bg="black")
        self.speed_label.pack()

        self.label_frame.pack()

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

# Размеры окна
        self.window_width = 430
        self.window_height = 230

# Вычисление координат для центрирования окна
        self.x = (self.screen_width - self.window_width) // 2
        self.y = (self.screen_height - self.window_height) // 2

# Установка положения окна
        self.root.geometry(f"{self.window_width}x{self.window_height}+{self.x}+{self.y}")
        self.root.mainloop()

    def new_attempt(self):
        self.flag = True
        self.mistakes = 0
        self.start_time = time.time()
        self.input_entry.delete(0, tk.END)
        self.sentence = database.get_random_sentence()
        self.text_label.config(text=self.sentence, fg="white")
        self.input_entry.bind("<KeyRelease>", self.check_string)


    def add_statistics(self, sentence, mistakes, speed):
        if self.flag:
            statistics_database.add_statistics(sentence, mistakes, speed)
        return


# Функция завершения попытки попытки
    def delay_function(self):
        self.text_label.config(text="")
        self.timer_label.config(text="Время: ")
        self.input_entry.delete(0, tk.END)
        self.mistakes_label.config(text="Ошибки", fg="white")
        self.speed_label.config(text="Скорость печати:", fg="white")
        self.input_entry.unbind("<KeyRelease>", self.check_string)


# Функция проверки правильности введённой строки
    def check_string(self, event):
        input_string = self.input_entry.get()
        # print(sentence)
        expected_string = self.sentence
        result = ""

        if len(input_string) > len(expected_string):
            result = "Строка неправильная"
        elif input_string == expected_string:
            current_time = time.time() - self.start_time
            seconds = int(current_time)
            milliseconds = int((current_time % 1) * 1000)
            formatted_time = "{:02d}.{:03d}".format(seconds, milliseconds)
            self.text_label.config(text="Правильно", fg="green")
            self.timer_label.config(text="Время: " + formatted_time, bg="black")
            self.speed_label.config(text="Скорость печати: " + str(format(len(sentence) / float(formatted_time), ".2f")) + " символов в секунду", bg="black")
            self.add_statistics(self.sentence, self.mistakes, format(len(sentence) / float(formatted_time), ".2f"))
            self.flag = False
            self.text_label.after(1400, self.delay_function)
            return

        else:
            for i, char in enumerate(input_string):
                if char == expected_string[i]:
                    result += char
                else:
                    clicks_database.increase_clicks(expected_string[i])
                    self.mistakes += 1
                    self.mistakes_label.config(text="Ошибки: " + str(self.mistakes), fg="red")
                    self.input_entry.delete(i, tk.END)
                    result += "-"

        def show_statistics(self):
            statistics_database_app = DatabaseApp("data.json")


    def new_sentence(self):
        self.text_label.config(text="Введите предложение", fg="white")
        self.input_entry.delete(0, tk.END)
        try:
            self.input_entry.unbind("<KeyRelease>", self.check_string)
        except:
            pass
        self.input_entry.bind("<Return>", self.add_new_sentence)

    def show_statistics(self):
        statistics_database_app = DatabaseApp("data.json")

    def add_new_sentence(self, event):
        self.text = self.input_entry.get()
        database.add_sentence(self.text)
        self.input_entry.delete(0, tk.END)
        self.text_label.config(text="", fg="white")
        self.input_entry.unbind("<Return>")
    def run(self):
        self.root.mainloop()

app = KeyboardKillerApp()
app.run()
