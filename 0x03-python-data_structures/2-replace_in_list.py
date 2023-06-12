#!/usr/bin/python3
# 2-replace_in_list.py

def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position."""
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list

# Test the function
if __name__ == "__main__":
    # Example list
    my_list = [1, 2, 3, 4, 5]
    index = 2
    new_element = 9
    replaced_list = replace_in_list(my_list, index, new_element)
    print("Original list:", my_list)
    print("Replaced list:", replaced_list)
