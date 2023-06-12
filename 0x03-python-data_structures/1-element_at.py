#!/usr/bin/python3
# 1-element_at.py

def element_at(my_list, idx):
    """Retrieve an element from a list."""
    return my_list[idx] if 0 <= idx < len(my_list) else None

# Test the function
if __name__ == "__main__":
    # Example list
    my_list = [1, 2, 3, 4, 5]
    index = 2
    result = element_at(my_list, index)
    print(f"The element at index {index} is: {result}")
