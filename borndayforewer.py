"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

def question_date(question, date):
    answer = input(question)
    while answer != date:
        print('Ошибочка...')
        answer = input(question)

question_date('Введите год рождения Пушкина:\n', '1799')
question_date('Введите день рождения Пушкина:\n', '6')
print('ok')
