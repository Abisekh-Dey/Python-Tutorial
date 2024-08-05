#1.Creating A New File
open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\Atm.txt","x")
print("File Created Successfully.....")
#2.Write in a File
f=open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\A.txt","w")
f.write("Abisekh Dey\n")
print("Data wrote in File Successfully.....")
f.close()
#3a.Read the File Content in The Terminal using read(bytes) method
f=open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\A.txt","r")
print(f.read(30))#Read method will print only data of the bytes we have mentioned in the read method which is here 30;if we don't mention the size then it will print total bytes of the of the data 
print("Data Read in File Successfully.....")
f.close()
#3b.Read the File Content in The Terminal using readline() method
f=open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\A.txt","r")
print(f.readline())#Readline method will print only a line from the file
f.close() 
print("Data Read in File Successfully.....")
#3c.Read the File Content in The Terminal using readlines() method
f=open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\A.txt","r")
file=f.readlines()#Read line method will print all lines from the file 
print("Data Read in File Successfully.....")
for i in file:
    print(i.strip())
    f.close()
#4.Read the File Content in The Terminal
f=open("names.txt",mode="r")
element=f.read()
print(element)
#5.Write in a File in append mode the inputs will be given by the used
f=open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\A.txt","a")
a=input("Enter The Name: ")
b=int(input("Enter The Roll Number: "))
c=input("Enter The Trade: ")
f.write(f"Name:{a}; Roll:{b}; Trade:{c}\n")
print("Data wrote in File Successfully.....")
f.close()
#6.Reading From a File which is not exist and handling the error
try:
    f=open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\B.txt","r")
    file=f.readlines()#Read line method will print all lines from the file 
    print(file)
except:
    print("File Not Found")
else:
    f.close()
    print("File Closed")
#7a.Create a new file and copy the data of an exsisting to the new file
try:
    with open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\A.txt","r") as f1:
        with open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\B.txt","w") as f2:
            for i in f1:
                f2.write(i)
except:
    print("File Not Found")
#7b.Create a new file and copy the data of an exsisting to the new file
try:
    f1= open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\A.txt","r")
    f2= open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\B.txt","w")
    for i in f1:
        f2.write(i)
except:
    print("File Not Found")
else:
    f1.close()
    print("File Closed")

#8.Delete An existing file
import os
if os.path.exists("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\B.txt"):
    os.remove("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\B.txt")
    print("File Deleted Successfully!")
else:
    print("File not Exist!")
#9.r+ mode in File
# Open a file named "example.txt" in read and write mode
with open('names.txt', 'r+') as file:
    # Read the content of the file
    content = file.readlines()
    print("Content of the file before writing:")
    print(content)
    
    # Move the file pointer to the beginning of the file
    file.seek(0)
    
    # Write something to the file
    file.write("This is a new line added using 'r+' mode.")
    
    # Move the file pointer to the beginning of the file
    file.seek(0)
    
    # Read the updated content of the file
    updated_content = file.read()
    print("\nContent of the file after writing:")
    print(updated_content)
#10.Update any number in the file using r+ method
with open('names.txt', 'r+') as file:
    # Read the content of the file
    content = file.read()
    print("Content of the file before writing:")
    print(content)
    print(id(content))
    content=int(content)
    print(id(content))
    file.seek(0)
    content=content+10
    print(id(content))
    content=str(content)
    print(id(content))

    file.write(content)
#11.
# Open a file in write mode ('w+')
file = open("names.txt", "w+")

# Write some content to the file
file.write("This is some content that we will truncate.")

# Print the initial size of the file
print("Initial size of file:", file.tell())

# Truncate the file to 20 bytes
file.truncate(20)

# Print the new size of the file
print("New size of file after truncation:", file.tell())

# Seek back to the beginning of the file to read its contents
file.seek(0)

# Read and print the contents of the file
print("Contents of the file after truncation:", file.read())

# Close the file
file.close()
#12.
# Open a file in write mode
file = open("names.txt", "w")

# Write some content to the file
file.write("Hello, World!\nThis is a test.")

# Close the file
file.close()

# Open the file in read mode
file = open("names.txt", "r")

# Read and print the content of the file
print("Contents of the file before seeking:")
print(file.read())

