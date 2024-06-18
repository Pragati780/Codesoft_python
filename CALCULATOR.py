def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Simple Calculator")
print("Basic operations are:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter choice (1/2/3/4): ")
    if choice in [1, 2, 3, 4]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            z=add(num1,num2)
            print('addition')
            print(z)

        elif choice == 2:
            z=subtract(num1, num2)
            print('substraction')
            print(z)

        elif choice == 3:
            print('multiplication of num1 and num2 is:', multiply(num1, num2))

        elif choice == 4:
            print("divisionm of num1 and num2 is:", divide(num1, num2))
        break

    else:
        print("Invalid Input. Please enter a valid option.")

