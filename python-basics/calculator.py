# simple calculator
operator = input("Enter an operator (+ - * /):")
a = float(input("Enter the first digit:"))
b = float(input("Enter the second digit:"))      # Type casting used
c = 0
if operator == "+":
    c = a+b
    print(f"{a} + {b} = {c}")
elif operator == "-":
    c = a - b
    print(f"{a} - {b} = {c}")
elif operator == "*":
    c = a * b
    print(f"{a} * {b} = {c}")
elif operator == "/":
    c = a / b
    print(f"{a} / {b} = {c}")
else:
    print("Enter a valid operator")
