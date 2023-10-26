def square_digits(num):
    numStr = str(num)
    total = ""
    for digit in numStr:
        val = int(digit)
        newVal = str(val ** 2)
        total += newVal
    return int(total)

print(square_digits(765))

# solution
# def square_digits(num):
#     ret = ""
#     for x in str(num):
#         ret += str(int(x)**2)
#     return int(ret)