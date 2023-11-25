import json
import seaborn as sns
import matplotlib.pyplot as plt


class ClicksAnalyzer:
    def __init__(self, database_file):
        self.database_file = database_file
        sns.set()

    def load_database(self):
        try:
            with open(self.database_file, "r") as file:
                database = json.load(file)
        except FileNotFoundError:
            database = {}

        return database

    def create_heatmap_data(self, database):
        heatmap_data = [[database.get(chr(i + 1072), 0) for i in range(33)]]
        return heatmap_data

    def plot_heatmap(self):
        database = self.load_database()
        heatmap_data = self.create_heatmap_data(database)

        plt.figure(figsize=(10, 6))
        sns.heatmap(heatmap_data, cmap="YlOrRd", annot=True, fmt="d", linewidths=0.5, cbar=False)
        plt.xlabel("Буква")
        plt.ylabel("Количество неправильных нажатий")
        plt.xticks(range(33), [chr(i + 1072) for i in range(33)])
        plt.title("Хитмап количества неправильных нажатий на буквы")
        plt.show()


clicks_analyzer = ClicksAnalyzer("clicks_database.json")
