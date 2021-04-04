import math


def wheel_factorization(number):
    prime_factorization = dict()
    counter = 0
    while number % 2 == 0:
        counter += 1
        number = number // 2

    prime_factorization[2] = counter
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        counter = 0
        while number % i == 0:
            number = number // i
            counter += 1
        if counter >= 1:
            prime_factorization[i] = counter

    if number > 2:
        prime_factorization[number] = 1

    return prime_factorization
