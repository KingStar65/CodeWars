def count_sheeps(sheep):
    count = 0
    for x in sheep:
        if x:
          count += 1
    return count;

array1 = [True,  True,  True,  False,
                  True,  True,  True,  True ,
                  True,  False, True,  False,
                  True,  False, False, True ,
                  True,  True,  True,  True ,
                  False, False, True,  True ];

result = count_sheeps(array1)
print(result)

"""
def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)
"""
