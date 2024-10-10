number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    print(f'The greatest number is {num1}.')
elif num2 >= num1 and num2 >= num3:
    print(f'The greatest number is {num2}.')
else:
    print(f'The greatest number is {num3}.')

    