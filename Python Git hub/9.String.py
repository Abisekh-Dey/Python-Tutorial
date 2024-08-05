#String is not Mutable
#1.
x='Abisekh'
y="Abisekh"
z='''Abisekh'''
print(x,len(x),type(x))
print(y,len(y),type(y))
print(z,len(z),type(z))
#2.Concatination
x='Abisekh'
y=" "
z='''Dey'''
print(x+y+z)
#3.
x="Abisekh Dey"
print(x[2:7])
print(x[1:])
print(x[:8])
print(x[0:8:2])#First 2 are slicing indexes and last one is for count
#4.
x='Abisekh Dey'
print(x[-10:-1])
print(x[-11:])
print(x[:-1])
print(x[-11:-1:2])
print(x[::-1])
#5.
x="abisekh dey"
y=x.upper()#upper function returns a new string we can't directly update any string because strings are not mutable so once we create a string we can't change the string
print(y)
#6.
x="ABISEKH DEY"
y=x.lower()
print(y)
#7.
x="abisekh dey"
y=x.capitalize()
print(y) 
#8.
x="Abisekh"
y="Dey"
z=" ".join(y)
print(z)
#9.Use of find function
#Format: string.find("Character/string/word to be found")
x="Abisekh Dey"
print(x.find("e"))
print(x.find("ise"))
print(x.find(" "))
print(x.find("Dey"))
#10.Use of strip function to remove trailing whitespace part of any string
x="     Abisekh Dey     "
print(x)#printing string with trailing whitespace characters
print(x.strip())#printing string with out trailing whitespace characters
#11a.Use of replace function
#Format: string.replace("old string","new string",count/times)
x="Abisekh Dey"
y=x.replace("Abisekh","Pallabi")
print(y)
#11b.Use of replace function
x="Abisekh Dey"
y=x.replace("e","j")#Here "e" is replaced by "j" in every cases by default; because I didn't mentioned how many times it should be replaced from the starting of the string
print(y)
#11c.Use of replace function
x="Abisekh Dey"
y=x.replace("e","j",1)#Here "e" is replaced by "j" but only once because here I mentioned "e" should be replaced by "j" only 1 time from the starting
print(y)
#11.d Use of replace function
x=input("Enter The Paragraph: ")
y=input("Enetr The Word to Replace: ")
z=input("Enter The New word: ")
a=x.replace(y,z,3)#for first 3 occurences the character /the sub string will be replaced  
print(a)
#12a.Use of split Function
#Format: string.split("Separator",Maxsplit) by default the separator is space; and maxsplit denotes how many split I require each of the separation will be done when it gets the space by default; if I don't mentioned maxsplit it will take all spaces a separator and split them and make a list of string accordingly
x="I live in India"
y=x.split()
print(y)
#12b.Use of split Function
x="I-live-in-India"
y=x.split("-",2)#Here the separator is "-" and Maxsplit is 2; after 2 spliting the rest part will be an individual string
print(y)
#12c.Use of split Function
x="I;Abisekh Dey"
y=x.split(";")
z="I-am-an Engineer"
a=z.split("-")
print(y+a)
y.append(a)
print(y)
#12d.Use of split Function
y="Name: Abisekh Dey;Roll: 12"
print(id(y))
y=y[len("Name: "):]
print(y,"id",id(y))
y=y.split(";Roll: ")
print(y,"id",id(y))
#12d.Use of split Function
y="Name: Abisekh Dey;Roll: 12"
print(id(y))
y=y[len("Name: "):]
print(y,"id",id(y))
a,y=y.split(";Roll: ")
print(a,y,"id",id(y))
#13a.Use of format function
name=input("Enter The Name: ")
marks=int(input("Enter The Mark: "))
s="The Student Name is {} and mark is {}".format(name,marks)
print(s)
#13b.Use of format function
name=input("Enter The Name: ")
marks=int(input("Enter The Mark: "))
s="The Student Name is {n} and mark is {m}".format(n=name,m=marks)
print(s)
#13c.Use of format function
name=input("Enter The Name: ")
marks=int(input("Enter The Mark: "))
print(f"The Student is {name} and marks is {marks}")
#14.
#Concider a string: "The Unexpected Always Happens"
#1.Assign the string to a variable
#2.Print the strin g
#3.Print The length of the string
#4.Check if pp Phrase is present or not in the string
#5.Print Subtracting from 0 to 10 index
#6.Replace "Always" with "Never"
#7.Add "No Matter What in The String"
#8.Print The Final String
x="The Unexpected Always Happens "
print(x)
print(len(x))
print(x.find("pp"))
print(x[0:11])
print(x.replace("Always","Never"))
y="No Matter What in The String" 
print(x+y)
#15a.Write a Python code to check a string is pallindrome or not
def pal(x):
    y=(x.replace(" ","")).lower()#First Replacing the White space character(" ") with nothing(""; then making the whole string in lower case 
    reverse_y=y[::-1]
    if y==reverse_y:
        print(f"The String:- {x} is Pallindrome")
    else:
        print(f"The String:- {x} is not Pallindrome")
a=input("Enter The String: ")
pal(a)
#15b.Write a Python code to check a string is pallindrome or not
def pal(x):
    y=(x.replace(" ","")).lower()#First Replacing the White space character(" ") with nothing(""; then making the whole string in lower case 
    reverse_y=y[::-1]
    if y==reverse_y:
        return "Pallindrome"
    else:
        return "not Pallindrome"
