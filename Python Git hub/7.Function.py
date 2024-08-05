#In Python Function Call will be always after the Function Defination or Function Construction 
#We can say we can call function only after when creating the function defination above the function call
#0a.
def hello():
    return "Hello!"
print(hello())
#0b.
def hello():
    print("Hello!")
hello()
#1a.
def sum(first_number,last_number):
    print(id(first_number))
    print(id(last_number))
    sum=0
    for i in range(first_number,last_number+1):
        sum=sum+i
    return sum
first_number=int(input("Enter The First Number: "))
last_number=int(input("Enter The Last Number: "))
print(id(first_number))
print(id(last_number))
print("Sum is:",sum(first_number,last_number))
#1b.
def sum(a,b):
    sum=0
    for i in range(a,b+1):
        sum=sum+i
    return sum
first_number=int(input("Enter The First Number: "))
last_number=int(input("Enter The Last Number: "))
print("Sum is:",sum(first_number,last_number))
#1c.
def sum():
    sum=0
    first_number=int(input("Enter The First Number: "))
    last_number=int(input("Enter The Last Number: "))

    for i in range(first_number,last_number+1):
        sum=sum+i
    return sum
print("Sum is:",sum())
#1d.
def sum():
    sum=0
    first_number=int(input("Enter The First Number: "))
    last_number=int(input("Enter The Last Number: "))

    for i in range(first_number,last_number+1):
        sum=sum+i
    print("Sum is:",sum)
sum()
#1e.Positional arguments in Python
def sum(a,b):
    sum=0
    for i in range(a,b+1):
        sum=sum+i
    return sum
print("Sum is:",sum(1,10))#Here the arguments are passed to the parameters in the same order as they are present in the function call
#1f\a.Keyword Arguments in function
def sum(a,b):
    sum=0
    for i in range(a,b+1):
        sum=sum+i
    return sum
print("Sum is:",sum(a=1,b=10))#keyword arguments; in function a=1 and b=10
print("Sum is:",sum(b=10,a=1))#still in function a=1 and b=10; Here order of the of the argument doesn't not matter but name of the arguments and parameters should be same 
#1f\b.Keyword Arguments in function
def sum(a,b):
    print(id(a))
    print(id(b))
    sum=0
    i=a
    while i<=b:
        sum+=i
        i+=1
    return sum
first_number=int(input("Enter The First Number: "))
last_number=int(input("Enter The Last Number: "))
print(id(first_number))
print(id(last_number))
print("Sum is:",sum(a=first_number,b=last_number))#keyword arguments;
print("Sum is:",sum(b=last_number,a=first_number))#Here order of the of the argument doesn't not matter but name of the arguments and parameters should be same 
#1g.Default Argument
def sum(a=0,b=0):#When no arguments are Passed then the default value of a and b is set to 0
    print("a is:",a)
    print("b is:",b)
    sum=0
    for i in range(a,b+1):
        sum=sum+i
    return sum
# print("Sum is:",sum(1,10))
print("Sum is:",sum())#No arguments are passed in the function; but in function parameters are set to their default value 0;if i don't set the default value of the parameters and also i don't passed the arguments in function call then it will generate error
#1h.
def sum(x,y):
    print(id(x))
    print(id(y))
    sum=0
    for i in range(a,b+1):
        sum=sum+i
    print("Sum is:",sum)
a=1
b=10
print(id(a))
print(id(b))
sum(a,b)
#2a. Print a list using function
def listt(n):
    x=list(int(input(f"{i+1}.Enter The Value of List[{i}]: "))for i in range(n))
    print("List is:",x)
size=int(input("Enter The Size of List: "))
listt(size)
#2b. Print a list using function
def listt(n):
    x=list(int(input(f"{i+1}.Enter The Value of List[{i}]: "))for i in range(n))
    return x
size=int(input("Enter The Size of List: "))
print("List is:",listt(size))
#3a. Print a tuple using function
def tup(n):
    x=tuple(int(input(f"{i+1}.Enter The Value of tuple[{i}]: "))for i in range(n))
    print("Tuple is:",x)
size=int(input("Enter The Size of Tuple: "))
tup(size)
#3b. Print a tuple using function
def tup(n):
    x=tuple(int(input(f"{i+1}.Enter The Value of tuple[{i}]: "))for i in range(n))
    return x
