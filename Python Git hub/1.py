#To create virtual environment in this directory we just need to run this line in the terminal-> python -m venv venv
#Till 25/4/2024 virtual environment is not created this directory because till 25/4/2024 it is required in this directory but it requires in future I have to run-> python -m venv venv in the terminal
#####We create vertual environment to resolve any import module issue##### 


#1a.Printing of Hellow World
print("Hellow World!!")
#1b.Use of \n in python which stands for newline character 
print("Hellow \nWorld!!")#\n is the newline operation in python
#2.Printing of my name
print("Abisekh Dey!")
#3a.Printing of name but name is assigned as a string to the character name
#In python we don't need to mention variable datatypes (like we don't have to mention whether the variable is int,float or char type); it can check automatically the datatype when we assign anything to the variable 
name = "Abisekh Dey" #String in python can be written as in "" or '' both can be done
# name = 'Abisekh Dey'
print("My Name is: ",name)
# print("My Name is: "+name)#If in this case name variable is a string then we can concatinate the name string after the string present in the print statement with adding + symbol before name 
#3b.Printing of name but name is assigned as a string to the character name
_Name = "Abisekh Dey"
print("My Name is: ",_Name)
#4a.Sum of 2 numbers integer type
print("Sum is: ",3+4)
#4b.Sum of 2 numbers floating type
print("Sum is: ",67.5+32.5)
#4b.Sum of 2 numbers floating type
print("Sum is: ",50+34.7)
#4c.Sum of 2 numbers using 2 variables; the values of the variables are pre defined
x=3
y=4
print("Sum is: ",x+y)
#5.Printing of my details in python using different datatypes(string,integer,float,boolian)
# String
Name = "Abisekh Dey"
# Integer
Roll_Number = 17632322013
# Float
Grade = 8.9
# Boolian
Is_Student = True
print(Name,Roll_Number,Grade,Is_Student)
print(Name,Roll_Number,Grade,Is_Student,sep="-")
print("Name is: ",Name,"\nRoll Number is: ",Roll_Number,"\nGrade: ",Grade,"\nIs He Student? ",Is_Student)
print("My Name is: "+Name+" My roll number is ",Roll_Number,"My Grade is: ",Grade,"I am a student: ",Is_Student)
#6.Use of separator betweeen variables in the print statement (sep="Enter any characters here by which we want to separate the values of the varriables in the output box")
x=1
y=2
z=3
print(x,y,z,sep="->")
# print(x,y,z,sep='->') #both "" and '' indicates string and act as same
#7.Use of ord(enter vaiable name) function to get the ascii value of a perticular character in the output box
character = "a"
print(type(character))
# character = 'a'
print(ord(character))
#8.Use of chr(enter variable name) function to get the ascii character of a perticular decimal number (Keep in mind: decimal number should not exceed the ascii table)
Ascii_value = 102
print(chr(Ascii_value))
#9.Printing name from user
name = input("Enter Your Name: ")# Here Anything what user gives input in the output box Python takes that as string (if we enter character it will take that as string but if we enter integer then it will take that as string too because all integers are characters according to the ascii table)
print("Your Name is: "+name)
print("Your name is:",name)
print("Showing The Datatype  of:",name,"'str' Stands for String Datatype ->",type(name))# it will show first the value of the variable and then it wll show the datatype of name variable using type(variable name)

