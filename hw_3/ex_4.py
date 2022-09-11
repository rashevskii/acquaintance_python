number = int(input("Введите чмсло для перевода в двоичное представление: "))
temp_num = number
temp = []
while temp_num > 0:
  temp.append(temp_num % 2)
  temp_num //= 2
temp.reverse()
res = ""
for el in temp:
  res += str(el)
print(f"Число {number} в двоичном представлении: {res}")
