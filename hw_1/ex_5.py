a_x = int(input("Введите координату x точки A: "))
a_y = int(input("Введите координату y точки A: "))
b_x = int(input("Введите координату x точки B: "))
b_y = int(input("Введите координату y точки B: "))

c_x, c_y = a_x, b_y

ac_length = a_y - c_y
if ac_length < 0:
  ac_length *= -1

bc_length = b_x - c_x
if bc_length < 0:
  bc_length *= -1

ab_length = ((ac_length ** 2) + (bc_length ** 2)) ** 0.5
print(f"Длина отрезка AB: {ab_length:.2f}")
