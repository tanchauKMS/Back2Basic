# test.py
from myset_wrapper import MySet

# Create a new set
my_set = MySet()

# Add values
my_set.add("apple")
my_set.add("banana")
my_set.add("orange")
my_set.add("apple")  # Duplicate value

# Get size
print("Set size:", my_set.get_size())

# Get values
values = my_set.get_values()

# Print values
print("Set values:")
for value in values:
    print(value)

# Destroy the set
del my_set