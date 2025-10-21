# Python Calculator 

operator = input("Enter operator (+, -, *, /): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


if operator == "+":
    result = num1 + num2
    print(round(result))

elif operator == "-":
    result = num1 - num2
    print(result)

elif operator == "*":
    result = num1 * num2
    print(result)

elif operator == "/":
    result = num1 / num2
    print(round(result, 3))   # rounding to 3 decimal places
else:
    print("The operator is not valid!")
