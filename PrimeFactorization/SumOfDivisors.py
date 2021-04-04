import math

from PrimeFactorization.WheelFactorization import wheel_factorization


def sum_of_divisors(number):
    prime_factors = wheel_factorization(number)
    res = 1
    for elem in prime_factors.keys():
        res *= (math.pow(elem, prime_factors[elem] + 1) - 1) / (elem - 1)

    return res
