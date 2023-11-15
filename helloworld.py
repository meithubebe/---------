#Вывод сто раз слово Привет мир!
# for i in range(100):
#     print("Привет, Мир!")



# x = 10
# y = 10
# z = x + y
# z 
# a = x - y
# a


# for i in range(1122):
#     print("Hello Everyone!")


# x = 100
# if x == 10:
#     print("10!")
# elif x == 20:
#     print("20!")
# else:
#     print("HZ BRO!")
# if x == 100:
#     print("X ravno 100!")
# if x % 2 == 0:
#     print("x chetnoe!")
# else:
#     print("x nechetnoe")

# 1: Zadanie

# print("Hello World!")
# print("Hello Everyone")
# print("My name Gustavo")


# 2 Zadanie


# usera_age = 100
# if usera_age < 10: 
#    print("Kruto Drug")
# elif usera_age == 20: 
#      print("Nice")
# else:
#     print("Ty Durak?")


# x = 10
# if x == 5:
#     print("Rovno 10!")
# elif x == 10:
#     print("Peremennaya bolshe 10!")
# else:
#     print("peremenna bolshe 25!")



# delimoe = float(input("Введите делимое число: "))
# delitel = float(input("Введите делитель: "))

# resutl_delenye = 24 / 12 
# ostatok = 24 % 12 

# print("Результат деления: ", resutl_delenye)
# print("Ostatok:", ostatok)




# age = input("Укажите возраст: ")
# int_age = int(age)
# if int_age < 21:
#     print("Вы молоды")
# else:
#     print("Ну ты и старик")



# def even_odd():
#    n = input("Введите число: ")
#    n = int(n)
#    if n % 2 == 0:
#     print("n - четное.")
#    else:
#     print("n - нечетное.")
# even_odd()
# even_odd()
# even_odd()



a = input("Введите число: ")   #Обработка исключений 
b = input("Введите еще одно: ")
a = int(a)
b = int(b)
try:
    print(a / b)
except ZeroDivisionError:
    print("b не может быть нулем. ")

