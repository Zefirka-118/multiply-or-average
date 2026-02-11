# Ask the user for 5 numbers.
# Then ask whether they want to multiply them
# or calculate the average.
# Two functions are required.

def multiply_numbers(a, b, c, d, e):
    return a * b * c * d * e


def average_numbers(a, b, c, d, e):
    return (a + b + c + d + e) / 5


print("Please enter 5 numeric values:")

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))
num4 = int(input("Number 4: "))
num5 = int(input("Number 5: "))

print("\nWhich operation would you like to perform?")
print("1 - Multiply")
print("2 - Average")

option = input("Enter your option (1 or 2): ")

if option == "1":
    result = multiply_numbers(num1, num2, num3, num4, num5)
    print(f"The multiplication result is: {result}")

elif option == "2":
    result = average_numbers(num1, num2, num3, num4, num5)
    print(f"The average result is: {result}")

else:
    print("Invalid option. Please try again ¯\\_(ツ)_/¯")
