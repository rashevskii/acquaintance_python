from math import pi


def pi_accuracy(d):
    print("Вывод числа пи с заданной точность {} = {:.{}f}".format(d, pi, d))

pi_accuracy(4)
