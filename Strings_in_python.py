""" In Python, strings are immutable, meaning their values cannot be changed after they are created. 
When you perform operations on strings, such as concatenation or slicing, 
a new string object is created, and the original string remains unchanged. """

# Strings: str objects are immutable. For example:
# python code
s = "hello"
# Attempting to change a character in the string will raise an error
# s[0] = 'H'  # This will result in a TypeError
# In this case, if you want to modify the string, you would create a new one:

# python code
s = "hello"
s = "H" + s[1:]



# Lists: list objects are mutable. For example:
# python code
lst = [1, 2, 3]
# You can modify elements in the list
lst[0] = 0


''' This distinction is important because it affects how you work with these data types in your code. 
Immutability has advantages, such as making strings hashable and ensuring safety in concurrent operations. 
If you need a mutable sequence of characters, you can use a list and then convert it back to a string when needed.'''
