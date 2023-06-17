from setuptools import setup

setup(
    name='clean_folder',  
    version='1.0', 
     # Список пакетів, які входять до пакету clean_folder
    packages=['clean_folder'], 

    # Вказуємо точку входу для консольного скрипту
    entry_points={  
        'console_scripts': [
            # Команда clean-folder буде викликати функцію main з модуля clean.py
            'clean-folder=clean_folder.clean:main'  
        ]
    },

    install_requires=[
        # перелік залежностей 
    ]
)

