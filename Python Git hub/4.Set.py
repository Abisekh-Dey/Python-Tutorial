#1a.Implementation of Set in Python
col={"Red","White","Blue"}
print(col,type(col),len(col))
print(hash(col))
#1b.Implementation of Set in Python
col=set(("Red","White","Blue"))
print(col,type(col),len(col))
#1c.Implementation of Set in Python
col={"Red","White","Blue",15,3.14,(9,0,7,5,(2,4,6))}#Lists are not allowed in set because list is unhashable
#Lists in Python are mutable, meaning their contents can be changed after creation. Mutable objects, like lists, don't have a fixed hash value because their content can change over time. As a result, lists are not hashable or unhashable.
#In Python, sets are indeed mutable, and a set containing another set is not hashable. When you have a set as an element of another set, the outer set becomes unhashable. This is because the inner set is mutable, and mutable objects cannot be hashed in Python.
print(col,type(col),len(col))
#1d.Implementation of single element Set in Python
x={1,}
print(x,type(x))
#1e.Implementation of single element Set in Python
x={1}#Comma is not necessary for sets and list to present single element set or list in python however comma is necessary in tuple to present single element tuple
print(x,type(x))
#2.Printing Set using For Loop
col={"Red","White","Blue"}
for i in col:
    print("Element",i,"Datatype:",type(i))
#3.Check any specific item is present in the Set or not
col={"Red","White","Blue"}
if "Red" in col:
    print("Red is present in the set!")
#3.Check any specific item is present in the Set or not
col={"Red","White","Blue"}
x=input("Enter The Element You Want to Find: ")
find=False
if x in col:
    find=True
if find==True:
    print(x,"is Present in The Set!")
else:
    print(x,"is not Present in The Set!")
#3a.Check any specific item is present in the Set or not
x={"Red","White","Blue",15,3.14,(9,0,7,5,6)}
find=False
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
elif dtype=="tuple":
    y=tuple(int(input(f"Enter The Element you Want to find of Tuple[{i}]: ")) for i in range(5))
    if y in x:
        found=True
if found is True:
    print(y,"is Present in The Set!")
else:
    print(y,"is not Present in The Set!")
#3b.Check any specific item is present in the Set or not
x={12,23,34,45,56}
y=int(input("Enter The Element You Want to Find: "))
if y in x:
    print(y,"is Present in Set!")
else:
    print(y,"is not Present in Set!")
#4a.Implementation of User Defined Set
n=int(input("Enter The Size of The Set: "))
x={int(input(f"{i+1}.Enter The Element of Set[{i}]: ")) for i in range(n)}
print(x,"Datatype:",type(x))
#4b.Implementation of User Defined Set
n=int(input("Enter The Size of The Set: "))
x=set()#writing {} and set() are not same process of writing empty set; if we want to create an empty set then I have to do set() instead of doing {}
#Though {elements,} is a way of mentioning set in python 
#But in the case of when we have to create an empty set we have to avoid this only writing {} but this is a correct approach of creating empty list [] and empty tuple (); because {} This syntax is used to create an empty dictionary, not an empty set
#So when we have to create an empty set we have to do set() instead of doing this {}
for i in range(n):
    y=input(f"{i+1}.Enter The Element of Set[{i}]: ")
    x.add(y)#.add() function is used to add only 1 element in set but we can't use .append() function in set; append function only can be used in list
print(x,"Datatype:",type(x))
#4c.Implementation of User Defined Set
n=int(input("Enter The Size of The Set: "))
x=set(int(input(f"{i+1}.Enter The Element of Set[{i}]: ")) for i in range(n))
print(x,"Datatype:",type(x))
#4d.Implementation of User Defined Set
n=int(input("Enter The Size of The Set: "))
x=set()
i=0
while i<n:
    y=int(input(f"{i+1}.Enter The Element of Set[{i}]: "))
    x.add(y)
    i+=1
#4e.Implementation of User Defined Set; set contains only tuple datatypes
n=int(input("Enter The Size of The Set: "))
x=set()
i=0
while i<n:
    y=tuple(int(input(f"{i+1}.Enter The Element of Set[{i}]: "))for i in range(n))
    x.add(y)#add function can not add unhashable type item in set,but update function can add unhashable types item in set(like list and set)
    i+=1
print(x,"Datatype:",type(x))  
#4f.Implementation of User Defined Set; set contains different datatypes except list and set bacause these are hashable
n=int(input("Enter The Size of The Set: "))
x=set()
i=0
while i<n:
    y=tuple(int(input(f"{i+1}.Enter The Element of Set[{i}]: "))for i in range(n))
    a=tuple(int(input(f"{i+1}.Enter The sub Element of Set[{i}]: "))for i in range(n))
    y=y+(a,)
    x.add(y)
    i+=1
print(x,"Datatype:",type(x))  
#4g.Implementation of User Defined Set; Take the elementts of set as list
#But This will generate Error Because List is unhashable; So we can't keep List at any place of set
#Corrected code is [4h] because if we want to keep list in the set then we have to type cast the list into tuple which is shown in [4h]
n=int(input("Enter The Size of The Set: "))
x=set()
i=0
while i<n:
    y=[int(input(f"{i+1}.Enter The Element of Set[{i}]: "))for i in range(n)]#taking Elements of List
    num=(10,20,30)
    num=num+(y,)#[Presenting list y as typle by writing (y,) but it doesn't type cast the list y into tuple];then concatinating tuple (y,) in tuple num
    x.add(num)
    i+=1
