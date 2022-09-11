# arr = [1.1, 1.2, 3.1, 5, 10.01]
arr = []
counter = 5
while counter > 0:
  arr.append(float(input("Введите вещественное число: ")))
  counter -= 1
fractions = []
for el in arr:
  frac = float("{:.2f}".format(el - int(el)))
  if frac > 0:
    fractions.append(frac)
res = max(fractions) - min(fractions)
print(res)
