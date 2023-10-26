def printer_error(s):
    error = 0
    for x in s:
        if x > 'm':
            error += 1
    errate = str(error) + "/" + str(len(s))
    # errate = f"{error}/{len(s)}"
    return errate

test = printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz")
print(test)

# best practise
# from re import sub
# def printer_error(s):
#     return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))