from PrimeFactorization.WheelFactorization import wheel_factorization


def number_of_divisors(number):
    prime_factors = wheel_factorization(number)
    res = 1
    for elem in prime_factors.values():
        res *= elem + 1

    return res
