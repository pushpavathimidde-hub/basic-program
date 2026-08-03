def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "cannot divide by zero"
    return a%b
def power(a,b):
    return a**b

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 7:
        print("calculator closed")
        break

    if choice < 1 or choice > 7:
        print("Invalid input")
        continue

    num1 =float(input("Enter a number:"))
    num2 = float(input("enter a number:"))

    if choice == 1:
        print("Result:", add(num1, num2))
    elif choice == 2:
        print("Result:", subtract(num1, num2))
    elif choice == 3:
        print("Result:", multiply(num1, num2))
    elif choice == 4:
        print("Result:", divide(num1, num2))
    elif choice == 5:
        print("Result:", modulus(num1, num2))
    elif choice == 6:
        print("Result:", power(num1, num2))
