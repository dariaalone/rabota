

print('Hello World!')

class Student:
    print("привет")

def new_greeting():
    return "Добро пожаловать в наше приложение!"
print(new_greeting())

try:
    number = int(input("Введите число: "))
    print(f"Вы ввели: {number}")
except ValueError:
    print("Ошибка: введите число")