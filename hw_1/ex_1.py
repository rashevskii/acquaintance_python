number = int(input("Введите номер дня недели: "))
if 8 > number > 0:
  if number == 6 or number == 7:
    print("Выходной")
  else:
    print("Будний день")
else:
  print("Введен неверный номер дня недели")
