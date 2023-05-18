# -*- coding: utf-8 -*-
"""Задача 2.1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dchtMj_x8pHFMnIGil8v8ZnPlS1OOil5

Задача 2.1.
Создайте две функции maximum и minimum,
которые получают список целых чисел в качестве входных данных
и возвращают наибольшее и наименьшее число в этом списке соответственно.
Например,

* [4,6,2,1,9,63,-134,566] -> max = 566, min = -134
* [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
* [42, 54, 65, 87, 0] -> min = 0, max = 87
* [5] -> min = 5, max = 5
функции sorted, max и min использовать нельзя!
def minimum(arr): pass

def maximum(arr): pass
"""

def minimum(arr): 
  min_num = arr[0] 
  for num in arr:
    if num < min_num:
     min_num += num
     return (min_num)

def maximum(arr):
  max_num = arr[0]
  for num in arr:
   if num > max_num:
    max_num = num
    return (max_num)

# Тесты
print(minimum([4,6,2,1,9,63,-134,566])) # -134
print(maximum([4,6,2,1,9,63,-134,566])) # 566

print(minimum([-52, 56, 30, 29, -54, 0, -110])) # -110
print(maximum([-52, 56, 30, 29, -54, 0, -110])) # 56

print(minimum([42, 54, 65, 87, 0])) # 0
print(maximum([42, 54, 65, 87, 0])) # 87

print(minimum([5])) # 5
print(maximum([5])) # 5