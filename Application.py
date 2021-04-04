from PrimeFactorization.WheelFactorization import wheel_factorization
from PrimeFactorization.NumberOfDivisors import number_of_divisors
from PrimeFactorization.SumOfDivisors import sum_of_divisors
from Euclid.GCD import gcd
from Euclid.LCM import lcm
from Euclid.ExtendedGCD import extended_gcd


def generate_prime_factors_for(number):
    print(wheel_factorization(number))
    print(number_of_divisors(number))
    print(sum_of_divisors(number))


if __name__ == '__main__':
    print(gcd(39, 26))
    print(lcm(39, 26))
    print(extended_gcd(17389, 7927))
