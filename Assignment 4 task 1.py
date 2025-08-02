# Task 1: Read a File and Handle Errors
# Problem Statement:  Write a Python program that:

# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.
try:
    file = open("simple.txt","r")
    Reading_file=file.read()
    for line in Reading_file.splitlines():
      print(line)
    file.close()
except FileNotFoundError:
 print("The file simple.txt was not found.")