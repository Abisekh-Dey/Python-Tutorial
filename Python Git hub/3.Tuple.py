#1.Creating Tuple in Python
col=("Red","White","Green")
print(col,type(col),len(col),hash(col))#hash(col) This will print a hash value
x=(12)#(12): This is not interpreted as a tuple but as an integer surrounded by parentheses. It is equivalent to the integer 12 without any tuple structure. In other words, (12) is just the number 12 enclosed in parentheses and does not create a tuple.
print(x,type(x))
x=(12,)#(12,): This is interpreted as a tuple with a single element, and that element is the integer 12. The comma , is necessary to indicate that it's a tuple. In Python, a single-item tuple must have a trailing comma to differentiate it from a simple expression within parentheses.
print(x,type(x))
#2.Creating Tuple in Python
col=tuple(("Red","White","Green"))
print(col,type(col),len(col))
#3.Creating Tuple in Python with Different Datatypes
x=(18,3.45,"Abisekh Dey",[12,23,34,45,56],(1,2,3,4,5),{2,4,6,8,10})
print(x,type(x),len(x))
#4.Printing of Different Indexes in Tuple in Python with Different Datatypes
x=(18,3.45,"Abisekh Dey",[12,23,34,45,56],(1,2,3,4,5))
print(x,type(x),len(x))
print(x[0],x[1],x[2],x[3],x[4])
#5.Printing of Different Indexes in Tuple in Python with Different Datatypes using while loop
x=(18,3.45,"Abisekh Dey",[12,23,34,45,56],(1,2,3,4,5))
print(x,type(x),len(x))
i=0
while i<len(x):
    print(x[i])
    i+=1
#6a.Printing of Different Indexes in Tuple in Python with Different Datatypes using for loop
x=(18,3.45,"Abisekh Dey",[12,23,34,45,56],(1,2,3,4,5))
print(x,type(x),len(x))
for i in range(len(x)):#the loop iterates over indexes, and you use these indexes to access the elements like x[0] when i=0;x[1] when i=1;till i<len(x)
    print(f"{i+1}.Tuple[{i}] =",x[i])
    #print(f"{i+1}.Tuple[{i}] = {x[i]}")#This also Generate the same result
#6b.Printing of Different Indexes in Tuple in Python with Different Datatypes using for loop showing of index() function
x=(18,3.45,"Abisekh Dey",[12,23,34,45,56],(1,2,3,4,5))
print(x,type(x),len(x))
for i in x:#the loop iterates over elements directly without the need for explicit index access.
    print(f"Tuple[{x.index(i)}] =",i)#x.index(i) is used to find the index of the current element i within the tuple x. The index() method returns the first index at which a given element appears in the tuple.
#However, using x.index(i) inside the loop can lead to unexpected results if the tuple contains duplicate or same elements. It will always return the index of the first occurrence of the element, not necessarily the current one in the loop.
#6c.Printing of Different Indexes in Tuple in Python with Different Datatypes using for loop showing of enumerate() function
#The enumerate() function is a built-in Python function that is used to iterate over a sequence (such as a list, tuple, or string) while keeping track of the index of the current item. It returns pairs of index and element, making it convenient to work with both the index and the value in a loop.
#Format: enumerate(iterable, start=0)
x = (18, 3.45, "Abisekh Dey", [12, 23, 34, 45, 56], (1, 2, 3, 4, 5))
print(x, type(x), len(x))
for index, i in enumerate(x):
    print(f"{index+1}.Tuple[{index}] =", i)#Here index is the variable datatype is int
print(type(index))
#6d.
x = ("18", "Abisekh Dey")
x=list(x)#Converting in list because tuple doesn't support data assignment
for index,i in enumerate(x):
    if i.startswith("18"):
        x[index]="15"