size=int(input("Enter The Size of Tuple: "))
print("Tupple is:",tup(size))
#4.
def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print("Sum is:",add(1,2,3,4,5,6,7,8,9,10))
#5.
def tup(x):
    sum=0
    for i in x:
        sum+=i
    return sum
n=int(input("Enter The Size of The Tuple: "))
x=tuple(int(input(f"{i+1}.Enetr The Element of Tuple[{i}]: "))for i in range(n))#Not only tuple but also I can Make List and Set as well
print("The Tuple is:",tup(x))
#6.
def tupp(y):
    sum=0
    for i in y:
        sum+=i
    return sum
x=(1,2,3,4,5,6,7,8,9,10)
print("Sum is:",tupp(x))
#7a. Printing Dictionary using Function
def dic(size):
    x={input(f"{i+1}.Enter The Keys: "):int(input(f"{i+1}.Enter The Value: "))for i in range(size)}
    print("Dictionary is:",x)
n=int(input("Enter The Size of The Dictionary: "))
dic(n)
#7b. Printing Dictionary using Function
def dic(size):
    x={input(f"{i+1}.Enter The Keys: "):int(input(f"{i+1}.Enter The Value: "))for i in range(size)}
    return x
n=int(input("Enter The Size of The Dictionary: "))
print("Dictionary is:",dic(n))
#8.Printing Dictionary using Function using keyword argument(**kwargs)
def d(**kwargs):
    print(kwargs)
d(x="a",y=12)
d(x="b",y=23)
d(x="c",y=34)
d(x="d",y=45)
d(x="e",y=56)
#9.Printing Dictionary using Function
def d(dictionary):
    print(dictionary)
    for i,j in dictionary.items():
        print(i,j)
def l(size):
    x=[input(f"{i+1}.Enter The Keys: ")for i in range(size)]
    y=[int(input(f"{i+1}.Enter The Value: "))for i in range(size)]
    a=dict(zip(x,y))
    d(a)
n=int(input("Enter The Size of Dictionary: "))
l(n)
#10.Printing Dictionary using Function using keyword argument(**kwargs)
def my_function(**kwargs):
    print(kwargs)

n = int(input("Enter The Size: "))
key_value_pairs = []

for i in range(n):
    key = input("Enter The Key: ")
    value = int(input("Enter The Value: "))
    x=(key, value)#Making a Tuple with keys and values in each iteration 
    key_value_pairs.append(x)#The Tuple appended into the list
    a=dict(key_value_pairs)#Typecasting the list into dictionary
my_function(**a)#Passing the dictionary as keyword arguments
#11.Nested Function (Function inside of Function)
def outerfunction():
    x=int(input("Enter The Value: "))
    def innerfunction():
        y=int(input("Enter The Value: "))
        result=x+y
        return result
    return innerfunction()
print("Sum is:",outerfunction())
#12.Function to Convert Uppercase Character To Lowercase Character
def convert(x):
    a=list(x)
    for i in range(len(a)):
        if a[i]>="a" and a[i]<="z":
            a[i]=a[i]-"a"+"A"
        elif a[i]>="A" and a[i]<="Z":
            a[i]=a[i]-"A"+"a"
    z=str(a)
    print(z)
name=input("Enter The Name: ")
convert(name)
#13.Function Call by Value or Pass by Value
def add(x):
    x=x+1
    print("Inside Function:",x)
a=4
print("Outside Function:",a)
#14a.Function Call by Reference or Pass by Reference
def lst(x):
    x.clear()#Here I am clearing the list;in python lists are passed in function by reference; so if I clear the list inside the function then the list will be cleared outside of the function too
    #So Outside function the list will print nothing but Inside Function The list will be printed separately
    #To avoid this I have to Return the list which I have Made inside of the function and re-assign to the variable which contains list outside of function (which is shown in 14b) 
    n=int(input("Enter The Size of The List: "))
    x=list(int(input(f"{i+1}.Enter The Value of List[{i}]: "))for i in range(n))
    print("Inside Function List is:",x)
a=[1,2,3,4,5]
lst(a)
print("Outside Function List is:",a)
#14b.Function Call by Reference or Pass by Reference
def lst(x):
    x.clear()
    n=int(input("Enter The Size of The List: "))
    x=list(int(input(f"{i+1}.Enter The Value of List[{i}]: "))for i in range(n))
    print("Inside Function List is:",x,id(x))
    return x
