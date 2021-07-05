import random
import time
command = "F"
while command != "Выйти":
    command = input("Выбирете что запустить:\nа)Калькулятор\nб)Мини игры\n")
    while command != "а" and command != "б" and command != "Выйти":
        command = input("ERROR: UNKNOUN COMMAND Введите корректную команду:")
    while command == "а":
       a = int(input("Введите любое число:"))
       b = int(input("Введите любое 2-е число:"))
       x = input("Введите номер действия:\n1)Сложение\n2)Вычитание\n3)Умножение\n4)Деление с дробями\n5)Деление нацело\n6)Деление нацело с остатком\n7)Остаток\n8)возведение в степень\n")
       while x != "1" and x != "2" and x != "3" and x != "4" and x != "5" and x != "6" and x != "7" and x != "8":
           x = input("Выбирете 1 из предоставленных выше вариантов")
       if x == "1":
           c = a + b
           print(c)
       elif x == "2":
           c = a - b
           print(c)
       elif x == "3":
           c = a * b
           print(c)
       elif x == "4":
           c = a / b
           print(c)
       elif x == "5":
           c = a // b
           print(c)
       elif x == "6":
           c = a // b
           d = a % b
           print(c + " (ост.:" + d + ")")
       elif x == "7":
           c = a % d
           print(c)
       else:
           c = a ** b
           print(c)
       command = input("Чтобы сбросить вычисления введите что угодно кроме 1:")
    while command == "б":
        command = input("Введите 1 из доступных вариантов:\n1)Угадай число 0-10\n2)Чепуха\n3)В разработке\n")
        while command != "1" and command != "2" and command != "3":
            commant = input("Выбирете 1 из доступных вариантов:")
        while command == "1":
            print("Угадай число 0-10")
            time.sleep(1)
            x = random.randint(0, 10)
            y = int(input("Число заданно, угадайте число от 0 до 10\n"))
            while y != x:
                while y < 0 and y > 10:
                    y = input("Вам нужно ввести число от 0 до 10 в этой игре:")
                y = int(input("Неверно! Попробуйте другое число:"))
            if y == x:
                command = "б"
        while command == "2":
            print("Чепуха")
            time.sleep(1)
            otv1 = input("Кто?")
            otv2 = input("С кем?")
            otv3 = input("Когда?")
            otv4 = input("Где?")
            otv5 = input("Что делали?")
            otv6 = input("Кто пришел?")
            otv7 = input("Что сказал?")
            otv8 = input("Что ему ответили?")
            otv9 = input("Чем все это закончилось?")
            print("Однажды " + otv1 + " вместе " + otv2 + " " + otv3 + " " + otv4 + " " + otv5 + " А потом пришел " + otv6 + " И сказал " + otv7 + " Ему ответили " + otv8 + " Это закончилось тем что " + otv9)
            command = "б"
        while command == "3":
            print("В разработке", end = "")
            time.sleep(1)
            print(".", end = "")
            time.sleep(1)
            print(".", end = "")
            time.sleep(1)
            print(".")
            time.sleep(1)
            input("coming soon)")
            command = "б"
