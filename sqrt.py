import math


def is_square(n):
    num = math.isqrt(n)
    if num * num == n:
        return True
    else:
        return False



print(is_square(17))



# def is_square(n):
#     return n > -1 and math.sqrt(n) % 1 == 0;