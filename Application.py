from PrimeFactorization.WheelFactorization import wheel_factorization
from PrimeFactorization.NumberOfDivisors import number_of_divisors
from PrimeFactorization.SumOfDivisors import sum_of_divisors


def generate_prime_factors_for(number):
    print(wheel_factorization(number))
    print(number_of_divisors(number))
    print(sum_of_divisors(number))


if __name__ == '__main__':
    generate_prime_factors_for(1800)