a=input("Enter The String: ")
print(f"{a} is:",pal(a))
#15c.Write a Python code to check a string is pallindrome or not
def pal(x):
    y=(x.replace(" ","")).lower()#First Replacing the White space character(" ") with nothing(""; then making the whole string in lower case 
    reverse_y=y[::-1]
    return y==reverse_y#It will return true or false to the function call
a=input("Enter The String: ")
if pal(a):
    print(f"The String:- {a} is Pallindrome")
else:
    print(f"The String:- {a} is not Pallindrome")
#16.Predict Output
print("Hello {name} Surname {sname}".format(name='Abisekh',sname='''Dey'''))
#17.Predict Output
x="6/2"
print("x")
#18.Predict Output
x="10/5"#Here 10/5 is a string not integers; so we can't do any arithmetic operation here 
print(x)
#19.Predict Output
x=10/5
print(x)
#20.Predict Output
x="Information"
print(x[2:8])
#21.Predict Output
x="Application"
y=x.replace("a","A")
print(y)
#22.Predict Output
x="poWer"
x.upper()#upper function returns a new string we can't directly update any string because strings are not mutable so once we create a string we can't change the string 
#here I updated the string by changing the case of the string but I didn't re-assigned the updated string to a new variable
print(x)
#23.Predict Output
x="poWer"
print(id(x))#id Function is used to check the memory address; here it will print initial memory address of x
x=x.upper()#Re-assigning Uppercase string in x
print(id(x))#it will print the address of x after assignment the value in x; so both will be different so both x are different
print(x)
#24.Use of isdigit() function in string; this function returns true or false
x="123"
print(x.isdigit())
x="1.5"
print(x.isdigit())
x="Avi"
print(x.isdigit())
#25.Use of isalpha() function in string; this function returns true or false
x="123"
print(x.isalpha())
x="Avi"
print(x.isalpha())
#26.Use of isupper() function in string; this function returns true or false
x="A"
print(x.isupper())
#27.Use of isdecimal() function in string; this function returns true or false
x="123"
print(x.isdecimal())# x has no floating point number
x="123.67"
print(x.isdecimal())
#28.Use of isascii() function in string; this function returns true or false
x="97"
print(x.isascii())
x="997"
print(x.isascii())
x="+"
print(x.isascii())
x="abc"
print(x.isascii())
#29.Use of islowert() function in string; this function returns true or false
x="a"
print(x.islower())
#30.Use of isspace() function in string; this function returns true or false
x=" "
print(x.isspace())
#31.Use of isnumeric() function in string; this function returns true or false
x="1"
print(x.isnumeric())
x = "12345"
y = "١٢٣٤٥"  # Arabic numerals
z = "½"       # Fraction character

print(x.isdigit())   # Output: True
print(y.isdigit())   # Output: True
print(z.isdigit())   # Output: False

print(x.isnumeric()) # Output: True
print(y.isnumeric()) # Output: True
print(z.isnumeric()) # Output: True
#32.Use of isalnum() function in string; this function returns true or false
x = "abc123"
print(x.isalnum())  # Output: True
y = "abc123!"
print(y.isalnum())  # Output: False
#33.
x="Abisekh"
if x.startswith("A") or x.startswith("a"):
    print("Hello")
#34.
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.printable)
print(string.punctuation)
print(string.whitespace)
#31.
x="12+("
a=["+","-","*","/"]
f=x.find("(")
if x[f-1] in a:
    print(x[f-1])
#VVVVVI
#32a. Pallindrome or not
x=input("Enter The String: ")
x = x.lower()
if len(x)%2!=0:
    y=len(x)//2
    a,b=x.split(x[y])
    b=b[::-1]
    if a==b:
        flag=True
    else:
        flag=False
else:
    y=len(x)//2
    a=x[0:y]
    b=x[y:]
    b=b[::-1]
    if a==b:
        flag=True
    else:
        flag=False
if flag:
    print("Pallindrome")
else:
    print("Not-Pallindrome")
#32b.  
x = input("Enter The String: ")
x = x.lower()  # Convert to lowercase to handle case-insensitive palindrome checks

if x == x[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
#33. Create a code where user will enter an alphabet but he can see the very next alphabet from the alphabet he entered
import string
l1=string.ascii_lowercase
l=input("Enter Any Alphabet: ")
l=l.lower()
for i in range(len(l1)):
    if l1[i]==l:
        print(f"You have entered: {l1[i+1]}")
        break
    elif l=="z":
        l=l1[0]
        print(f"You have entered: {l}")
        break
else:
    print("Invalid input. Please enter a valid alphabet.")
#34. Create a code where user will enter an alphabet but he can see the very next alphabet from the alphabet he entered
l=[chr(i) for i in range(97,123)]
# for i in range(97,123):
#     l.append(chr(i).lower())
a=input("Enter Any Alphabet: ")
for i in range(len(l)):
    if l[i]==a:
        print(f"You have entered: {l[i+1]}")
        break
    elif a=="z":
        a=l[0]
        print(f"You have entered: {a}")
        break
else:
    print("Invalid input. Please enter a valid alphabet.")
#35. Create a code where user will enter an alphabet but he can see the very next alphabet from the alphabet he entered
a=input("Enter Any Alphabet: ")
if a.isalpha()==True and len(a)==1:
    a=a.lower()
    if a=="z":
        a="a"
    else:
        a=chr(ord(a)+1)
print(f"You have entered: {a}")