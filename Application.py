from PrimeFactorization.WheelFactorization import wheel_factorization


def generate_prime_factors_for(number):
    print(wheel_factorization(number))


if __name__ == '__main__':
    generate_prime_factors_for(34000)