print(x,"Datatype:",type(x))  
#4h.Implementation of User Defined Set; set contains only tuple datatypes;Take the elementts of set as list
n=int(input("Enter The Size of The Set: "))
x=set()
i=0
while i<n:
    y=[int(input(f"{i+1}.Enter The Element of Set[{i}]: "))for i in range(n)]#taking Elements of List
    num=tuple(y)#Type casting List y into tuple y
    x.add(num)
    i+=1
print(x,"Datatype:",type(x))  
#5a.Use of Update()function in set
x={12,23,34,45,56}
y={67,78}
x.update(y)#.update() function is used to add more than 1 element or sequences of elements in set
print(x)  
#5b.Use of Update()function in set
x={12,23,34,45,56}
y=("red","white")
x.update(y)
print(x)  
#5c.Use of Update()function in set
x={12,23,34,45,56}
y=[67,78]
x.update(y)
print(x)  
#6a.Remove element from a set remove(element) function
col={"Red","White","Black","Green","Blue"}
col.remove("Black")#This function will throw error if the item not present in the set
print(col,"After Removing The Length of The Set Decreases to:",len(col))
#6b.Remove element from a User Defined set remove(element) function
n=int(input("Enter The Size of The Set: "))
x={int(input(f"{i+1}.Enter The Element of Set[{i}]: ")) for i in range(n)}
print(x,"The Initial Length of The Set is:",len(x))
rem=int(input("Enter The Element You Want to Remove: "))
x.remove(rem)#This function will throw error if the item not present in the set
print(x,"After Removing The Length of The Set Decreases to:",len(x))
#6c.Remove element from a User Defined set remove(element) function and inplementation discard(elemnet) function
n=int(input("Enter The Size of The Set: "))
x={int(input(f"{i+1}.Enter The Element of Set[{i}]: ")) for i in range(n)}
print(x,"The Initial Length of The Set is:",len(x))
rem=int(input("Enter The Element You Want to Remove: "))
x.remove(rem)
print(x,"After Removing The Length of The Set Decreases to:",len(x))
rem=int(input("Enter The Element You Want to Remove: "))
x.discard(rem)
print(x,"After Removing The Length of The Set Decreases to:",len(x))
rem=int(input("Enter The Element You Want to Remove: "))
x.discard(rem)#This function will not throw error if the item not present in the set
print(x,"After Removing The Length of The Set Decreases to:",len(x))
#6d.Remove element from a User Defined set remove(element) function and inplementation discard(elemnet) function
n=int(input("Enter The Size of The Set: "))
x={int(input(f"{i+1}.Enter The Element of Set[{i}]: ")) for i in range(n)}
print(x,"The Initial Length of The Set is:",len(x))
m=int(input("How Many Number You Want to Remove: "))
rem=[int(input(f"{i+1}.Enter The Element You Want to Remove: "))for i in range(m)]
x.remove(rem[0])#This function will throw error if the item not present in the set
print(x,"After Removing The Length of The Set Decreases to:",len(x))
for i in range(1,len(rem)):#Loop Starts From 1 index of the list rem
    x.discard(rem[i])#This function will not throw error if the item not present in the set
    print(x,"After Removing The Length of The Set Decreases to:",len(x))
#7.Use of Union() function in set
#Format: new set = set1.union(set2)
x={12,23,34,45,56}
y=[67,78,89]
print("x is:",x,"\ny is:",y)
result=x.union(y)#Return the union of sets as a new set.(i.e. all elements that are in either set.)
#between 2 variable x and y one of these have to be in set
print("Union of x and y will be:",result)
x.update(y)#Update a set with the union of itself and others.
print("Updating y in x The Result will be:",x)
#8.Use of Intersection() and intersection_update() function in set
#Format: new set = set1.intersection(set2)
#Format: set1.intersection_update(set2)
x={12,23,34,45,56}
y=[56,67,78]
print("x is:",x,"\ny is:",y)
result=x.intersection(y)#Return the intersection of two sets as a new set.(i.e. all elements that are in both sets.)
#between 2 variable x and y one of these have to be in set
print("Intersection of x and y will be:",result)
x.intersection_update(y)#Update a set with the intersection of itself and another.
print("Intersection of x and y will be:",x)
#9.Use of symmetric_difference()function in set
x={12,23,34,45,56}
y=[56,67,78]
print("x is:",x,"\ny is:",y)
result=x.symmetric_difference(y)#Return the symmetric difference of two sets as a new set.(i.e. all elements that are in exactly one of the sets.)
#between 2 variable x and y one of these have to be in set
print("Sets With out Common elements will be:",result)
x.symmetric_difference_update(y)
print("Sets With out Common elements will be:",x)
#10a.Find Common Elements in 3 Lists using Set and the result will be in list
a=[1,5,10,20,40,80]
b=[6,7,20,80,100]
c=[3,4,15,20,30,70,80,120]
set_a=set(a)
set_b=set(b)
set_a.intersection_update(set_b)
set_a.intersection_update(c)
result=list(set_a)
print("Common Elemens in 3 Lists will be",result)
#10b.Find Common Elements in 3 Lists using Set and the result will be in list
a=[1,5,5]
b=[3,4,5,5,10]
c=[5,5,10,20]
set_a=set(a)
set_a.intersection_update(b)
set_a.intersection_update(c)
result=list(set_a)
print("Common Elemens in 3 Lists will be",result)
#11.Find Sum of all numbers in list
x={1,2,3,4,5,6,7,8,9,10}
print("Sum is:",sum(x))
#11.
import random

x = {1234, 3456, 9000, 1233}

for i in x:
    y = random.choice(tuple(x))
print(y, type(y))
#12.
import random

x = {1234, 3456, 9000, 1233}
y = random.choice(tuple(x))
print(y, type(y))
