number = int(input("Введите число: "))
count = 1
for i in range(1, number + 1):
  count *= i
  print(count, end=" ")
print()
