from random import randint


def polynomial(k):
    factors = [randint(1,101) for _ in range(0, k + 1)]
    res = ""
    for i in range(0, len(factors)):
      if i == len(factors) - 1:
          res += f"{factors[i]} = 0"
      elif k == 1:
        res += f"{factors[i]}x + "
      else:
          res += f"{factors[i]}x^{k} + "
      k -= 1
    with open("polynomial.txt", "w", encoding="utf-8") as f:
        f.write(res)

polynomial(4)
