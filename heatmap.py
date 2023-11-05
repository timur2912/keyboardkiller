import json
import seaborn as sns
import matplotlib.pyplot as plt

DATABASE_FILE = "clicks_database.json"


# Функция для загрузки базы данных из файла JSON
def load_database():
    try:
        with open(DATABASE_FILE, "r") as file:
            database = json.load(file)
    except FileNotFoundError:
        database = {}

    return database


# Функция для построения хитмапа
def plot_heatmap():
    database = load_database()

    # Создаем матрицу данных для хитмапа
    heatmap_data = [[database.get(chr(i + 1072), 0) for i in range(33)]]

    # Создаем отображение с помощью Seaborn
    sns.set()
    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_data, cmap="YlOrRd", annot=True, fmt="d", linewidths=0.5, cbar=False)
    plt.xlabel("Буква")
    plt.ylabel("Количество неправильных нажатий")
    plt.xticks(range(33), [chr(i + 1072) for i in range(33)])
    plt.title("Хитмап количества неправильных нажатий на буквы")
    plt.show()