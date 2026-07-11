def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose: +  -  *  /")
op = input("Operator: ")

if op == "+":
    print(add(num1, num2))
elif op == "-":
    print(sub(num1, num2))
elif op == "*":
    print(mul(num1, num2))
elif op == "/":
    print(div(num1, num2))
else:
    print("Invalid operator")