a=[1,2,3,4,5]
print(id(a))
a=lst(a)
print("Outside Function List is:",a,id(a))#Both id's will be same
#14c.Function Call by Reference or Pass by Reference (Best example)
def modify(x):
    n=int(input("Enter The Value: "))
    x.append(n)
    print("Inside Function List is:",x,id(x))
a=[1,2,3,4,5]
modify(a)
print("Outside Function List is:",a,id(a))
#14d.Function Call by Reference or Pass by Reference
def lst(x):
    x.clear()
    n=int(input("Enter The Size of The List: "))
    x=list(int(input(f"{i+1}.Enter The Value of List[{i}]: "))for i in range(n))
    y=tuple(x)
    print("Inside Function Tuple is:",y)
    return y
a=[1,2,3,4,5]
a=lst(a)
print("Outside Function Tuple is:",a)
#14e.Function Call by Reference or Pass by Reference
def lst(y):
    x=list(y)
    x.clear()
    n=int(input("Enter The Size of The List: "))
    x=tuple(int(input(f"{i+1}.Enter The Value of List[{i}]: "))for i in range(n))# In Python, variables are dynamically typed, and we can assign them to objects of different types. The previous assignment x = list(y) creates a list, and later, the assignment x
    # Each assignment to x overwrites the previous reference, and Python automatically manages the memory and type of the variable.
    z=list(x)
    print("Inside Function List is:",z)
    return z
a=(1,2,3,4,5)
a=lst(a)
print("Outside Function List is:",a)
#14f.Function Call by Reference or Pass by Reference
def change(x):
    # x=x[0]+1#It sums the value of x[0] with 1; so type of x will be integer
    # print(type(x))#it will print integer
    x[0]=x[0]+1 #just changing the value of list x[0] position and again re-assign to x[0] again;
    #Due to this both inside and outside both list's 0 positoin value will be chaanged; and the type of x reamains as list
    print(type(x)) #it will print list as type of x
    print("Inside Function:",x)
a=[5]
change(a)
print("Outside Function",a)
#14g.Function Call by Reference or Pass by Reference
def ch(x):
    #x=[1,2,3]#This will not Update the original list;it's just Re-assignment of a new list to x;Each assignment to x overwrites the previous reference, and Python automatically manages the memory and type of the variable.
    x.extend([1,2,3])
    print("Inside Function:",x)
a=[12,23,34]
ch(a)
print("Outside Function:",a)
#14h. This is call by value not call by reference because in python integers are not mutable
def ch(x):
    x=x+1
    print(id(x))
    return x
a=5
a=ch(a)
print(a,id(a))#the id's will be same because this a=ch(a) assignment its not an call by reference 
#15.Function To Find Factorial of Any Number:
def fact(x):
    fact=1
    if x==0:
        print(f"Factorial of {x} is",fact)
    else:
        for i in range(1,x+1):#For the case of factorial the loop will from 1 to the number for which we are calculating the factorial
            fact=fact*i
        print(f"Factorial of {x} is",fact)
a=int(input("Enter The Number: "))
fact(a)
#16.Predict Output
x=50
def func(x):
    x=2
func(x)
print("x is now:",x)#Printing statement is outside of function
#17.Predict Output
def say(msg,time=1):
    print(msg*time)
say("Hello")
say("Abisekh",5)
#18.Find Sum of any Fibobnacci number using loop
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        previous_of_previous_sum=0
        previous_sum=1
        for i in range(2,n+1):
            current_sum=previous_of_previous_sum+previous_sum
            previous_of_previous_sum=previous_sum
            previous_sum=current_sum
        return current_sum
number=int(input("Enter The Fibonacci Number: "))
print(f"Sum of Fibonacci Number {number} is:",fib(number))
#19.Find Fibonacci Sequence till n number
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        previous_of_previous_sum=0
        previous_sum=1
        for i in range(2,n+1):
            current_sum=previous_of_previous_sum+previous_sum
            previous_of_previous_sum=previous_sum
            previous_sum=current_sum
        return current_sum
number=int(input("Enter The Number: "))
for i in range(number+1):
    print(f"Sum of Fibonacci Number {i} is:",fib(i)) 
