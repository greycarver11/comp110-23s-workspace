"""Practicing importing from other modules"""

from lessons.my_functions import addition

if __name__ == "__main__":
    print("howdy")

print(addition(1,2))

# print(my_functions.addition(1,2))

# print(my_functions.my_variable)