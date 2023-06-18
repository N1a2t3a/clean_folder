import os

def process_folder(path):
    # Створення порожніх списків для файлів та папок
    files = []
    directories = []

    # Перебір елементів у папці
    for item in os.listdir(path):
        # Отримання повного шляху до елемента
        item_path = os.path.join(path, item)
        # Перевірка, чи є елемент файлом
        if os.path.isfile(item_path):
            # Додавання імені файлу до списку файлів
            files.append(item)
        # Перевірка, чи є елемент папкою
        elif os.path.isdir(item_path):
            # Додавання імені папки до списку папок
            directories.append(item)

    # Виведення списку файлів
    print("Files:")
    for file in files:
        print(file)

    # Виведення списку папок
    print("Directories:")
    for directory in directories:
        print(directory)

# Приклад виклику функції process_folder з поточної папки
process_folder('.')

