import re

def is_correct_mobile_phone_number_ru(number):
    # Удаляем все пробелы и дефисы из номера
    number = number.replace(" ", "").replace("-", "")

    # Проверяем, что номер начинается с 8 или +7
    if not number.startswith("8") and not number.startswith("+7"):
        return False

    # Проверяем, что после 8 или +7 идет трехзначный код оператора
    if len(number) < 11 or not number[1:4].isdigit():
        return False

    # Проверяем, что после кода оператора идет 7 цифр
    if not number[4:].isdigit() or len(number[4:]) != 7:
        return False

    return True

def test_is_correct_mobile_phone_number_ru():
    # Тестовые данные
    test_cases = [
        "+7 999 123-45-67",
        "+7(900)1234567",
        "8 (999) 123-45-67",
        "+79991234567",
        "89991234567",
        "+7 999 123 45 67",
        "+7 999 12 34 567",
        "+7 999 1234567",
        "+7 (999) 1234567",
        "+7(999)1234567",
        "+7 999 123-45-6",
        "+7 999 123-45-678",
        "+7 999 123 45 6",
    ]

    # Запуск тестов
    for number in test_cases:
        if is_correct_mobile_phone_number_ru(number):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    test_is_correct_mobile_phone_number_ru()

import sys
def main():
    phone_number = sys.stdin.readline().strip()

    if is_correct_mobile_phone_number_ru(phone_number):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
