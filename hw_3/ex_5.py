n = int(input("Введите число для расчета Фибоначчи: "))
fib1 = fib2 = 1
neg_fib1 = 1
neg_fib2 = -1

neg_fib = [1, -1]
pos_fib = [1, 1]

for i in range(2, n):
  neg_fib1, neg_fib2 = neg_fib2, neg_fib1 - neg_fib2
  neg_fib.append(neg_fib2)

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    pos_fib.append(fib2)
    
neg_fib.reverse()
res = neg_fib + [0] + pos_fib
print(res)
