a = input("Введите число: ")   #Обработка исключений 
b = input("Введите еще одно: ")
a = int(a)
b = int(b)
try:
    print(a / b)
except ZeroDivisionError:
    print("b не может быть нулем. ")
