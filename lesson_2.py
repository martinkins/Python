"""1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
 а указать явно, в программе."""

my_list = [2, 'text', 456, 45.3]
for i in my_list:
    print(f"Тип данных {i} - {type(i)}")

""" 2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 
2 и 3 и т. д. При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов 
нужно использовать функцию input()."""

list_quantity = int(input("Введите количество элементов списка: "))
my_list2 = list(range(list_quantity))
for i in range(list_quantity):
    my_list2[i] = int(input(f"Введите {i+1}-й элемент списка: "))
print(f"Список до обмена: {my_list2}")
for i in range(list_quantity//2):
    my_list2[i*2] ,my_list2[i*2+1]=my_list2[i*2+1],my_list2[i*2]
print(f"Список после обмена: {my_list2}")

"""3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц
 (зима, весна, лето, осень). Напишите решения через list и dict."""

number_month = int(input("Введите номер месяца от 1 до 12: "))
list_month=['январь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь']
dict_mouth = {1:'январь',2:'февраль',3:'март',4:'апрель',5:'май',6:'июнь',7:'июль',8:'август',9:'сентябрь',
10:'октябрь',11:'ноябрь',12:'декабрь'}
print(f"Решение через список : {list_month[number_month-1]}")
print(f"Решение через словарь : {dict_mouth[number_month]}")

"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. 
Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове."""

my_string = input("Введите строку : ")
my_string=my_string.split()
for i in range(len(my_string)):
    print(f"строка {i+1} : {my_string[i][:10]}")

""" 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2]"""

my_list = [7, 5, 3, 3, 2]
flag = 0
my_number = int(input("Введите число : "))
print(f"Рейтинг до изменений : {my_list}")
for i in range(len(my_list)):
    if my_number > my_list[i] and flag == 0:
        my_list.insert(i, my_number)
        flag = 1
if my_number <= my_list[len(my_list)-1]:
    my_list.append(my_number)
print(f"Новый рейтинг : {my_list}")
