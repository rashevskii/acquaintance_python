


from random import choice


arr = [i for i in range(0, 20)]
print("Исходный список - ", arr)
shuffled_arr = []
while len(shuffled_arr) != len(arr):
  random_el = choice(arr)
  if not random_el in shuffled_arr:
    shuffled_arr.append(random_el)
print("Перемешанный список - ", shuffled_arr)
