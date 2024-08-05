#1a.Printing of List in Python
num=[12,23,34,45,56]
print(num)
print(type(num))
print(len(num))#Prints size of the list
print(hash(num))#Lists are not Hashable Thats why it will generate error
#Lists in Python are mutable, meaning their contents can be changed after creation. Mutable objects, like lists, don't have a fixed hash value because their content can change over time. As a result, lists are not hashable or unhashable.
#2b.Printing of List in Python
num=list((12,23,34,45,56))
print(num)
print(type(num))
print(len(num))#Prints size of the list
x=[1]
print(x,type(x))
#3.Printing of List in Python which contains different datatypes
num=[12,2.3,"a","Abisekh Dey",[1,2,3,4,5,6,7,8,9,10]]
print(num)
print(type(num))
print("Size of the List is:",len(num))#Prints size of the list
print(num[0])
print(num[4])
#4a.Search Any Element in The List using in and not in function in Python
num=[12,2.3,"a","Abisekh Dey",[1,2,3,4,5,6,7,8,9,10]]
if "Abisekh Dey" in num:
    print("Abisekh Dey string is Present in Num List!")
else:
    print("Abisekh Dey string is Absent in Num List!")
if "B" not in num:
    print("B is Absent in the Num List!")
else:
    print("B is Present in the Num List!")
#4b.Search Any Element in The List using in and not in function in Python
x=[12,2.3,"Abisekh Dey",[1,2,3,4,5],(12,23,34,45,56),{"Red","Green","White"}]
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
    # for i in range(len(x)):
    if y in x:
        found=True
    print(type(y))
elif dtype=="tuple":
    y=tuple(int(input(f"Enter The Element you Want to find of Tuple[{i}]: ")) for i in range(5))
    # i=0
    # while i<len(x[4]):
    #     if y[i]==x[4][i]:
    #         found=True
    #     i+=1
    # while i<len(x):
    if y in x:
        found=True
    print(type(y))
        # i+=1
elif dtype=="set":
    y=set((input(f"Enter The Element you Want to find of Tuple[{i}]: ")) for i in range(3))
    if y in x:
        found=True
    print(type(y))
    # i=0
    # while i<len(x[5]):
    #     if y[i]==x[5][i]:
    #         found=True
    #     i+=1
if found is True:
    print(y,"is Present in List!")
else:
    print(y,"is Not Present in List!")
#4c.Search Any Element in The List using in and not in function in Python
x=[12,23,34,45,56]
y=int(input("Enter The Element You Want to find "))
if y in x:
    print(y,"is Present in The List!")
else:
    print(y,"is not Present in The List!")
#5.Printing of List in Python using for loop
num=[12,2.3,"a","Abisekh Dey",[1,2,3,4,5,6,7,8,9,10]]
for i in range(5):
    print(f"{i+1}.List[{i}] =",num[i])
#6.Printing of List in Negetive Indexing in Python using for loop
num=[12,2.3,"a","Abisekh Dey",[1,2,3,4,5,6,7,8,9,10]]
for i in range(len(num)):
    print(f"{i}.List[-{i+1}] =",num[-(i+1)])
#7.Printing of List in Python using while loop
num=[12,2.3,"a","Abisekh Dey",[1,2,3,4,5,6,7,8,9,10]]
i=0
while i<len(num):
    print(f"{i+1}.List[-{i}] =",num[-i])
    i+=1
