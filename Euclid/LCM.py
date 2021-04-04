from Euclid.GCD import gcd


def lcm(num1, num2):
    return (num1 * num2) / gcd(num1, num2)
