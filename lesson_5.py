"""1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
Об окончании ввода данных будет свидетельствовать пустая строка."""

out_f = open("out_file.txt", "w")
while True:
    my_string = input("Введите данные : ")
    if my_string == "":
        break
   # my_string = my_string + "\n"
    out_f.write(my_string)
out_f.close()

"""2.Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и 
слов в каждой строке."""

with open('Text.txt','r', encoding='utf-8') as f_str:
    i=0
    for line in f_str:
        my_str = line.split()
        i += 1
        print(f"В строке {i} количество слов = {len(my_str)}")
    print(f"Количество строк = {i}")

"""3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов 
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. 
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32 """

with open('Staff.txt','r', encoding='utf-8') as f_str:
    i=0
    staff_sum = 0
    for line in f_str:
        my_str = line.split()
        i += 1
        staff_sum = staff_sum + float(my_str[1])
        if float(my_str[1]) < 20000:
            print(my_str[0])
        staff_sum = staff_sum / i
    print(f"Средняя величина дохода сотрудников = {staff_sum}")

"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны
 заменяться на русские. Новый блок строк должен записываться в новый текстовый файл."""

with open('New.txt','w', encoding='utf-8') as f_wrt:
    with open('Number.txt', 'r', encoding='utf-8') as f_str:
        my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
        print (my_dict.get('One'))
        for line in f_str:
            my_str = line.split()
            print(my_str)
            my_string = my_dict.get(my_str[0]) + ' ' + my_str[1] + ' ' + my_str[2] + '\n'
            f_wrt.write(my_string)

"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить её на экран."""

with open('Number_sum.txt','w', encoding='utf-8') as f_str:
    my_string = input("Введите числа через пробел : ")
    f_str.write(my_string)
with open('Number_sum.txt','r', encoding='utf-8') as f_str:
    my_sum = 0
    my_str = f_str.read()
    my_str = my_str.split()
    for num in my_str:
        my_sum = my_sum + float(num)
    print(f"Сумма равна  = {my_sum}")

"""6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и 
наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. 
Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""

import re
report = {}
with open('Lesson.txt', 'r', encoding='UTF-8') as my_file:
    my_text = my_file.read()
    my_file.seek(0)
    for row in my_file:
        row_items = row.split(': ')
        hours = re.findall(r"\d+", row_items[1])
        report.update({row_items[0]: sum([int(i) for i in hours])})
print(report) 

"""7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать 
данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста."""

import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('firms.txt', 'r') as my_file:
    for line in my_file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')
