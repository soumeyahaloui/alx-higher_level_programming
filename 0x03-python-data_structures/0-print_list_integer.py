#!/usr/bin/python3
# 0-print_list_integer.py

def print_list_integer(my_list=[]):
    """Print all integers of a list."""
    for num in my_list:
        print("{:d}".format(num))

# Test the function
if __name__ == "__main__":
    # Example list
    my_list = [1, 2, 3, 4, 5]
    print_list_integer(my_list)
