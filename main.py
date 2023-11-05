from sentenses import *
import tkinter as tk
from tkinter import font as tkfont
from clicks import *
from heatmap import *
from statistics import *
import time


def new_attempt():
    global sentence
    global mistakes
    global start_time
    global flag
    flag = True
    mistakes = 0
    start_time = time.time()
    input_entry.delete(0, tk.END)
    sentence = get_random_sentence()
    text_label.config(text=sentence, fg="white")
    input_entry.bind("<KeyRelease>", check_string)


def add_statistics(sentence, mistakes, speed):
    global flag
    if flag:
        statistics_database.add_statistics(sentence, mistakes, speed)
    return


# Функция завершения попытки попытки
def delay_function():
    text_label.config(text="")
    timer_label.config(text="Время: ")
    input_entry.delete(0, tk.END)
    mistakes_label.config(text="Ошибки", fg="white")
    speed_label.config(text="Скорость печати:", fg="white")
    input_entry.unbind("<KeyRelease>", check_string)


# Функция проверки правильности введённой строки
def check_string(event):
    global sentence
    global mistakes
    global start_time
    global flag
    input_string = input_entry.get()
    # print(sentence)
    expected_string = sentence
    result = ""

    if len(input_string) > len(expected_string):
        result = "Строка неправильная"
    elif input_string == expected_string:
        current_time = time.time() - start_time
        seconds = int(current_time)
        milliseconds = int((current_time % 1) * 1000)
        formatted_time = "{:02d}.{:03d}".format(seconds, milliseconds)
        text_label.config(text="Правильно", fg="green")
        timer_label.config(text="Время: " + formatted_time, bg="black")
        speed_label.config(text="Скорость печати: " + str(format(len(sentence) / float(formatted_time), ".2f")) + " символов в секунду", bg="black")
        add_statistics(sentence, mistakes, format(len(sentence) / float(formatted_time), ".2f"))
        flag = False
        text_label.after(1400, delay_function)
        return

    else:
        for i, char in enumerate(input_string):
            if char == expected_string[i]:
                result += char
            else:
                clicks_database.increase_clicks(expected_string[i])
                mistakes += 1
                mistakes_label.config(text="Ошибки: " + str(mistakes), fg="red")
                input_entry.delete(i, tk.END)
                result += "-"


def delete_clicks():
    clicks_database.clear_database()
    return

def delete_statistics():
    statistics_database.clear_data()
    return

def show_statistics():
    statistics_database_app = DatabaseApp("data.json")


def new_sentence():
    text_label.config(text="Введите предложение", fg="white")
    input_entry.delete(0, tk.END)
    try:
        input_entry.unbind("<KeyRelease>", check_string)
    except:
        pass
    input_entry.bind("<Return>", add_new_sentence)


def add_new_sentence(event):
    text = input_entry.get()
    add_sentence(text)
    input_entry.delete(0, tk.END)
    text_label.config(text="", fg="white")
    input_entry.unbind("<Return>")


# Графичкский интерейс
root = tk.Tk()
root.title('KeyboardKiller')
root.configure(bg="black")

custom_font = tkfont.Font(size=16)

text_label = tk.Label(root, text="", font=custom_font, bg="black")
text_label.pack()

input_entry = tk.Entry(root, font=custom_font)
input_entry = tk.Entry(root, width=40)
input_entry.pack()

button_frame1 = tk.Frame(root, bg="black")

new_attempt_button = tk.Button(button_frame1, text="Новоя попытка", font=custom_font, command=new_attempt)
new_attempt_button.config(width=15)
new_attempt_button.pack(side=tk.LEFT)

new_sentence_button = tk.Button(button_frame1, text="Добавить упражнение", font=custom_font, command=new_sentence)
new_sentence_button.config(width=15)
new_sentence_button.pack(side=tk.LEFT)
button_frame1.pack()

button_frame2 = tk.Frame(root, bg="black")
heatmap_button = tk.Button(button_frame2, text="Heatmap", font=custom_font, command=plot_heatmap)
heatmap_button.config(width=15)
heatmap_button.pack(side=tk.LEFT)

delete_clicks_button = tk.Button(button_frame2, text="Очистить Heatmap", font=custom_font, command=delete_clicks)
delete_clicks_button.config(width=15)
delete_clicks_button.pack(side=tk.LEFT)
button_frame2.pack()

button_frame3 = tk.Frame(root, bg="black")
statistics_button = tk.Button(button_frame3, text="Статистика", font=custom_font, command=show_statistics)
statistics_button.config(width=15)
statistics_button.pack(side=tk.LEFT)

delete_statistics_button = tk.Button(button_frame3, text="Очистить Статистику", font=custom_font, command=delete_statistics)
delete_statistics_button.config(width=15)
delete_statistics_button.pack(side=tk.LEFT)
button_frame3.pack()

label_frame = tk.Frame(root, bg="black")

mistakes_label = tk.Label(label_frame, text="Ошибки", font=custom_font, bg="black")
mistakes_label.pack()

timer_label = tk.Label(label_frame, text="Время", font=custom_font, bg="black")
timer_label.pack()

speed_label = tk.Label(label_frame, text="Скорость печати:", font=custom_font, bg="black")
speed_label.pack()

label_frame.pack()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Размеры окна
window_width = 400
window_height = 220

# Вычисление координат для центрирования окна
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Установка положения окна
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.mainloop()