print(x)
#7.Negetive indexing in Tuple using for loop
x = (18, 3.45, "Abisekh Dey", [12, 23, 34, 45, 56], (1, 2, 3, 4, 5))
for i in range(len(x)):
    print(f"{i+1}.Tuple[-{i+1}]:",x[-(i+1)])
#8.Negetive indexing in Tuple using while loop
x = (18, 3.45, "Abisekh Dey", [12, 23, 34, 45, 56], (1, 2, 3, 4, 5))
i=0
while i<len(x):
    print(f"{i+1}.Tuple[-{i+1}]:",x[-(i+1)])
    i+=1
#9a.Positive Range indexing in Tuple
x = (18, 3.45, "Abisekh Dey", [12, 23, 34, 45, 56], (1, 2, 3, 4, 5))
print(x[2:5])
#9b.Negetive Range indexing in Tuple
x = (18, 3.45, "Abisekh Dey", [12, 23, 34, 45, 56], (1, 2, 3, 4, 5))
print(x[-5:-1])
#10a.Check any Specified Element is present in Tuple
x = (18, 3.45, "Abisekh Dey", [12, 23, 34, 45, 56], (1, 2, 3, 4, 5),{"Red","Black","Blue"})
print(x)
found=False
dtype=input("Enter Datatype of Search Element: ")
if dtype=="int":
    y=int(input("Enter The Element you Want to find: "))
    if y in x:
        found=True
elif dtype=="float":
    y=float(input("Enter The Element you Want to find: "))
    if y in x:
        found=True
elif dtype=="str":
    y=input("Enter The Element you Want to find: ")
    if y in x:
        found=True
elif dtype=="list":
    # y=list(int(input(f"Enter The Element you Want to find of list[{i}]: ")) for i in range(5))
    y=[]
    i=0
    while i<5:
        ele=int(input(f"Enter The Element you Want to find of list[{i}]: "))
        y.append(ele)
        i+=1
    # i=0
    # while i<len(x[3]):
    #     if y[i]==x[3][i]:
    #         found=True
    #     i+=1
    for i in range(len(x[3])):
        if y[i]==x[3][i]:
            found=True
elif dtype=="tuple":
    y=tuple(int(input(f"Enter The Element you Want to find of Tuple[{i}]: ")) for i in range(5))
    i=0
    while i<len(x[4]):
        if y[i]==x[4][i]:
            found=True
        i+=1
elif dtype=="set":
    y={input(f"Enter The Element you Want to find of Set[{i}]: ") for i in range(3)}
if y in x:
    found=True
if found is True:
    print(y,"is Present in Tuple!")
else:
    print(y,"is Not Present in Tuple!")

#10b.Check any Specified Element is present in Tuple
x = (12, 23, 34, 45, 56)
y=int(input("Enter The Element you Want to find: "))
found=False
if y in x:
        found=True
if found is True:
    print(y,"is Present in Touple!")
else:
    print(y,"is Not Present in Tuple!")

#11a.Concatination in Tuple
x=(12,23,34)
y=(45,56)
x=x+y
print(x)
#11b.Concatination in Tuple
x=()
y=(45,56)
x=x+y
print(x)
#11c.Concatination in Tuple
x=(12,23,34)
y=tuple()
x=x+y
print(x)
#11d.Concatination in Tuple
x=(12,23,34)
y=(45,56)
x=x+(y,)
print(x)
#11e.Concatination in Tuple
x=()
y=(45,56)
x=x+(y,)
print(x)
#11f.Concatination in Tuple
x=(12,23,34)
y=(45,56)
z=[1,2,3]
a=tuple(z)
x=x+(y,)+a
print(x)
#11g.Concatination in Tuple
x=(12,23,34)
y=(45,56)
z=[1,2,3]
x=x+(y,)+(z,)
print(x,type(z))
#12.Find Sum of all numbers in tuple using sum function
x=(1,2,3,4,5,6,7,8,9,10)
print("Sum is:",sum(x))
#12a.Addition of Tuple Elements using for loop:
x=(1,2,3,4,5,6,7,8,9,10)
sum=0
for i in x:
    sum+=i
