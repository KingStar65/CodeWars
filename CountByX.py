def count_by(x, n):
    list = []
    max = x*n
    loop = range(x, max+1, x)
    for c in loop:
        list.append(c)
    return list

print(count_by(2,5))

# def count_by(x, n):
#     return [i * x for i in range(1, n + 1)]
# def count_by(x, n):
#     arr = []
#     for num in range(1, n+1):
#         result = x * num
#         arr.append(result)
#     return arr