def prime_factors(number):
    res = []
    divider = 2
    while divider * divider <= number:
        if number % divider == 0:
            res.append(divider)
            number //= divider
        else:
            divider += 1
    if number > 1:
        res.append(number)
    return res

factors = prime_factors(3554)
print(factors)
