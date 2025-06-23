#Task 1
import time
import math
import operator
from functools import reduce
import os
import string

path = input("Enter the path to list directories and files")

print("\n Directories: ")
# list only directories
directories = [d for d in os.listdir(
    path) if os.path.isdir(os.path.join(path, d))]
print(directories)
print("\nFiles:")
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
print(files)

list_all = os.listdir(path)
print("all files")
print(list_all)

#Task 2
path = input("Enter the path to check for access")
if os.path.exists(path):
    print("The path exists")
    # checking if its readable
    if os.access(path, os.R_OK):
        print("The file is read able")
    else:
        print("the file is not readble")
    # checking if the path is writable
    if os.access(path, os.W_OK):
        print("the path is write able")
    else:
        print("the file is not readable")
    if os.access(path, os.X_OK):
        print("the file is execuatble")
    else:
        print("the file is not execuatble.")
else:
    print("the file does not exist")

# TASK 3

all_list = ''
path = input("please insert your desired path: ")
if os.path.exists(path):
    all_list = os.path.dirname(path)
    print(all_list)
    file_name = os.path.basename(path)
    print(file_name)
else:
    print("access is not allowed")

# task 4

file_name = input("please insert your File name: ")

try:
    # open the file in read more
    with open(file_name, "r") as file:
        # intializing the line count;
        line_count = 0
        for line in file:
            line_count += 1
    print("The total number of line is", line_count)
except FileExistsError:
    print("The file does not exist. Please check the filename and try again")

# Task 5:

my_list = ["apple", "banana", "cherry", "Date"]
# Getting the file name from the user
file_name = input(
    "please insert the filename of ur txt file with txt extension")
# open the file in write mode
with open(file_name, "w") as file:
    for item in my_list:
        file.write(item + '\n')
print("List has been written to ", file_name)

# task 6
"""
file_name = 'A'
for i in string.ascii_uppercase:
    file_name = f"{i}.txt"  # it creats the filename
    with open(file_name, "w") as file:
        file.write(f"this is the fle for the letter {i}.")
print("26 txt files have been created")
"""

# task 7

sourcr_file = input("Enter the name of the source file(with .txt extension): ")
destination_file = input("Enter the name of the destination file (with .txt)")
try:

    with open(sourcr_file, 'r') as src:
        content = src.read()
    with open(destination_file, 'w') as dest:
        dest.write(content)
    print("Content copied successfully from",
          sourcr_file, "to", destination_file)
except FileNotFoundError:
    print("the source file does not exist. please check the filename and try again")

# task 8

file_path = input("Enter the path of the file to delete: ")

if os.path.exists(file_path):
    print("The file exists.")

    if os.access(file_path, os.W_OK):

        try:
            os.remove(file_path)
            print("The file has been deleted successfully.")
        except Exception as e:
            print("An error occurred while trying to delete the file:", e)
    else:
        print("The file is not writable. Cannot delete the file.")
else:
    print("The file does not exist.")


numbers = [2, 3, 4, 5]

result = reduce(operator.mul, numbers)
print("Multiplication of all numbers:", result)

# task2: count the uppercase and lowercase letter in a string


def count_case(text):
    upper_case = sum(1 for c in text if c.isupper())
    lower_case = sum(1 for c in text if c.islower())
    print("Uppercase letters:", upper_case)
    print("Lowercase letters:", lower_case)


# Example:
count_case("Hello World!")

# task 3

def is_palindrome(s):
    return s == s[::-1]

# Example:
string = "madam"
if is_palindrome(string):
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")


def delayed_sqrt(num, delay_ms):
    time.sleep(delay_ms / 1000)
    result = math.sqrt(num)
    print(f"Square root of {num} after {delay_ms} milliseconds is {result}")


# Example:
delayed_sqrt(25100, 2123)


t = (True, 1, "hello", 3.14)

print("All elements are true:", all(t))