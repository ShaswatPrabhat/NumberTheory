def extended_gcd(num1, num2):
    if num1 == 0:
        return num2, 0, 1
    gcd, x1, y1 = extended_gcd(num2 % num1, num1)

    x = y1 - (num2 // num1) * x1
    y = x1

    return gcd, x, y