# Move the file pointer to the beginning of the file
file.seek(0)

# Read and print the content of the file again
print("\nContents of the file after seeking:")
print(file.read())

# Close the file
file.close()
#13. Delete a line in file
def delete_line(file_path, line_number):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove the line to be deleted
    if 0 < line_number <= len(lines):
        #len(lines): This expression returns the total number of lines in the file. lines is a list containing all the lines read from the file using file.readlines().
        #0 < line_number: This checks whether line_number is greater than 0. It ensures that line_number is a positive integer.
        #line_number <= len(lines): This checks whether line_number is less than or equal to the total number of lines in the file. It ensures that line_number does not exceed the total number of lines in the file.
        del lines[line_number - 1]
        #Using del lines[-1] to delete the last line directly from the list of lines:
        # This method deletes the last line directly from the list of lines read from the file.
        # Then, it writes back the modified list of lines to the file.

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)
        print(f"Line {line_number} deleted successfully.")
    else:
        print("Invalid line number.")

# Example usage
file_path = 'names.txt'  # Replace 'example.txt' with your file path
line_number_to_delete = 3  # Replace 3 with the line number you want to delete
delete_line(file_path, line_number_to_delete)
#14.Find the last line of the txt file
def get_last_line(file_path):
    with open(file_path, 'rb') as file:
        file.seek(-2, 2)  # Seek to the second last byte from the end of the file
        while file.read(1) != b'\n':
            file.seek(-2, 1)  # Move backwards one byte
        last_line = file.readline().decode().strip()
    return last_line

file_path = 'names.txt'  # Replace 'your_file.txt' with your file path
last_line = get_last_line(file_path)
print("Last line:", last_line)
#15.
def delete_last_line(file_path):
    with open(file_path, 'r+') as file:
        lines = file.readlines()
        file.seek(0)  # Move the cursor to the beginning of the file
        file.truncate()  # Clear the file content
        file.writelines(lines[:-1])  # Write all lines except the last one back to the file

file_path = 'names.txt'  # Replace 'your_file.txt' with your file path
delete_last_line(file_path)
#16.Use of Truncate method in file
f=open("names.txt","r+")
x=f.readlines()
f.seek(0)# Move the cursor to the beginning of the file
f.truncate()#Truncate is used to delete the txt file contents
f.writelines(x[:-1])
#Using f.truncate() followed by f.writelines(x[:-1]):
# This method first truncates the file, removing all its contents.
# Then, it writes back all the lines from the original content, excluding the last line, effectively deleting it.
#17a.
# Function to convert string to binary

def string_to_binary(string):
    binary = ''.join(format(ord(char), '08b') for char in string)
    print(len(binary))
    return binary

# Data to be stored
data = "17632322013"

# Convert data to binary
binary_data = string_to_binary(data)

# Open a file in binary write mode
with open("A.txt", "w") as f:
    # Write binary data to the file
    f.write(binary_data)

print("Binary data has been written to binary_data.txt file.")


# Sample string
original_string = "110001110111110110110011110010110011110010110010110000110001110011"

# Add a space after every 4 characters
modified_string = ' '.join(original_string[i:i+4] for i in range(0, len(original_string), 8))

print(modified_string)

#17b.
# Function to convert binary to string
def binary_to_string(binary):
    modified_string = ' '.join(binary[i:i+8] for i in range(0, len(binary), 8))
    binary_values = modified_string.split()
    string = ''.join(chr(int(char, 2)) for char in binary_values)
    return string

# Open the binary data file in read mode
with open("A.txt", "r") as f:
    # Read the binary data
    binary_data = f.read()

# Convert binary data back to string
decoded_data = binary_to_string(binary_data)
print(len(binary_data))
print("Decoded data:", decoded_data)



import Atm
x=Atm.Student()
x.set_name("abisekh")
print(x.get_name())


import Atm
Atm.Student.get_name("abisekh")
print(Atm.Student.get_name())


from Atm import ATM
ATM()

from Atm import ATM
x=ATM()

import Atm
Atm.ATM()

import Atm as a
a.ATM()

from datetime import datetime
print(datetime.now())
print(datetime.now().hour)