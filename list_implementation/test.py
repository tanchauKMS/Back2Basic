from mylist_wrapper import MyList

my_list = MyList()
my_list.append_item(1)
my_list.append_item(2)
my_list.append_item(3)
print(my_list.get_length())  # Output: 2
print(my_list.get_item(0))  # Output: 1
print(my_list.get_item(2))  # Output: 2