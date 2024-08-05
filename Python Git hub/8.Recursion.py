#1a.Calculation of Factorial using Recursion(Working as Call Stack in memory)
def fact(x):
    if x==0:#Base case
        return 1
    else:
        result = x*fact(x-1)
        return result
n=int(input("Enter The Number: "))
print(f"Factorial of {n} is:",fact(n))
#1b.Calculation of Factorial using Recursion(Working as Call Stack in memory)
def fact(x):
    if x == 0:#Base case
        print("Factorial of 0 is: 1")
        return 1
    else:
        result = x * fact(x-1)
        print(f"Factorial of {x} is:", result)
        return result
#2a.Printing number in reverse order N to 1 using recursion
n = int(input("Enter The Number: "))
fact(n)
def rev(x):
    if x==0:
        return 
    else:
        print(x)
        rev(x-1)
n=int(input("Enter The Number: "))
rev(n)
#2b.Printing number in reverse order N to 1 using recursion
def rev(x):
    if x == 0:
        return 2#when x==0 it will return 2 beacuse I set 2 to return  
    else:
        print(x)
        return rev(x - 1)#it returns the function call by decrementing the value of x by 1 to the actual part from where the function is called first

n = int(input("Enter The Number: "))
result = rev(n)#first function call;Here the function call is decremented in each of the iteration
print("Result:", result)
#3a. Printing 1 to N or first N numbers using Recursion
def num(x):
    if x==11:
        return
    else:
        print(x)
        num(x+1) 
n=int(input("Enter The Starting Number: "))
num(n)
#3b. Printing 1 to N or first N numbers using Recursion
def num(x):
    if x==0:
        return
    else:
        num(x-1)
        print(x) 
n=int(input("Enter The Number: "))
num(n)
#4a.Print Sum of First n numbers using Recursion
def sum(x):
    if x==0:
        return 0
    else:
        result=x+sum(x-1)
        return result
n=int(input("Enter The Number: "))
print(f"Sum of {n} numbers will be:",sum(n))
#4b.Print Sum of First n numbers using Recursion
def sum(x):
    if x==0:
        print(f"Sum of {n} numbers will be: 0")
        return 0
    else:
        result=x+sum(x-1)
        print(f"Sum of {n} numbers will be:",result)
        return result
n=int(input("Enter The Number: "))
sum(n)
#5.Print Value of a when b is the power of a using recursion (take a=2 and b=5)
def power(x,y):
    if y==0:
        return 1
    else:
        result=x*power(x,y-1)
        return result
a=int(input("Enter The Value of a: "))
b=int(input("Enter The Value of b: "))
print("The Result will be:",power(a,b))
#6.Find sum of any fibonacci number using Recursion
def fib(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return (fib(x-1)+fib(x-2))
n=int(input("Enter The Fibonacci Number: "))
print(f"Sum Fibonacci Number {n} is:",fib(n))
#7.Find fibonacci series using Recursion
def fib(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return (fib(x-1)+fib(x-2))
n=int(input("Enter The Fibonacci Number: "))
for i in range(n+1):
    print(f"Sum Fibonacci Number {i} is:",fib(i))
#8.Sum of digits of any number with out using for loop using recursion 
###VVI
def sum(x):
    if x==0:
        return 0
    else:
        unitnumber=x%10
        return unitnumber+sum(x//10)#I have used floor division because it returns integer value
a=int(input("Enter The Number: "))
print("Sum of the digits will be:",sum(a))
#9.Printing Number in reverse order using recursion
###VVI
def rev(x):
    if x==0:
        return 0
    else:
        unitnumber=x%10
        print(unitnumber,end="")
        rev(x//10)#I have used floor division because it returns integer value
a=int(input("Enter The Number: "))
rev(a)
print("-is The Reversed Number of",a)