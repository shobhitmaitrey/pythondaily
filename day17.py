#  Conditional statements in Python are used to make decisions in your code based on certain conditions. 
#  The if, else, and elif (short for "else if") keywords are commonly used for this purpose. 


# Example: Checking if a number is positive, negative, or zero

# Taking user input for a number
num = float(input("Enter a number: "))

# Using if, elif, and else statements to check the conditions
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
