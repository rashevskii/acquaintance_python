from random import randint
from turtle import position
number = int(input("Введите число для последовательности: "))
arr = []
for num in range(1, number + 1):
  arr.append(randint(-number, number + 1))
print(arr)

positions = input("Укажите номера позиций для произведения через пробел: ")
power = 1
arr_pos = positions.split(" ")
for el in arr_pos:
  num_el = int(el)
  if num_el < len(arr):
    power *= arr[num_el]
print(power)
