# Function to find HCF/GCD
def find_hcf(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

# Input two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Call the function to find HCF/GCD
hcf = find_hcf(num1, num2)

# Display the result
print(f"The HCF/GCD of {num1} and {num2} is {hcf}.")
