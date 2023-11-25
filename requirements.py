import os
import subprocess
from main import *
def install_dependencies():
    try:
        subprocess.check_call(["python", "-m", "pip", "install", "-r", "requirements.txt"])
        print("Зависимости установлены успешно!")
    except subprocess.CalledProcessError:
        print("Ошибка установки зависимостей.")

install_dependencies()

if __name__ == "__requirements__":
    install_dependencies()
    app.run()
