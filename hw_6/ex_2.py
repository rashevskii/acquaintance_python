# def non_repeating_numbers(some_arr):
#   return list(set(some_arr))

# arr = [46, 46, 2, 8, 15, 105, 105, 10, 365, 105, 95, 11, 789, 23, 1]
# numbers = non_repeating_numbers(arr)
# print(numbers)

arr = [46, 46, 2, 8, 15, 105, 105, 10, 365, 105, 95, 11, 789, 23, 1]
non_repeating_numbers = lambda some_arr : list(set(some_arr))
print(non_repeating_numbers(arr))