print("Sum of Elements of Tuple will be:",sum)
#13.Addition of Tuple Elements using for loop:
x=(1,2,3,4,5,6,7,8,9,10)
i=0
sum=0
while i<len(x):
    sum+=x[i]
    i+=1
print("Sum of Elements of Tuple will be:",sum)
#14a.Implimentation of User Defined Tuple
n=int(input("Enter The Size of The Tuple: "))
num=()
print(id(num))
for i in range(n):
    x=int(input("Enter The Element: "))
    num=num+(x,)
    print(id(num))
print(id(num))
print("The Elements of The Tuple:",num)
#14b.Implimentation of User Defined Tuple
n=int(input("Enter The Size of The Tuple: "))
num=tuple(int(input(f"{i+1}.Enter The Element[{i}]: ")) for i in range(n))
print("The Elements of The Tuple:",num)
#14c.Implimentation of User Defined Tuple
n=int(input("Enter The Size of The Tuple: "))
num=()
i=0
while i<n:
    x=int(input("Enter The Element: "))
    num=num+(x,)
    i+=1
print("The Elements of The Tuple:",num)
#14d.Implimentation of User Defined Tuple
n=int(input("Enter The Size of The Tuple: "))
num=tuple()# writing only this () or tuple() both Represents empty tuple in python
i=0
while i<n:
    x=int(input("Enter The Element: "))
    num=num+(x,)
    i+=1
print("The Elements of The Tuple:",num)
#14e.Implimentation of User Defined Tuple
n=int(input("Enter The Size of The Tuple: "))
num=()
i=0
while i<n:
    x=int(input("Enter The Element: "))
    num=num+(x,)
    i+=1
a=tuple(int(input(f"{i+1}.Enter The Element of Tuple[{i}]: "))for i in range(n))
num=num+(a,)
b=[int(input(f"Enter The Element of List[{i}]: "))for i in range(n)]
num=num+(b,)
c={int(input(f"Enter The Element of set[{i}]: "))for i in range(n)}
num=num+(c,)
print("The Elements of The Tuple:",num)
#15.Unpacking Tuple
col=("Red","Green","White")
col1,col2,col3=col
print(col)
print(col1,col2,col3)
#16.Tuple Reversal
n=int(input("Enter The Size Of The Tuple: "))
x=tuple(int(input(f"{i+1}.Enter The Element of Tuple[{i}]: ")) for i in range(n))
print(f"Tuple is: {x}")# or i can write print("Tuple is:",x) both are correct
a=[i for i in reversed(x)]#Creating List to store elements of tuple in Reversed Order because we can't Reverse elements of tuple directly because the elements are fixed/unchangeable of each index in tuple 
print("List is:",a)
new_tuple=tuple(a)
print("New Tuple is:",new_tuple)
for i in range(n):
    print(f"{i+1}.New Tuple[{i}]:",new_tuple[i])




x=(12,23,34,45,56)
y=(56,67,78)
z=(56,89)
a=(56,)
for i in x:
    for j in y:
        for k in z:
            for l in a:
                if i==j==k==l:
                    print("Common Element Found!\nElement is:",i)
x=(12,23,34,45,56)
y=(56,67,78)
for i in x:
    for j in y:
        if i==j:
            print("Common Element Found!\nElement is:",i)
#17.
import random
x=(1234,4567,6789)
y=random.choice(x)
print(y)
#18.
import random
x=[1234,4567,6789]
y=random.choice(x)
print(y)
#19a.
import random
x="abcdefghijklmnopqrstwxyz"
y=random.choice(x)
print(y)
#19b.Selecting random 6 alphabets from the given alphabets
import random
x="abcdefghijklmnopqrstwxyz"
y="".join(random.choice(x) for i in range(6))
print(y)
#20.
x=(1,2)
y=(3,4)
x=x+y
print(x)