###ARITHMETIC OPERATION IN PYTHON###
#10.Sum of 2 numbers From user defined input
x = int(input("Enter The Value of x: "))# Specifying The value of the x is integer type by putting int(input statement)
y = int(input("Enter The value of y: "))# Specifying The value of the y is integer type by putting int(input statement)
sum = x+y
print("Sum is:",sum)
print("Datatype of sum is",sum,type(sum))
#11.Sum of 2 numbers From user defined input
x = float(input("Enter The Value of x: "))# Specifying The value of the x is float type by putting float(input statement)
#taking x=12.3
y = float(input("Enter The value of y: "))# Specifying The value of the y is float type by putting float(input statement)
#taking y=45.8
sum = x+y
print("Sum is:",sum)
print("Datatype of sum is",sum,type(sum))
round_sum = round(sum,1)# round(varible name,number of floating points we require) function rounds up the floating value to the specified floating point numbers which we mentioned in the function
#round(sum,1) if there are more than 1 or only 1 floating point number it will print that number 
#round(sum,2) if there are more than 2 or only 2 floating point number it will print those numbers
print("Rounded Sum is:",round_sum)
#12.Division of 2 numbers
x=int(input("Enter The Value: "))
y=int(input("Enter The Value: "))
Division=x/y
print("Division will be:",Division,"Datatype is:",type(Division))
#13.Remainder of Division of 2 numbers
x=int(input("Enter The Value: "))
y=int(input("Enter The Value: "))
rem=x%y
print("Remainder will be:",rem,"Datatype is:",type(rem))
#14.Multiplication of 2 numbers
x=int(input("Enter The Value: "))
y=int(input("Enter The Value: "))
mul=x*y
print("Multiplication will be:",mul,"Datatype is:",type(mul))
#15.Subtraction of 2 numbers
x=int(input("Enter The Value: "))
y=int(input("Enter The Value: "))
sub=x-y
print("Subtraction will be:",sub,"Datatype is:",type(sub))
#16.Exponent of numbers
x=int(input("Enter The Value: "))
y=int(input("Enter The Value: "))
expo=x**y
print("Exponent will be:",expo,"Datatype is:",type(expo))
#17.Floor Division of 2 numbers (if the answer consist of floating numbers then it will omit the floating part and round up the number to its nearest whole integer)
x=int(input("Enter The Value: "))
y=int(input("Enter The Value: "))
Floor_div=x//y
print("Round up Division will be:",Floor_div,"Datatype is:",type(Floor_div))
#18.Swapping of 2 numbers using third variable from user defined input
x=int(input("Enter The Value: "))
y=int(input("Enter The Value: "))
z=x
x=y
y=z
print("Value of x:",x,"Value of y:",y)
#19.Swapping of 2 numbers without using third variable from user defined input
x=int(input("Enter The Value: "))
y=int(input("Enter The Value: "))
x=x+y
y=x-y
x=x-y
print("Value of x:",x,"Value of y:",y)
####Comparison Operator in Python####
#Comparison Operator Return True or False#
x=2
y=3
print("x is:",x,"y is:",y)
print("1.",x>y)
print("2.",x<y)
print("3.",x==y)
print("4.",x!=y)
print("5.",x>=y)
print("6.",x<=y)
####Logical Operator in Python####
#20.Logical AND operation in Python
x=int(input("Enter The Value: "))
if(x>=0 and x<=10):
   print("This is an Example of Logical AND in Python!")
else:
   print("This is not an Example of Logical AND in Python!") 
#21.Logical OR operation in Python
x=int(input("Enter The Value: "))
if(x==11 or x==12):
   print("This is an Example of Logical OR in Python!")
else:
   print("This is not an Example of Logical OR in Python!") 

#22.Logical NOT operation in Python
x=int(input("Enter The Value: "))
if(not(x==10)):
   print("This is an Example of Logical NOT in Python!")
else:
   print("This is not an Example of Logical NOT in Python!") 