#8.Printing of List in Negetive Indexing in Python using While loop
num = [12, 2.3, "a", "Abisekh Dey", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
i = 0
while i < len(num):
    print(f"{i+1}.List[{-(i+1)}] =", num[-(i+1)])
    i += 1
print(num[-2])
print(num[-5])
#9.Print from 1 position upto 3 position elements of the list (List length should be > 4)
num = [12, 2.3, "a", "Abisekh Dey", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print(num[1:4])# Starting Position is inclussive but Ending Position is exclussive; 
#if i want to print from 1 position upto 3 position elements of the list then I have to set the starting position to 1 and ending position >3
#Format is num[starting:ending] 
#10.Print from 1 position upto 3 position elements of the list (List length should be > 4) using Negetive Indexing
num = [12, 2.3, "a", "Abisekh Dey", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print(num[-4:-1])# Starting Position is inclussive but Ending Position is exclussive; 
#if i want to print from 1 position upto 3 position elements of the list then I have to set the starting position to -4 and ending position >-2 because negetive indexing starts from right hand side and starts from -1 and moves to the left accordingly
#Format is num[starting:ending] 
#11.Use of append() function in the list
#it adds element at the last position of the list
#Format: list.append(element)
num = [12, 2.3, "a", "Abisekh Dey", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
num.append(["A",2,3,"B","Z"])# Only we can pass 1 argument; a . is necessary to use before append function
print(num)
#12.Use of insert() function in the list
#it adds element at the any position of the list
#Format: list.insert(position,element)
num = [12, 2.3, "a", "Abisekh Dey", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
num.insert(3,["A",2,3,"B","Z"])# Only we can pass 2 arguments; a . is necessary to use before insert function
print(num)
num.insert(4,50)
print(num)
#13.Use of extend() function in the list
#It extends a list with another list
#Format: list1.extend(list2)
num = [12, 2.3, "a", "Abisekh Dey", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
digit = [0,1,0,1,0]
num.extend(digit)#a . is necessary to use before extend function
print(num)
digit.extend(num)
print(digit)
#14.Use of remove() function in the list
#It removes a specific element from the list but we only need to mention the element in remove function and don't need to mention the index
#Format: list.remove(element)
num = [12, 2.3, "a", "Abisekh Dey", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print("Initial Length of the list is:",len(num))
print(num)
num.remove("a")#a . is necessary to use before remove function
print(num)
print("After removing an element from the list the size decreases to",len(num))
#15.Use of pop() function in the list
#It removes a specific element from the list when we mention the index of the specific element but we only need to mention the index in pop function and don't need to mention the element
#If we don't mention the index in the pop function then the last element of the list will be deleted automatically
#Format: list.pop(element)
num = [12, 2.3, "a", "Abisekh Dey", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print("Initial Length of the list is:",len(num))
print(num)
x=num.pop(2)#a . is necessary to use before pop function
print(num)
print(x)#Thiss will print the deleted item
print("After removing an element from the list the size decreases to",len(num))
num.pop()#a . is necessary to use before pop function
print(num)
print("After removing an element from the list the size decreases to",len(num))
#16.Change of Elements in the List
num = [12, 2.3, "a", "Abisekh Dey", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print("Unchanged List:",num,"Length:",len(num))
num[0]=16 #Method 1 of changing; Changing of a perticular element of a perticular index 
num[1]=3.4 #Method 1 of changing;Changing of a perticular element of a perticular index 
num[2:5]=["Pallabi Mondal",[12,23,34,45,56]] # Method 2 of changing; Changing in a range of elements
#Format: list[starting:ending] where starting is inclussive and ending is exclussive
#Here i mentioned the range [2:5] where it will start from 2 index and will end before 5 index; in between 2 to <5 there are 3 indexes present that are 2,3,4 index
#But I changed only 2 elemnent; this is a correct method but the Length of the list will be decreased
print("Updated list:",num,"Length:",len(num))
#17a.Sorting of List in Assending Order using sort function
number = [23,34,56,45,12,78,89,67,56]
number.sort()
print(number)
#97b.Sorting of List in Assending Order using sort function
alpha=["apple","awesome","ambition","absence","assuming"] # It will sort According to alphabet order
alpha.sort() #.sort()==.sort(reverse=False) both are correct
#sort() is an inbuilt function to sort a list in assending order because boolian type parameter reverse is set to False in sort function;a . is necessary to use before sort function
#Thats why we need to set the reverse parameter reverse=True if we want to sort a list in descending order
print(alpha)
#18a.Sorting of List in Descending Order using sort function
number = [23,34,56,45,12,78,89,67,56]
number.sort(reverse=True)#reverse is a boolian datatype it returns either True or False
print(number)
#18b.Sorting of List in Descending Order using sort function
number = [4,7,9,5,3,2,6,8,0,1]
number.sort()
print(number)
number.sort(reverse=True)#reverse is a boolian datatype it returns either True or False
print(number)
number.sort(reverse=False)
print(number)
#19a.Create a list and put some random numbers if any number of that list is divisible by 5 move that numbers to the another list 
num=[12,15,115,50,32,35,60,6,65,70.05]
new_num=[num for num in num if num%5==0]
print(new_num)
#99b.Create a list and put some random numbers if any number of that list is divisible by 5 move that numbers to the another list 
num=[12,15,115,50,32,35,60,6,65,70.05]
new_num=[i for i in num if i%5==0]
print(new_num) 
#19c.Create a list and put some random numbers if any number of that list is divisible by 5 move that numbers to the another list using for loop
num=[12,15,115,50,32,35,60,6,65,70.05]
new_num=[]
for i in num:
    if i%5==0:#The variable i takes the value of each element in the list num in each iteration of the loop. So, in this case, i represents the value of an element in the list, and i % 5 == 0 checks if that value is divisible by 5.
        #he for loop abstracts away the need for an explicit index, so you work directly with the values in the list.
        new_num.append(i)
print(new_num) 
#19d.Create a list and put some random numbers if any number of that list is divisible by 5 move that numbers to the another list using while loop
num=[12,15,115,50,32,35,60,6,65,70.05]
new_num=list()# or i can write [] only this
i=0
while i<len(num):
    if num[i]%5==0:#We are manually iterating through the indices of the list using the index variable i. Here, num[i] represents the value of the element at index i in the list num. So, again, num[i] % 5 == 0 checks if the value of the element at that index is divisible by 5.
        #The use of num[i] in the while loop is necessary because you are explicitly working with indices or we have to cntrol while loop dynamically in python
        new_num.append(num[i])
    i+=1
print(new_num) 
#20.Copy 1 list to another list using copy() function
num=[12,15,115,50,32,35,60,6,65,70.05]
new_num=num.copy()#a . is necessary to use before copy function
print(new_num)
new_num=num+new_num # + is added to concatinate to lists
print(new_num)
#21.Printing The Elements of a Sub-list inside list using for loop
num=[1,2,[12,23,34,45,56],50,57]
print(num[2][0])
print(num[2][1])
print(num[2][2])
print(num[2][3])
print(num[2][4])
for i in num[2]:
    print(i,end=" ")
#22.Printing The Elements of a Sub-list inside list using while loop
num=[1,2,[12,23,34,45,56],50,57]
i=0
while i<len(num[2]):
    print(num[2][i],end=" ")
    i+=1
#23a.Swapping of Elements of given Indexes of list [index 1 and index 3]
num=[12,23,34,45,56]
temp=num[1]
num[1]=num[3]
num[3]=temp
print(num)
#23b.Swapping of Elements of given Indexes of list [index 0 and index 4]
num=[12,23,34,45,56]
temp=num[0]
num[0]=num[4]
num[4]=temp
print(num)
#24a.Implimentation of User Defined List
n=int(input("Enter The Size of The List: "))
num=[]
for i in range(n):
    x=int(input(f"{i+1}.Enter Element[{i}]: "))
    num.append(x)# Here in every  iteration the value of x is changed and added to the list accordingly
print("Elements of The List Are:",num)
#24b.Implimentation of User Defined List
n = int(input("Enter The Size of The List: "))
num = [int(input(f"{i + 1}. Enter Element[{i}]: ")) for i in range(n)]#[]represents list
print("Elements of The List Are:", num)
#24c.Implimentation of User Defined List
n = int(input("Enter The Size of The List: "))
num = list(int(input(f"{i + 1}. Enter Element[{i}]: ")) for i in range(n))
print("Elements of The List Are:", num)
#24d.Implimentation of User Defined List
n=int(input("Enter The Size of The List: "))
num=list()# Writing [] only also means list in python both writing [] and list() both represents empty set in python
i=0
while i<n:
    x=int(input(f"{i+1}.Enter Element[{i}]: "))
    num.append(x)# Here in every  iteration the value of x is changed and added to the list accordingly
    i+=1
print("Elements of The List Are:",num)
#24e.Implimentation of User Defined List
n=int(input("Enter The Size of The List: "))
num=[]
for i in range(n):
    a=(input(f"{i+1}.Enter Element-1[{i}]: "))
    x=int(input(f"{i+1}.Enter Element-2[{i}]: "))
    num.append((a,x))# Here in every iteration the value of a & x is changed and added to the list as a tuple of (a,x) accordingly
print("Elements of The List Are:",num)

#25.Swapping of Elements of user defined Indexes of list in a user defined list
n=int(input("Enter The Size of The List: "))
num=[]
for i in range(n):
    x=int(input(f"{i+1}.Enter Element[{i}]: "))
    num.append(x)
print("Elements of The List Are:",num)
index1=int(input("Enter the First Index: "))
index2=int(input("Enter the Second Index: "))
temp=num[index1]
num[index1]=num[index2]
num[index2]=temp
print("Swapped List is:",num)
#26.List Reversal in Python using While loop
n=int(input("Enter The Size of The List: "))
num=[]
for i in range(n):
    x=int(input(f"{i+1}.Enter Element[{i}]: "))
    num.append(x)
print("Elements of The List Are:",num)
i=0
while i<n//2:
    temp=num[i]
    num[i]=num[n-i-1]
    num[n-i-1]=temp
    i+=1
print("Swapped List is",num)
#27.List Reversal in Python using For loop
n=int(input("Enter The Size of The List: "))
num=[]
for i in range(n):
    x=int(input(f"{i+1}.Enter Element[{i}]: "))
    num.append(x)
print("Elements of The List Are:",num)
for i in range(n//2):
    temp=num[i]
    num[i]=num[n-i-1]
    num[n-i-1]=temp
print("Swapped List is",num)
#28a.Generationof Character List From User Defined Size Using For Loop
n=int(input("Enter The Size of The List: "))
char=[]
for i in range(ord("A"),ord("A")+n):
    char.append(chr(i))
print(char)
#28b.Generationof Character List From User Defined Size Using while Loop
n=int(input("Enter The Size of The List: "))
char=[]
i=ord("A")
while i<ord("A")+n:
    char.append(chr(i))
    i+=1
print(char)
#28c.Generationof Character List From User Defined Size USing For loop
n=int(input("Enter The Size of The List: "))
char=[chr(i) for i in range(ord("A"),ord("A")+n)]#List Comprehension
print(char)
#28d.Generationof Character List From User Defined Size using while loop(In List Comprehension use for loop but Avoid using while loop)
#In Python, list comprehensions are designed to work well with for loops, but using a while loop in a single line is not as straightforward due to the structure of list comprehensions. The syntax for a list comprehension expects an expression followed by a for loop, but a while loop doesn't fit into this syntax directly.
from itertools import count, takewhile
n = int(input("Enter The Size of The List: "))
char = list(map(lambda i: chr(i), takewhile(lambda i: i < ord("A") + n, count(ord("A")))))
print(char)
#29a.Finding common Element in 4 lists using for loop
x=[12,23,34,45,56]
y=[56,67,78]
z=[56,89]
a=[56]
for i in x:
    for j in y:
        for k in z:
            for l in a:
                if i==j==k==l:
                    print("Common Element Found!\nElement is:",i)
#29b.Finding common Element in 2 lists using while loop
x=[12,23,34,45,56]
y=[56,67,78]
i=0
while i<len(x):
    j=0
    while j<len(y):
        if x[i]==y[j]:
            print("Common Element Found!\nElement is:",x[i])
        j+=1
    i+=1
#30.Create a list inside of the list
x=[1,2,3]
z=[]
n=int(input("enter The size of The Sub List: "))
for i in range(n):
    a=[int(input(f"{i+1}.Enter The Value of Sublist[{i}]: "))for i in range(n)]
    z.append(a)
    print(z)
    x.append(z)
    print(x)
print(x,len(x))#in the x list first it will update the z list with the upcoming element in the list z list which is previously there in the list x; then the total updated z list will be added in the x list again
#30a.Create a list inside of the list
x=[1,2,3]
z=[]
n=int(input("enter The size of The Sub List: "))
for i in range(n):
    a=[int(input(f"{i+1}.Enter The Value of Sublist[{i}]: "))for i in range(n)]
    z.append(a)
x.append(z)#it will directly add the updated z list in to the x list
print(x,len(x))
#30b.Create a list inside of the list
x=[1,2,3]
z=[]
n=int(input("enter The size of The Sub List: "))
for i in range(n):
    a=[int(input(f"{i+1}.Enter The Value of Sublist[{i}]: "))for i in range(n)]
z.append(a)#due to z list is outside of the for loop then the z will be added with the elements of a list but for the last iteration of for loop only
#if the for loop runs more than one time then the elements of list a for only the last iteration will be added in z list; elements of a list for the previous iterations will not be added
x.append(z)
print(x,len(x))
#30d.Create a list inside of the list
x=[1,2,3]
z=[]
n=int(input("enter The size of The Sub List: "))
a=[int(input(f"{i+1}.Enter The Value of Sublist[{i}]: "))for i in range(n)]
z.append(a)
x.append(z)
print(x,len(x))
#31.Sort 2 lists in assending order and the duplicate elements will not be considered
def ms(a,b):
    a.extend(b)
    c=set(a)
    d=list(c)
    d.sort()
    return d
a=[1,2,3,3,4,5,6]
b=[4,4,5,6,7,8,9]
print("The Sorted List will be:",ms(a,b))
#32.Predict Output
def l(x):
    print(x)
    print("Address of new_list:",id(x))
    x.append(67)
    print("Address of new_list:",id(x))
    print(x)
list=list((12,23,34,45,56))
print("Address of original_list:",id(list))
l(list[:])#Passing a new list "list[:]"  as an argument and elements of list[:] are the copy of original list "list"; then the copied list is passed to the function 
#if i do any modification in the list in the function then it will not change the original list which is list=[12,23,34,45,56] this will be unchanged because the the modification is done only in the new copied list so it will not affect the original list
#since "list" and "list[:]" are differnt and reffering different list object; so their memory address will be also different 
print("Address of new_list:",id(list[:]))
print(list)
#33a.Creation of a 2d List
#In Python, a 2D list is a list where each element is itself a list. This means we have a list of lists, where each inner list represents a row (or column, depending on how you interpret it) of elements in a two-dimensional structure.
#So, to summarize:
# A 1D list is a simple list containing elements.
# A 2D list is a list where each element is itself a list.
row=3
column=3
matrix=[]
for i in range(row):
    x=[]
    for j in range(column):
        y=int(input(f"{j+1}.Enter The Value for [{i}]:[{j}] = "))
        x.append(y)
    matrix.append(x)
print(matrix)
#33b.Creation of a 2d List
n=3
x=[]
for i in range(n):
    a=[int(input(f"{j+1}.Enter The Value for [{i}]:[{j}] = ")) for j in range(n)]
    x.append(a)
print(x)
#33c.Creation of a 2d List
n = 3
x = []
for i in range(n):
    a = [int(input(f"Enter the value for [{i}][{j}]: ")) for j in range(n)]
    x.append(a)

print("matrix = [")
for row in x:
    print("    ", row)
print("]")
#33d.Creation of a 2d List
n=int(input("Enter The size of the list: "))
x=[]
for i in range(n):
    a=[input(f"{i+1}.Enter The Value for [{i}]:[{j}]: ")for j in range(n)]
    x.append(a)
for i in x:
    print(i)
#33e.Creation of a pre defined 2d List
l=[[1,2,3],[4,5,6],[7,8,9]]
for i in l:
    print(i)
print(l)
#33f.Creation of a pre defined 2d List
l=[[[1,2,3]],[[4,5,6]],[[7,8,9]]]
for i in l:
    print(i)#it will print the elements of list; due to this a 2d list the elements will be also list
print(l)#it will print the whole list
#34.
x=[12,23,34,45,56]
x=str(x)
y="67"
print(x+y)
#35.
x=[12,23,34,45,56]
x=tuple(x)
y=67
x=x+(y,)
x=list(x)
print(x)
#
a=[("a","b","c")]
ind=0
l=[]
for i in range(len(a)):
    for j in range(len(a[i])):
        l[ind]=a[i][j]
        ind+=1
print(l)