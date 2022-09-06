import string


fl_num = float(input("Введите вещественное число: "))
arr_num = str(fl_num).split(".")

sum = 0
for item in arr_num:
  for el in item:
    sum += int(el)
print(sum)
