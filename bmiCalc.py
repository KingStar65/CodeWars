def bmi(weight, height):
    bmi = 0
    bmi = weight / (height ** 2)

    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"


print(bmi(65, 1.76))