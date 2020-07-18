def condtion() :
    num1 = float(input("give number 1 \n "))
    num2 = float(input("give number 2 \n"))
    if num1*num2 > 1000:
        result = num1 + num2
    elif num1 * num2 < 1000 :
        result = num1*num2
    return (result)
print(condtion())

