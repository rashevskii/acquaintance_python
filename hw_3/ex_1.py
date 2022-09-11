arr = [2,3,5,9,3,12,5,24,8]
sum = 0
for i in range(0, len(arr)):
  if i % 2 != 0:
    sum += arr[i]
print(sum)
