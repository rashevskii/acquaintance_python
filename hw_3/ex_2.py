arr = [2,3,4,5,6,7,8]

left_index = 0
right_index = len(arr) - 1
if len(arr) % 2 == 0:
  arr_middle = (len(arr) // 2)
else:
  arr_middle = (len(arr) // 2) + 1
pow_arr = []

for i in range(0, arr_middle):
  print(i)
  pow_arr.append(arr[left_index] * arr[right_index])
  left_index += 1
  right_index -= 1 
print(pow_arr)
