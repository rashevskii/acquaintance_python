number = int(input("Введите число: "))
arr = []
for i in range(1, number + 1):
  arr.append(round((1 + 1 / i) ** i, 2))
counter = 0
for el in arr:
  counter += el

print(counter)
