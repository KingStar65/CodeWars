def number(lines):
    count = 1
    newList = []
    for x in lines:
        newList.append(str(count) + ": " + x)
        count += 1
    return newList

myList = ["a", "b", "c"]
print(number(myList))