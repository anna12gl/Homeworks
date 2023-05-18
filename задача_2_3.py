# -*- coding: utf-8 -*-
"""Задача 2.3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mF4PnHqO8G7zbh9vXJfxM5jSih8YbakR

## Задача 2.3.
####Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
*Например,
switch_it_up(1) -> 'One'
switch_it_up(3) -> 'Three'
switch_it_up(10000) -> None
#### Использовать условный оператор if-elif-else нельзя!
def switch_it_up(number): pass
"""

def switch_it_up(number):
 num_dict = {
0: 'Zero',
1: 'One',
2: 'Two',
3: 'Three',
4: 'Four',
5: 'Five',
6: 'Six',
7: 'Seven',
8: 'Eight',
9: 'Nine'
}
 return num_dict.get(number, None)

#проверка работы функции
print(switch_it_up(1))   # 'One'
print(switch_it_up(3))   # 'Three'
print(switch_it_up(0))   # 'Zero'
print(switch_it_up(7))   # 'Seven'
print(switch_it_up(10))  # None