#20a.
def rectangle_area(x,y):
    return x*y
def rectangle_perimeter(x,y):
    return 2*(x+y)
a=int(input("Enter The Width: "))
b=int(input("Enter The Length: "))
print("The Length and Width of Rectangle",a,b)
print(f"The Area of The Retangle when width is {a} and length is {b} is:",rectangle_area(a,b))
print(f"The Perimeter of The Retangle when width is {a} and length is {b} is:",rectangle_perimeter(a,b))
#20b.
def rectangle_area():
    a=int(input("Enter The Width: "))
    b=int(input("Enter The Length: "))
    print("The Length and Width of Rectangle",a,b)
    return a*b
def rectangle_perimeter():
    a=int(input("Enter The Width: "))
    b=int(input("Enter The Length: "))
    return 2*(a+b)
print(f"The Area of The Retangle is:",rectangle_area())
print(f"The Perimeter of The Retangle is:",rectangle_perimeter())
#21.
class Rectangle:
    def set_dimension(self,length,width):
        self.length=length
        self.width=width
    def rectangle_area(self):
        return self.length*self.width
    def rectangle_perimeter(self):
        return 2*(self.length+self.width)
rectangle=Rectangle()
a=int(input("Enter The Width: "))
b=int(input("Enter The Length: "))
rectangle.set_dimension(a,b)
print("The Length and Width of Rectangle",rectangle.length,rectangle.width)
print(f"The Area of The Retangle when width is {a} and length is {b} is:",rectangle.rectangle_area())
print(f"The Perimeter of The Retangle when width is {a} and length is {b} is:",rectangle.rectangle_perimeter())
#22a.Program to Find any number is Prime or not
def prime(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count=count+1
    if count==2:#If the number is prime there will present only 2 conditions
        print(f"{x} is a Prime Number.")
    else:
        print(f"{x} is not a Prime Number.")
a=int(input("Enter The Number: "))
prime(a)
#22b.Program to Find any number is Prime or not
###VVI
def prime(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count=count+1
    return count
a=int(input("Enter The Number: "))
num=prime(a)
if num==2:
    print(f"{a} is a Prime Number.")
else:
    print(f"{a} is not a Prime Number.")    
#23.
def stat(x):
    x+=1
    print(x)
    return x
a=0
a=stat(a)
a=stat(a)
a=stat(a)
#24.
# This is a module-level variable
static_variable = 0
print(id(static_variable))
def increment_static_variable():
    global static_variable
    static_variable += 1
    print(id(static_variable))
    print("Static variable:", static_variable)

# Test the functions
increment_static_variable()
# print_static_variable()  # Output: Static variable: 1

increment_static_variable()
# print_static_variable()  # Output: Static variable: 2
increment_static_variable()
#25. Create a code where user will enter an alphabet but he can see the very next alphabet from the alphabet he entered
def n1(alpha):
    import string
    l1=string.ascii_lowercase
    alpha=alpha.lower()
    for i in range(len(l1)):
        if l1[i]==alpha:
            return l1[i+1]
        elif alpha=="z":
            alpha=l1[0]
            return alpha
    else:
        return "Invalid input. Please enter a valid alphabet."
l=input("Enter Any Alphabet: ")
print("You have entered:",n1(l))
#26. Create a code where user will enter an alphabet but he can see the very next alphabet from the alphabet he entered
def n2(alpha):
    alpha=alpha.lower()
    l=[chr(i) for i in range(97,123)]
    # for i in range(97,123):
    #     l.append(chr(i))
    for i in range(len(l)):
        if l[i]==alpha:
            return l[i+1]
        elif alpha=="z":
            alpha=l[0]
            return alpha
    else:
        return "Invalid input. Please enter a valid alphabet."
a=input("Enter Any Alphabet: ")
print("You have entered:",n2(a))
#27. Create a code where user will enter an alphabet but he can see the very next alphabet from the alphabet he entered
def n3(alpha):
    if alpha.isalpha()==True and len(alpha)==1:
        alpha=alpha.lower()
        if alpha=="z":
            alpha="a"
            return alpha
        else:
            alpha=chr(ord(alpha)+1)
            return alpha
a=input("Enter Any Alphabet: ")
print("You have entered:",n3(a))