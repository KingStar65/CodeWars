
def digital_root(n):
    # ...
    if n < 10:
        return n

    total = 0
    nstr = str(n)
    for char in nstr:
        num = int(char)
        total += num
    return digital_root(total)


print(digital_root(16))      # Output: 7
print(digital_root(942))     # Output: 6
print(digital_root(132189))  # Output: 6
print(digital_root(493193))  # Output: 2