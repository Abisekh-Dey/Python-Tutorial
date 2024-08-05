import sys
import os
def department():
    department=input("Enter The Department: ")
    dep=department.upper()
    if dep=="ECE":
        dep="ELECTRONICS AND COMMUNICATION ENGINEERING"
    if dep=="CSE":
        dep="COMPUTER SCIENCE AND ENGINEERING"
    if dep!="ELECTRONICS AND COMMUNICATION ENGINEERING" and dep!="COMPUTER SCIENCE AND ENGINEERING":
        for i in range(3):
            os.system("cls")
            department=input("Re-Enter The Department: ")
            dep=department.upper()
            if dep=="ECE":
                dep="ELECTRONICS AND COMMUNICATION ENGINEERING"
            if dep=="CSE":
                dep="COMPUTER SCIENCE AND ENGINEERING"
            if dep=="ELECTRONICS AND COMMUNICATION ENGINEERING" or dep=="COMPUTER SCIENCE AND ENGINEERING":
                break
            else:
                if dep!="ELECTRONICS AND COMMUNICATION ENGINEERING" and dep!="COMPUTER SCIENCE AND ENGINEERING" and i==2:
                    print("Invalid Department!")
                    sys.exit()

def sem():
    semester=int(input("Enter Semester: "))
    if semester!=3 and semester!=4:
        for i in range(3):
            os.system("cls")
            semester=int(input("Re-Enter Semester: "))
            if semester==3 or semester==4:
                break
            else:
                if semester!=3 and semester!=4 and i==2:
                    print("Invalid Semester!")
                    sys.exit()            
department()
sem()