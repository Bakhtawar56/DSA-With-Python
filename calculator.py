first=input("Enter first number:")
operator=input("enter opeartor +,-/,%,*:")
second=input("enter second number:")



if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)

else:
    print("invalid operation")