import re
import string

def strip_punctuation_ru(data):

    # Создаем таблицу перевода, которая заменяет все знаки препинания на пустую строку.
    table = str.maketrans("", "", string.punctuation + "«»")

    # Удаляем знаки препинания из строки.
    data = data.translate(table)

    # Разделяем строку на слова и удаляем пустые элементы.
    words = data.split()
    words = [word for word in words if word]

    # Возвращаем строку, состоящую из слов, разделенных одним пробелом.
    return " ".join(words)
def strip_punctuation_ru(data):
    # Удаление знаков препинания с использованием регулярного выражения
    return re.sub(r'[^\w\s]', '', data)

def test_strip_punctuation_ru():
    test_cases = [
        ("Привет, как дела?", "Привет как дела"),
        ("Это текст с точкой. И запятой, ну и тире – ещё!", "Это текст с точкой И запятой ну и тире ещё"),
        ("Проверка... точек", "Проверка точек"),
        ("...,!-@", "")  # Пустая строка после удаления всех знаков пунктуации
    ]

    for test_case, expected_result in test_cases:
        result = strip_punctuation_ru(test_case)
        if result == expected_result:
            print("YES")
        else:
            print("NO")

test_strip_punctuation_ru()


import sys

data = sys.stdin.readline().strip()

print(strip_punctuation_ru(data))