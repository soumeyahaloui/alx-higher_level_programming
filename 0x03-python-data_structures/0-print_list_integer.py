#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for num in my_list:
        print("{:d}".format(num))

# Test the function
if __name__ == "__main__":
    # Example list
    my_list = [1, 2, 3, 4, 5]
    print_list_integer(my_list)
