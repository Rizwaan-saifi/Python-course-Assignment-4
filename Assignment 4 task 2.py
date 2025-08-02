
# Task 2: Write and Append Data to a File
# Problem Statement: Write a Python program that:

# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.

user_input= input("Enter text to write to the file : ")

with open("output.txt","w") as file:
    file.write(user_input+ "\n")
file.close()

print("Data successfully written to output.txt")
print("------------------------------------------------")

additional_text = input("Enter additional text to append : ")

with open("output.txt","a") as file:
    file.write(additional_text)
file.close()

print("Data successfully appended")
print("------------------------------------------------")


print("Final contents of output.txt : ")
file = open("output.txt","r")
Reading_file=file.read()
for line in Reading_file.splitlines():
    print(line)
file.close()
