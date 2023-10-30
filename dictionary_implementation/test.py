# test.py
from mydictionary_wrapper import MyDict

# Create a new dictionary
my_dict = MyDict()

# Set values
my_dict.set_value("apple", 10)
my_dict.set_value("banana", 5)
my_dict.set_value("orange", 8)

# Get size
print("Dictionary size:", my_dict.get_size())

# Get values
print("Value of 'apple':", my_dict.get_value("apple"))
print("Value of 'banana':", my_dict.get_value("banana"))
print("Value of 'orange':", my_dict.get_value("orange"))
print("Value of 'grape':", my_dict.get_value("grape"))  # Key not found

# Update value
my_dict.set_value("apple", 15)
print("Updated value of 'apple':", my_dict.get_value("apple"))

# Destroy the dictionary
del my_dict