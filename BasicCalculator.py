# Building a calculator

x = float(input("Give me a number: "))
o = input("Give me an operator: ")
y = float(input("Give me a second number: "))

if o == "+":
    print(x + y)
elif o == "-":
    print(x - y)
elif o == "*":
    print(x * y)
elif o == "/":
    print(x / y)
elif o == "**":
    print(x ** y)
else:
    print(f"Error: unknown operator \"{o}\"")