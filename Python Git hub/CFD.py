#Creation of self made Fraction Datatype because Python Don't any Fration Datatype
#Example of Fraction Datatype:- 2/3,5/2
#The Reason of Creation: if I want to create a list of [2/3,5/2];then it if I print the list then in the printed list we can not able to see the Original elements of the list which is [2/3,5/2]
#Python compiler automatic convert fraction into floating point value like 2/3 will be 0.6666666666666666 and 5/2 will be 2.5
#So the printed list will be [0.6666666666666666, 2.5];beacuse Python don't support fraction data type; to avoid this we can create a fraction datatype which will have an independent fraction class origin
#The datatype will be printed in fraction format and all the calculation will be done in fraction format and also the final result will be in fraction format 
# list=[2/3,5/2]
# print(list) #This will print this ->[0.6666666666666666, 2.5] not this->[2/3,5/2]

class Fraction:
    def __init__(self,n,d):
        self.__numerator=n
        self.__denominator=d
    def __str__(self): #__str__ is a magic function 
        return f"{self.__numerator}/{self.__denominator}"    
    def __add__(self,other):
        numerator=self.__numerator*other.__denominator+other.__numerator*self.__denominator
        denominator=self.__denominator*other.__denominator
        return f"{numerator}/{denominator}"
    def __sub__(self,other):
        numerator=self.__numerator*other.__denominator-other.__numerator*self.__denominator
        denominator=self.__denominator*other.__denominator
        return f"{numerator}/{denominator}"
    def __mul__(self,other):
        numerator=self.__numerator*other.__numerator
        denominator=self.__denominator*other.__denominator
        return f"{numerator}/{denominator}"
    def __truediv__(self,other):
        numerator=self.__numerator*other.__denominator
        denominator=self.__denominator*other.__numerator
        return f"{numerator}/{denominator}"
    
    
def add_record(name, roll_number):
    with open('names.txt', 'a') as file:
        file.write(f"Name: {name},Roll: {roll_number}\n")

# def display_records():
#     with open('names.txt', 'r') as file:
#         records = file.readlines()
#         found = False
#         for record in records:
#             record = record.strip()  # Remove leading/trailing whitespaces
#             name, roll_number = record.split(',')
#             if name.startswith("Name: "):  # Check if the record starts with "Name: "
#                 name = record[len("Name: "):(len("Name: ")+len("Abisekh"))]  # Remove "Name: " from the beginning
#                 roll_number=record[(len("Name: ")+len("Abisekh")+len(",Roll: ")):]
#             if name == 'Avi' and roll_number == '12':
#                 print("Grade A")
#                 found = True
#                 break
#         if not found:
#             print("No record found for Avi with roll number 12")
def display_records():
    with open('names.txt', 'r') as file:
        records = file.readlines()
        print(records)
        found = False
        for record in records:
            print(record)
            record = record.strip()  # Remove leading/trailing whitespaces
            if record.startswith("Name: "):  # Check if the record starts with "Name: "
                record = record[len("Name: "):]  # Remove "Name: " from the beginning
                name, roll_number = record.split(',Roll: ')
                print(name)
                print(roll_number)
                if name == 'Avi' and roll_number == '12':
                    print("Grade A")
                    found = True
                    break
        if not found:
            print("No record found for Avi with roll number 12")

def main():
    while True:
        print("1. Add a record")
        print("2. Display all records")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter a name: ")
            roll_number = input("Enter roll number: ")
            add_record(name, roll_number)
            print("Record added successfully.")
        elif choice == '2':
            print("List of records:")
            display_records()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()


x=[12,23,34,45,56]
for i in x:
    print(i)








def add_name(name):
    with open('names.txt', 'a') as file:
        file.write(name + '\n')

def display_names():
    with open('names.txt', 'r') as file:
        names = file.readlines()
        for name in names:
            print(name.strip())

def main():
    while True:
        print("1. Add a name")
        print("2. Display all names")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter a name: ")
            add_name(name)
            print("Name added successfully.")
        elif choice == '2':
            print("List of names:")
            display_names()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
    
    
