"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у 
пользователя, предусмотреть обработку ситуации деления на ноль."""

def my_func(num1,num2):
    try:
        num3 = num1 / num2
    except Exception:
        print("Вы ввели неверное значение 2-го числа. ")
        return
    else:
        return num3
my_number1 = float(input("Введите число 1: "))
my_number2 = float(input("Введите число 2: "))
print(my_func(my_number1,my_number2))

"""2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
 год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
 Осуществить вывод данных о пользователе одной строкой."""

def my_func(**kwargs):
    return print(*kwargs.values())

print(my_func(name=input('Введите имя: '),s_name=input('Введите фамилию: '),date_birth=input('Введите год рождения: '),
            city=input('Введите город проживания: '),email=input('Введите email: '), tel=input('Введите телефон: ')))

"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает
сумму наибольших двух аргументов."""

def my_func(num1,num2,num3):
    my_list=[num1,num2,num3]
    my_list.sort()
    my_sum=my_list[1]+my_list[2]
    return my_sum
my_number1 = float(input("Введите число 1: "))
my_number2 = float(input("Введите число 2: "))
my_number3 = float(input("Введите число 3: "))
print(my_func(my_number1,my_number2,my_number3))

"""4. Программа принимает действительное положительное число x и целое отрицательное число y. Выполните возведение 
числа x в степень y. Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без встроенной
 функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
 Второй — более сложная реализация без оператора **, предусматривающая использование цикла."""

# Первый способ
def my_func(x,y):
    my_exp=1/x**y
    return my_exp
# Второй способ
def my_func1(x,y):
    my_exp=1
    for i in range(abs(y)):
        my_exp=my_exp*x
    my_exp=1/my_exp
    return my_exp
my_number1 = int(input("Введите число x: "))
my_number2 = int(input("Введите целое отрицательно число y: "))
print(f"Первый способ: {my_func(my_number1,my_number2)}")
print(f"Второй способ: {my_func1(my_number1,my_number2)}")

"""5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter
должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
 Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введён
 после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого
 завершить программу."""

def my_func(my_str):
    my_str = my_str.split()
    func_sum=0
    flag=0
    for el in my_str:
        if el=="q":
            flag = 1
            continue
        func_sum=func_sum+int(el)
    return func_sum,flag
print("Cимвол q - выход из программы")
my_sum=0
flag=0
while True:
    my_string = input("Введите строку чисел через пробел: ")
    sum_func,flag = my_func(my_string)
    my_sum=my_sum+sum_func
    print(f"сумма равна: {my_sum}")
    if flag==1:
        break

"""6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
 но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text."""

def int_func(my_str):
    my_str = my_str.capitalize()
    return my_str
my_string=input("Введите слова из маленьких латинских букв: ")
print(f"Слово с прописной буквы: {int_func(my_string)}")

"""7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
 Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
 но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func()."""

def int_func(my_str):
    my_str = my_str.capitalize()
    return my_str

my_string=input("Введите слова через пробел: ")
my_string = my_string.split()
i=0
while i<len(my_string):
    print(int_func(my_string[i])," ",end="")
    i+=1
