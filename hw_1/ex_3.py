x_coord = int(input("Введите кардинату X: "))
y_coord = int(input("Введите координату Y: "))

if x_coord == 0:
  print("Точка лежит на оси X")
elif y_coord == 0:
  print("Точка лежит на оси Y")
elif x_coord > 0 and y_coord > 0:
  print("Точка лежит в первой четверти")
elif x_coord < 0 and y_coord > 0:
  print("Точка лежит во второй четверти")
elif x_coord < 0 and y_coord < 0:
  print("Точка лежит в третьей четверти")
elif x_coord > 0 and y_coord < 0:
  print("Точка лежит в четвертой четверти")
