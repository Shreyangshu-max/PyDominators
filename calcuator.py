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

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Modulus (%)")
    print("7. Exit")
    
    while True:
        choice = input("\nEnter operation (1-7): ")
        
        if choice == '7':
            print("Exiting calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    result = add(num1, num2)
                    print(f"{num1} + {num2} = {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"{num1} - {num2} = {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"{num1} * {num2} = {result}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")
                elif choice == '5':
                    result = power(num1, num2)
                    print(f"{num1} ^ {num2} = {result}")
                elif choice == '6':
                    result = modulus(num1, num2)
                    print(f"{num1} % {num2} = {result}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select 1-7.")

# Run the calculator
if __name__ == "__main__":
    calculator()