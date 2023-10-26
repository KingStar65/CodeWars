def narcissistic(value):
    total = 0
    n = len(value)
    for char in value:
        num = int(char)
        newnum = num ** n
        total += newnum
    if total == int(value):
        return True
    else:
        return False  # Code away

#order = input("Input any value and i will tell you if it is narcissistic or not: ")
issit = narcissistic(str(154))
print(issit)