x=5
y=5
print("If x is y:",x is y)
print("If x is not y:",x is not y)
####Bitwise Operatior####
x = 5
y = 3
print("After binary conversion of the values of (x & y); x BITWISE AND y will be=>",x & y,"The answer will be in decimal; binary answer will be converted to decimal\n""If we apply BITWISE NOT then the value will be:",~(x&y),"The BITWISE NOT result will be 2's complement of (x&y)")
print("After binary conversion of the values of (x & y); x BITWISE OR y will be:=>",x | y,"The answer will be in decimal; binary answer will be converted to decimal\n""If we apply BITWISE NOT then the value will be:",~(x|y),"The BITWISE NOT result will be 2's complement of (x|y)")
print("After binary conversion of the values of (x & y); x BITWISE EXOR y will be=>",x ^ y,"The answer will be in decimal; binary answer will be converted to decimal\n""If we apply BITWISE NOT then the value will be:",~(x^y),"The BITWISE NOT result will be 2's complement of (x^y)")
print("BITWISE NOT of x is:",~x,"It is 2's complement of x")
print("BITWISE NOT of y is:",~y,"It is 2's complement of y")
#23.Calculate volume of a sphere
x = 2
pi = 3.14
print("Volume of the Sphere is:",(4/3)*pi*x**3)
#24.Calculate volume of a sphere from user defined input
r = int(input("Enter The Radius: "))
pi = float(input("Enter the value of pi: "))
volume = (4/3)*pi*(r**3)# ** is the exponential operator
print("The Volume of The Sphere is:",volume)
#25.Typecasting String to Int and Int to Float 
x=2
y=5
z=3
str_x=str(x)
str_y=str(y)
str_z=str(z)
final_string = str_x + str_y + str_z #concatenates the str_x,str_y,str_z together
print("The String will be:",final_string,"Datatype is:",type(final_string))
final_int = int(final_string)
print("The Integer Value will be:",final_int,"Datatype is:",type(final_int))
final_float = float(final_int)
print("The Float Value will be:",final_float,"Datatype is:",type(final_float))
#26.Convert Temparature Celcius to Farenheight
Temparature_celcius = float(input("Enter The Temparature in Celcius: "))
Temparature_farenheight = (Temparature_celcius*(9/5))+32
print("The Temparature in Farenheight will be:",Temparature_farenheight)
#27.Find the result of (x>y and x<15) when x=10 and y=5
x=10
y=5
print("The result will be:",x>y and x<15)
#28.If x=5 and y="2" print x+y
x=5
y="2"
print(x+y)
#29.Calculate 8//3+8%2
print("The value will be:",8//3+8%2) 
#30.What will be value of d if d is a float after the operation d=2/7
d=2/7
print("d will be:",d,"Datatype of d will be:",type(d))
#31.What will be value of d if d is a float after the operation d=8/2
d=8/2
print("d will be:",d,"Datatype of d will be:",type(d))#In Python 3, division (/) always returns a float, even if the result is a whole number. This behavior is different from Python 2, where the division of two integers would result in an integer if the division was exact.
#32.What will be value of d if d is a float after the operation d=2//7
d=2//7
print("d will be:",d,"Datatype of d will be:",type(d))#In python 3, floor division returns an int
#33.What will be value of d if d is a float after the operation d=10//2
d=10//2
print("d will be:",d,"Datatype of d will be:",type(d))
#34.Find any number is Positive or Negetive
x = int(input("Enter The Number: "))
if(x>=0):
   print("The Number is Positive!")
else:
   print("The Number is Negetive!")
#35.Check Any Number Even or Odd
x = int(input("Enter The Value: "))
if(x%2==0):
   print("The Number is Even!")
else:
   print("The Number is Odd!")
#36.Calulate Profit or Loss
x = int(input("Enter The Cost price: "))
y = int(input("Enter The Sell price: "))
if x<y :
   print("Profit is made!\n""Profit=",y-x)
elif x==y :
   print("Neither Profit Nor Loss!")
else :
   print("Loss is Made!\n""Loss=",x-y)
#37.Print Grade based on Marks
x = int(input("Enter The Marks: "))
if x>=90 and x<=100:
   print("Grade Obtained O")
elif x>=80 and x<=89:
   print("Grade Obtained E")
elif x>=70 and x<=79:
   print("Grade Obtained A")
elif x>=60 and x<=69:
   print("Grade Obtained B")
elif x>=50 and x<=59:
   print("Grade Obtained C")
elif x>=40 and x<=49:
   print("Grade Obtained D")
elif x<40:
   print("Grade Obtained F")
else:
   print("Invalid Marks")
#38.Check Any Number is 4 digit or not
x = int(input("Enter The Number: "))
if x>=1000 and x<=9999:
   print("The Number is 4 digit Number!")
else:
   print("The Number is not a 4 digit Number!")
#39.Find The Gratest Number Between 3 Numbers
x = int(input("Enter The Number: "))
y = int(input("Enter The Number: "))
z = int(input("Enter The Number: "))
if x>y and x>z:
   print("Greatest Number is:",x)
elif y>x and y>z:
   print("Greatest Number is:",y)
elif z>x and z>y:
   print("Greatest Number is:",z)
else:
   print("Both Numbers are Same!")
#40.Find The Gratest Number Between 3 Numbers Using Nested If-Else
x = int(input("Enter The Number: "))
y = int(input("Enter The Number: "))
z = int(input("Enter The Number: "))
if x>y:
   if x>z:
      print("Greatest Number is:",x)
   else:
      print("Greatest Number is:",z)
elif y>x:
   if y>z:
      print("Greatest Number is:",y)
   else:
      print("Greatest Number is:",z)
else:
      print("Both Numbers are Same!") 
#41.Find The Gratest Number Between 3 Numbers Using Nested If-Else
x = int(input("Enter The Number: "))
y = int(input("Enter The Number: "))
z = int(input("Enter The Number: "))
if x>y:
   if x>z:
      print("Greatest Number is:",x)
   else:
      print("Greatest Number is:",z)
else:
   if y>z:
      print("Greatest Number is:",y)
   else:
      print("Greatest Number is:",z)
#42.Take a Number and Check Whether it is Divisible by 3 or 5 when it is not Divisible by 15
x = int(input("Enter The Number: "))
if x%15==0:
   print(x,"is Divisible by 15")
else:
   if x%3==0 or x%5==0:
      print(x,"is Divisible by 3 or 5")
      if x%3==0:
         print(x,"is Divisible by 3")
      else:
         print(x,"is Divisible by 5")
   else:
      print(x,"is not Divisible by 3 or 5 too")
#43.Making of a Calculator Using Match Case in Python
x = int(input("Enter number 1: "))
y = int(input("Enter Number 2: "))
ope = input("Enter The Operation: ")
match ope:
   case "+": print("Sum is:",x+y)
   case "-": print("Subtraction is:",x-y)
   case "*": print("Multiplication is:",x*y)
   case "/": print("Division is:",x/y)
   case "%": print("Remainder is:",x%y)
   case "**": print("Exponent is:",x**y)
   case "//": print("Floor Division is:",x//y)
   case _: print("Invalid Operator!")#case _:stands for default case
#44.Find any Number is Even or Odd using Ternary Operator
x = int(input("Enter The Number: "))
print("Number is:","Even"if x%2==0 else"Odd")
#45a.Use of For Loop in Python
for i in range(0,10):#We use range Function to implement for loop in python 
   #in Python Loop strats from 0; but in this case i will start from 1 and i will run i<10 = 9 times 
   #but in python i++ is not required because it i++ automatically generated by range function by default or we can say 'step size' i++ is by default set by range function
   #If we don't mention any step size then range function will automatically by deault set the step size to i++
   #But we can change the step size as well by mentioning the step size range(starting point,(i<ending point),step size) where step size is set by default i++ or we can set i+2 or i+3 and so on... 
   print(i,"Abisekh Dey")
#45b.Use of For Loop in Python
for i in range(5):#in python range(5) generates values from 0 to 4. Therefore, when we print i after the loop, it prints 4, not 5.
   print(i)
print(i)#it prints 4, not 5.
#45c. Use of While Loop in Python
i=0
while i<5:
   print(i)
   i+=1
print(i)#it will print 5 because after printing the value of i in the loop it increments the value of i; but after i=4 iteration after printing i=4 then again it will increment the value of i and then it will be i=5 but due to the loop condition i<5 so when the value of i will be equal to 5 the loop will end and outside the loop it will print the final value of i which will be 5
#46.Use of For Loop in Python without using i
for _ in range(0,10,2):#2 is the step size; if we don't use i then I have to enter an underscore '_' at the place of i
   print("Abisekh Dey")
#47.Print first 10 numbers using for loop
for i in range(0,10):
   print("Number is:",i+1)#Taking i+1 to avoid printing 0 to 9 because i want to print 1 to 10
#48.Print First 100 Even numbers
for i in range(0,100):
   if i%2==0:
      print("Even Number is:",i)
#49.Print how many numbers in 100 is divisible by 17
for i in range(0,100):
   if i%17==0:
      print(i,"is Divisible by 17 and division result is:",i/17)#'/' operator returns float value
#50.Print sum of first 10 numbers
sum = 0
for i in range(0,10):
   sum = sum + i
print("Sum is:",sum)
#51a.Print Table of 5
x = int(input("Enter The Number For which You want to see The Table: "))
for i in range(1,11):
   print("Table of",x,"Will be",i,"*",x,"=",i*x)
#51b.Print Table of 5
x = int(input("Enter The Number For which You want to see The Table: "))
for i in range(1,11):
   print(i*x,end="\t")#By default, print adds a newline character at the end of each printed line. However, you can change this behavior by specifying the end parameter.
#52.Print of List datatype using for Loop 
list = [1,2,3,"apple",5.4,[10,20,30]] #List can contain any data type
for i in list:
   print(i)#This code will print each element of the list on a new line.
#53.Print of a List datatype without for loop
list = [1,2,3,"apple",5.4,[10,20,30]] #List can contain any data type
print(list)
#54.Use of While loop in Python
i = 0
while i<10:
   print("Abisekh Dey")
   i=i+1  #in Python i++ or i-- is not allowed to change the value of i we have to do i=i+1 or i=i-1
#55.Printing of first 10 numbers using while loop
i = 0
while i<10:
   print("Number is:",i+1)#Taking i+1 to avoid printing 0 to 9 because i want to print 1 to 10
   i=i+1
#56.Printing of first 100 numbers in reverse order using while loop
i = 100
while i>0:
   print("Number is:",i)
   i=i-1
#57.Print First 100 Odd numbers using While loop
i = 0
while i<100:
   if i%2!=0:
      print("Odd Number is:",i)
   i=i+1
#when We use a for loop in Python, it doesn't lend itself easily to the kind of dynamic control you're attempting in the C code. 
#If you want to have more control over the loop iteration, especially in cases where you might want to repeat or skip iterations based on dynamic conditions, a while loop is often more suitable.
#58a.Proghram to reverse a loop (Wrong Method but in C language this a correct method because there i can dynamicly control for loop)
for i in range(0,10):
   x = int(input(f"{i}.Enter The Number: "))
   if x==5:
      print("Number Can't be 5!")
      i=i-1 # No use of this line because this can not reverse the loop; because we can't dynamicly control for loop in Python
      #Here the loop will continue from i=0 to i<10 and when x==5 becomes true then it prints Number Can't be 5! and then modes to the next iteration
      # x is not an array due to this the value of x is updated in each iteration
      continue 
#58b.Proghram to reverse a loop (Wrong Method but in C language this a correct method because there i can dynamicly control for loop)
for i in range(0,10):
      for j in range(i,i+1):
         x = int(input("Enter The Number: "))
         if x==5:
            print("Number Can't be 5!")
            j=j-1# No use of this line because this can not reverse the loop; because we can't dynamicly control for loop in Python
            #Here the loop will continue from i=0 to i<10 and when x==5 becomes true then it prints Number Can't be 5! and then modes to the next iteration
            # x is not an array due to this the value of x is updated in each iteration
            continue
#58c.Proghram to reverse a loop using while loop when x==5
i = 0
while i<10:
   x = int(input("Enter The Number: "))
   if x==5:
      print("Number Can't be 5!")
      i=i-1
      continue
   i=i+1
#58d.Proghram to reverse a loop when x==5 using while loop dynamically to control the outer for loop
for i in range(0,10):
    j = i
    while j <= i:
        x = int(input("Enter The Number: "))
        if x == 5:
            print("Number Can't be 5!")
            j = j - 1
            continue
        break
#59.Printing of first 10 numbers in reverse order using for loop
for i in range(10,0,-1):
   print(i)
#60.Finding multiplication of first 10 numbers
i = 1
Mul = 1
while i<11:
   Mul = Mul*i
   i = i+1
print("Multiplication of First 10 Numbers are:",Mul)
#61a.Print First 100 Even Numbers without using % operator
i = 2
while i<101:
   print("Even Number is:",i)
   i = i+2
#61b.Print First 100 Odd Numbers without using % operator
i = 1
while i<100:
   print("Odd Number is:",i)
   i = i+2   
#61c.Print First 100 Odd Numbers without using % operator
for i in range(1,100,2):
   print("Odd Number is:",i)
#61d.Print First 100 Even Numbers without using % operator
for i in range(2,101,2):
   print("Odd Number is:",i)
#62.Find Output
x = 1
while x==1:
   x = x-1
print(x)# 0
#63.Predict Output
x = 4
y = 0
while x>=0:
   x = x-1
   y = y+1
   if x==y:
      continue # skips the condition when x==y
   else:
      print(x,y)
#64.Predict Output
x = 4
y = 0
while x>=0:
   x = x-1
   y = y+1
   if x==y:
      break # Ends The program when x==y
   else:
      print(x,y)
#65.Predict Output
x = 4
y = 0
while x>=0:
   if x==y:
      break # Ends The Program when x==y
   else:
      print(x,y)
   x = x-1
   y = y+1
###PATTERN PRINT IN PYTHON###
#66.Predict Output
for i in range(3):
   print(" * "*5) # * is reffered as Multiplication operator;but " * " asterics in double quotes means string;then i multiplied the string with 5 to print 5 asterics(This can Happen only in python )
   # Multiplication of string with an integer happens only in python
# print(" * * * * * ")
#67a.Predict Output
for i in range(3):
   for j in range(0,i+1):
      print(" * ",end="\t")
   print()
#67b.Predict Output
for i in range(3):
   for j in range(i,3):
      print(" * ",end="\t")
   print()
#68.Predict Output
n = int(input("Enter Value: "))
for i in range(n+1):
   print(i,end="\t")
#69a.Predict Output
n = int(input("Enter Value: "))
for i in range(n):
   for j in range(n): #Here the loop will continue till j<n
      print(j+1,end="\t")
   print()
#69b.Predict Output
n = int(input("Enter Value: "))
for i in range(n):
   for j in range(1,n+1): #Here the loop will continue from j=1 to j<=n
      print(j,end="\t")
   print()
#69c.Predict Output
n = int(input("Enter Value: "))
for i in range(n):
   for j in range(n,0,-1): #Here the loop will continue till j>0
      print(j,end="\t")
   print()
#70a.Predict Output
n = int(input("Enter Value: "))
i=0
while i<n:
      j=0
      while j<n:
         print(j+1,end="\t")
         j+=1
      print()
      i+=1
#70b.Predict Output
n = int(input("Enter Value: "))
i=0
while i<n:
      j=1
      while j<=n:
         print(j,end="\t")
         j+=1
      print()
      i+=1
#71.Predict Output
n = int(input("Enter Value: "))
i=0
while i<n:
      j=n
      while j>0:
         print(j,end="\t")
         j-=1
      print()
      i+=1
#72.Printing of Table of n numbers where n=0,1,2,3,4.....
x = int(input("Enter The Number For Which You Want to See The Table: "))
n = int(input("Enter How Many Columns You Want in The Table: "))
print("[More Row = Table of Multiple Numbers Which Will Start From The Previous Table Printing Number]")
m = int(input("Enter How Many Rows You Want in The Table: "))
i=0
while i<m:
      j=1
      while j<=n:
         print(x*j,end="\t")
         j+=1
      print()
      x+=1# Increments the Value of x by after printing a Multiplication table 
      i+=1
#73.Row-wise Multiplication Table Printer" or "Incremental Row Multiplier."
print("The Loop Will Run Equal of The Column Numbers")
n = int(input("Enter How Many Columns You Want in The Table: "))
i=0
while i<n:
      j=1
      while j<=n:
         print(i*j,end="\t")
         j+=1
      print()
      i+=1
#74.Predict Output
n=int(input("Enter The Value: "))
for i in range(n):
   for j in range(n,i,-1):
      print(j,end="\t")
   print()
#75.Predict Output
n=int(input("Enter The Value: "))
for i in range(n):
   for j in range(i,n):
      print(j+1,end="\t")
   print()
#76.Predict Output
n=int(input("Enter The Value: "))
y=ord("A")#65
for i in range(n):
   for j in range(0,i+1):
      x=chr(y+j)#65+0=A;65+1=B printing accordingly
      print(x,end="\t")
   print()
#77.Predict Output
n=int(input("Enter The Value: "))
for i in range(n):
   print(" "*(n-i),end="")
   for j in range(0,i+1):
      print(j+1,end=" ")
   print()
#78.Predict Output
n=int(input("Enter The Value: "))
for i in range(1,n):
   print(" "*(n-i),end="")
   for j in range(1,2*i):
      print(j,end="")
   print()
#79.Predict Output
n = int(input("Enter The Value: "))
for i in range(n):
    print(" " * (n - i), end="")
    for j in range(0, i):
        print(j+1, end=" ")
    print()
#80.Predict Output
i=0
n=int(input("Enter The Value: "))
order = ord("A")
while i<n:
   j=0
   while j<i+1:
      char = chr(order+j)
      print(char,end="\t")
      j+=1
   print()
   i+=1
#81.Predict Output
i=0
n=int(input("Enter The Value: "))
while i<n:
   print(" "*(n-i),end="")
   j=0
   while j<i+1:
      print("*",end=" ")
      j+=1
   print()
   i+=1 
#82.Print memory address of any variable
x=[12,23,34,45,56]
print(id(x))
for i in range(len(x)):
   print(id(x[i]))
#83.Print memory address of any variable
x=12
print(id(x))  
#84.Predict Output
a=3
b=a
print(id(a))
print(id(b))
print(b)  
#85.Predict Output
#in python integers are not mutaable object it means once we create an integer object we cant change/modify/reassign the integer object
#it means if i make a=3 once then i can't change it to a=5; if i try to do so python will create another a variable in the another memory location which will point 5 the integer object
#so a=3 memory address is different with the a=5 memory address 
a = 3
print(id(a))  # Print the memory address of the integer object with value 3
a = 5
b = a
print(id(a))  # Print the memory address of the integer object with value 5
print(id(b))  # Print the memory address of the integer object referred to by b, which is also 5
print(b)      # Print the value referred to by b, which is 5
#85.Predict Output
#in python strings are not mutaable object it means once we create an string object we cant change/modify/reassign the string object
#it means if i make a="abisekh" once then i can't change it to a="pallabi"; if i try to do so python will create another a variable in the another memory location which will point "pallabi" the string object
#so a="abisekh" memory address is different with the a="pallabi" memory address 
a="abisekh"
print(id(a))# Print the memory address of the string object with value "abisekh"
a="pallabi"
b=a
print(id(a))# Print the memory address of the string object with value "pallabi"
print(id(b))# Print the memory address of the string object referred to by b, which is also "pallabi"
print(b)# Print the value referred to by b, which is "pallabi"
#86.Predict Output
a = 3
print(id(3))
print(id(a))  # The memory address of the integer object 3 that 'a' refers to
three = 3
print(id(3))  # The memory address of the integer object 3 that is not referenced by 'a'
print(id(three))
print(a+three)
three = 3.0
print(id(three))
print(id(3.0))
#87.Predict Output
a=3
print(id(a))
print(id(3))
a=3
print(id(a))
print(id(3))
#88.Predict Output
a=int(3)
print(id(a))
print(id(3))
print(id(int))
#89.
import msvcrt

def get_password(prompt="Enter your password: "):#this function gets a Default Argument in promt parameter
    print(prompt, end='', flush=True)#printing the promt parameter; to stop moving the cursor to the next line end=' ' is used;
    #In this password prompt scenario, it's important to immediately display the asterisks (*) representing the password characters as the user types them, without waiting for them to press Enter. So, flush=True ensures that the asterisks are displayed in real-time as the user types the password.
    password = ''#A variable password is initialized as an empty string to store the password entered by the user.
    while True:#The while True: loop runs indefinitely until the user presses the Enter key.
        char = msvcrt.getch()#each time msvcrt.getch() is called within the loop, it captures a single character entered by the user, which is then stored in the char variable for further processing. This allows the program to handle each character entered by the user individually, without echoing it to the console.
        #msvcrt.getch() returns bytes, not strings. Bytes represent raw data, while strings represent text.
        #print(type(char))#it will print the type of char in bytes
        char = char.decode('utf-8')#char.decode('utf-8') converts the character received from msvcrt.getch() from bytes to a Unicode string and assigns to char variable, enabling further processing within the Python program.
        #print(type(char))#it will print the type of char in string
        if char == '\r' or char == '\n':#it will check if the input character is "\r"-> carriage return or "\n"
            print()#This print statement is used because after we entering the password we have to move the cursor to the next line so in python print statement by default print a newline after excecution
            return password
        elif char == '\b':#it will check if user press any backspace 
            if password:#This condition ensures that there are characters in the password string before attempting to delete a character. It prevents attempting to delete a character when the password is already empty.
                password = password[:-1]#if backspace is pressed then This line removes the last character from the password string. The slice [:-1] effectively deletes the last character from the string.
                print('\b \b', end='', flush=True)
                #print('\b \b', end=''): This print statement is used to erase the last character echoed on the screen due to the backspace(backspace is also a character). It outputs a backspace character ('\b') to move the cursor back one position, then prints a space to overwrite the last character, and finally another backspace character to move the cursor back again. This effectively simulates erasing the last character from the screen.
        else:
            password += char#concatinating "char" in password string one by one 
            print('*', end='', flush=True)#An astericks(*) is printed at the place of input character in each iteration of loop 

password = get_password()
print("Password entered:", password)
#90.
pin = int(input("Enter The Pin: "))

import getpass

password = getpass.getpass("Enter your password: ")

print("Password entered:", password)
#91.
from datetime import datetime

def calculate_age(birthdate):
    today = datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def main():
    # Input your date of birth in YYYY-MM-DD format
    date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        dob = datetime.strptime(date_of_birth, "%Y-%m-%d")
        age = calculate_age(dob)
        print("Your age is:", age)
    except ValueError:
        print("Invalid date format. Please enter in YYYY-MM-DD format.")

if __name__ == "__main__":
    main()
#92a.
from datetime import datetime
print(datetime.now())
print(datetime.today())
print(datetime.today().strftime("%Y-%m-%d %H:%M"))
x=datetime.now()#this is a class method of datetime class
print(x)
print(x.year)
print(x.day)
print(x.month)
print(x.strftime("%B"))#This prints the full name of the month of the datetime object x.
print(x.strftime("%b"))#This prints the abbreviated name of the month of the datetime object x
print(x.strftime("%m"))#This prints the month number (with zero padding) of the datetime object x.
print(x.strftime("%Y"))#This prints the year with century (e.g., "2024") of the datetime object x.
print(x.strftime("%y"))#This prints the year without century (e.g., "24") of the datetime object x.
print(x.strftime("%I"))#This prints the hour (12-hour clock) of the datetime object x.
print(x.strftime("%H"))#This prints the hour (24-hour clock) of the datetime object x.
print(x.strftime("%p"))#This prints "AM" or "PM" based on the hour of the datetime object x.
print(x.strftime("%M"))#This prints the minute (with zero padding) of the datetime object x.
#92b.
from datetime import datetime
x=datetime(2024,2,21)
print(x)
print(x.year)
print(x.day)
print(x.month)
print(x.strftime("%B"))#This prints the full name of the month of the datetime object x.
print(x.strftime("%b"))#This prints the abbreviated name of the month of the datetime object x
print(x.strftime("%m"))#This prints the month number (with zero padding) of the datetime object x.
print(x.strftime("%Y"))#This prints the year with century (e.g., "2024") of the datetime object x.
print(x.strftime("%y"))#This prints the year without century (e.g., "24") of the datetime object x.
print(x.strftime("%I"))#This prints the hour (12-hour clock) of the datetime object x.
print(x.strftime("%H"))#This prints the hour (24-hour clock) of the datetime object x.
print(x.strftime("%p"))#This prints "AM" or "PM" based on the hour of the datetime object x.
print(x.strftime("%M"))#This prints the minute (with zero padding) of the datetime object x.
#93a.
from datetime import datetime
x=datetime(2024,2,21)
print(x.now())
y=datetime.now()
print(x)
print(y)
print(x.year)
print(y.day)
z=y.strftime("%Y")
print(z)
#93b.
import datetime
y=datetime.datetime.now()
print(y)
#94a.
from datetime import datetime

date_string = "2024-02-21"
formatted_date = datetime.strptime(date_string, "%Y-%m-%d")
print(formatted_date)
#94b.
from datetime import datetime

date_string = "2024-02-21"
format_string = "%Y-%m-%d"

formatted_date = datetime.strptime(date_string, format_string)
#95a.
import time
import os
# print("This statement will be printed for 1 minute.")
# time.sleep(5)
# os.system("cls")

def print_for_one_minute():
    # Set the statement to print
    statement = "This statement will be printed for 1 minute."

    # Calculate the time after 1 minute
    end_time = time.time() + 5  # 5 seconds increased in actual time

    # Print the statement
    print(statement)

    # Loop until 1 minute is over
    while time.time() <= end_time:
        # Sleep for a short duration to avoid high CPU usage
        time.sleep(1)#sleep duration is 1 second for each duration; total 5 durations so sleep duration will be 5*1=5 seconds

    # Clear the screen after 1 minute
    os.system('cls' if os.name == 'nt' else 'clear')#On Windows, cls is used to clear the console.
      #On Unix/Linux/Mac, clear is used to clear the terminal screen.

if __name__ == "__main__":
    print_for_one_minute()
#95b.
import time
import os
print("This statement will be printed for 1 minute.")
time.sleep(5)
os.system("cls")

#96.
import time
print(time.time())
#97.
import time

# Get the current time as a time tuple
current_time = time.localtime()

# Format the time as a string in the desired format
formatted_time = time.strftime("%I:%M %p", current_time)

# Print the formatted time
print("Current time:", formatted_time)
#98a. Printing of Digital Clock
from datetime import datetime
import time

def update_clock():
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("\r"+current_time, end="", flush=True)# concatinating /r and current_time with each other ; \rcurrent_time here \r moves the cursor to the beginning of the line and prints current_time after 1 second in infinite loop (while true) 
        time.sleep(1)  # Sleep for 1 second before updating the time

# Start updating the clock
update_clock()
#98b. Printing of Digital Clock
from datetime import datetime
import time

def update_clock():
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("\r",current_time, end="", flush=True)# It will print the same as 98a but it will print a space before printing the time due to the comma before current_time
        time.sleep(1)  # Sleep for 1 second before updating the time
update_clock()
#99. Use of \r Carriage return
print("Black\rWhite")# here \r moves the cursor to start of the line and overrites the lenth of white on to black
print("Abisekh\rDey")# here \r moves the cursor to start of the line and overrites the lth of Dey on to Abisekh
#100. Predict Output
a=2
b="2"
print(a==b)#It will be false because a is in int and b is in string
#101. Predict Output
x="abisekh"
for i in x:
   print(i)
#102. Number guessing game 
x=25
y=int(input("Guess The Number: "))
while x!=y:
   y=int(input("Wrong Guess! Guess The Number Again: "))
print(f"Congratulations! You Guessed The Correct Number {x}")
#103.
sum=0
for i in range(101):
   if i%5==0:
      sum+=i
print(sum)