num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation: +  -  *  /")
op = input("Enter operator: ")

if op == "+":
    print("Result:", num1 + num2)

elif op == "-":
    print("Result:", num1 - num2)

elif op == "*":
    print("Result:", num1 * num2)

elif op == "/":
    if op=="/" and num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print("Result:", num1 / num2)

else:
    print("Invalid operator")