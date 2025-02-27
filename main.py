def show_menu():
    print("\nSelect the operation:")
    print("1. Subtraction")
    print("2. Addition")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def calculate():
    while True:
        show_menu()
        choice = input("Enter the number of the desired operation (1/2/3/4/5): ")

        if choice == '5':
            print("Thank you for using the calculator! Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid option! Try again.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Error: Invalid input. Please enter numbers only.")
            continue

        if choice == '1':
            result = num1 - num2
            print(f"\n{num1} - {num2} = {result}")
        elif choice == '2':
            result = num1 + num2
            print(f"\n{num1} + {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"\n{num1} * {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("\nError: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"\n{num1} / {num2} = {result}")

if __name__ == "__main__":
    print("Welcome to the Python Calculator!")
    calculate()