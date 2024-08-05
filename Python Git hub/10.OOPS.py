#1.
class Student:
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
student1=Student()
x=input("Enter The Name: ")
student1.set_name(x)
print(student1.name)
print(student1.get_name())

student2=Student()
x=input("Enter The Name: ")
student2.set_name(x)
print(student2.name)
print(student2.get_name())
#1f.
def name(x):
    return x
for i in range(2):
    a=input("Enter The Name: ")
    print(name(a))
    print(name(a))
#2.
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
#2f.
def rectangle_area(x,y):
    return x*y
def rectangle_perimeter(x,y):
    return 2*(x+y)
a=int(input("Enter The Width: "))
b=int(input("Enter The Length: "))
print("The Length and Width of Rectangle",a,b)
print(f"The Area of The Retangle when width is {a} and length is {b} is:",rectangle_area(a,b))
print(f"The Perimeter of The Retangle when width is {a} and length is {b} is:",rectangle_perimeter(a,b))
#3a.
class Square:
    def squ(self,x):
        self.side=x
        print("The Side of the Square is: ",self.side)
        print("The Side of the Square is: ",square.side)
        return self.side*self.side
square=Square()
a=int(input("Enter The Side: "))
square.squ(a)
# print("The Side of the Square is: ",square.side)
print("Area of The Square is: ",square.squ(a))
#3b.
class Square:
    def squ(self,x):
        self.side=x
    def square_area(self):
        return self.side*self.side
square=Square()
a=int(input("Enter The Side: "))
square.squ(a)
print("The Side of the Square is: ",square.side)
print("Area of The Square is: ",square.square_area())
#3f.
def square(x):
    return x*x
a=int(input("Enter The Side: "))
print("The Area of The Square is:",square(a))
#4.Constructor (sum of all digits of a number)
class Digit:
    def __init__(self,num):
        self.num=num
    def sum(self):
        if self.num==0:
            return 0
        else:
            x=self.num%10
            return x+Digit(self.num//10).sum()
a=int(input("Enter The Number: "))
number=Digit(a)
print("The Sum is:",number.sum())
class digit:
    def __init__(self,x):
        self.x=x
    def get_sum(self):
        if self.x==0:
            return 0
        else:
            sum=0
            for i in range(0,self.x+1):
                sum=sum+i
            return sum
x=int(input("Enter The Number: "))
s=digit(x)
print(f"sum of {x} numbers will be: {s.get_sum()}")
#5.
class Name:
    def set_name(self,x):
        self.name=x #Class Attribute
    def get_name(self):
        return self.name
name=Name()
a=input("Enter The Name: ")
name.set_name(a)
r=int(input("Enter Roll: "))
name.roll=r #Instance Attribute
print("Name is:",name.get_name())
print("Roll No is:",name.roll)
#5a.
class Name:
    def __init__(self,x):
        self.name=x #Class Attribute
    def get_name(self):
        return self.name
a=input("Enter The Name: ")
name=Name(a)#Using Constructor
r=int(input("Enter Roll: "))
name.roll=r #Instance Attribute
print("Name is:",name.get_name())
print("Roll No is:",name.roll)
#6.
class Parent:
    def __init__(self):
        self.name="Abisekh Dey"
        print("This is Parent Class")
class Child(Parent):
        def __init__(self):
            super().__init__()
            print("This is Child Class")
            print(self.name)
child=Child()
#7.What is Self? 
#Self is the Instance of the Object which is present in the class
#Proof
#Method 1:
class Stu:
    def n(self,x):
        self.name=x
    def address(self):
        return id(self)
a=Stu()
a.n("Abisekh Dey")
print("Address of Object:",id(a))
print("Address of Self:",a.address())
print("Name is:",a.name)
#Method 2:
class Add:
    def address(self):
        print("Address of Self:",id(self))
x=Add()
x.address()
print("Address of Object:",id(x))
#Method 3:
class Id:
    def __init__(self):#Using Constructor
        print("Address of Self:",id(self))
x=Id()
print("Address of Object:",id(x))
#Method 4:
class Id:
    def __init__(self):#Using Constructor
        print("Address of Self:",id(self))
x=Id()
print("Address of Object:",id(x))
y=Id()
print("Address of Object:",id(y))# For this Object y; the Address of Self and the Address of Object y will be same but address will be different from the previous Object x 
#8a.
class Customer:
    def __init__(self,Name,Gender):#Class Constructor
        self.name=Name
        self.gender=Gender
def greet(customer):#This function is outside of the class and getting customer as parameter
    print(id(customer))#Printing the memory address of the parameter customer 
    #so the reference variable "cust" is copied at the place of "customer" parameter; cust is the reference variable contains the object address of Customer class
    #This means that customer inside the greet function is referencing the same object as cust outside the function. So customer and cust refer to the same instance of the Customer class.
    #Thats why cust and customer parameter both can access the real instance variable because customer is referencing the same instance of the Customer class that cust is referencing.
    print(id(cust))#Both customer and cust are pointing the same memory address; so cust and customer is the same reference variable of object of Customer class 
    if cust.gender=="male":
        print("Hello",customer.name,"Sir")
    else:
            print("Hello",customer.name,"Mam")
cust=Customer("Abisekh","male")#cust is the reference variable which contains the object address of Customer class or we can say cust is the instance object of Customer class 
print(id(cust))#Printing the address of the reference variable or instance object of Customer class which is defined by cust
greet(cust)#calling the greet function and passing the reference variable "cust" as an argument to the function 
#8b.
class Customer:
    def __init__(self,Name,Gender):
        self.name=Name
        self.gender=Gender
def greet(customer):
    print(id(customer))
    if cust.gender=="male":
        print("Hello",customer.name,"Sir")
    else:
            print("Hello",customer.name,"Mam")
cust=Customer("Abisekh","male")
customer=Customer("Abisekh","male")
print(id(cust))
greet(customer)
#9.
class Customer:
    def __init__(self,Name,Gender):
        self.name=Name
        self.gender=Gender
def greet(customer):
    print(id(customer))
    if cust.gender=="male":
        print("Hello",customer.name,"Sir")
    else:
            print("Hello",customer.name,"Mam")
    cust2=Customer("Pallabi","female")# This cust2 instance object is made inside of the function
    print(id(cust2))# This will print the memory address of cust2
    return cust2#This is returning the reference variable cust2 to the function call
cust=Customer("Abisekh","male")
print(id(cust))
new_cust=greet(cust)#cust2 is returned here and re assigned to new_cust; so now new_cust is referencing the same instance of the Customer class that cust2 is referencing.
print(id(new_cust))#It will print the memory location of new_cust which actually is the same as cust2 memory address; because new_cust is referencing the same instance of the Customer class that cust2 is referencing.
print(new_cust.name)#cust2 is assigned to new_cust so new_cust is referencing the same instance of the Customer class that cust2 is referencing
#cust2 is passing 2 arguments in the class Customer because of cust2 and new_cust is the same instance of the Customer class thats why new_cust can access the instance variable new_cust.name and new_cust.gender of Customer class
#10.
class Customer:
    def __init__(self, name):
        print('''
              id-1,id-7,id-8,id-9 Should be same!
              id-2,id-5,id-3,id-4,id-10 Should  be same!
              id-11,id-12 Should be same!
              id-13,id-14 Should be same!
              id-6 Will be different!
              ''')
        print("id-1", id(self))       # Print the memory address of the instance
        print("id-2", id(name))       # Print the memory address of the 'name' argument
        self.name = name
        print("id-3", id(self.name))   # Print the memory address of the 'name' instance variable
        print("id-4", id(name))        # Print the memory address of the 'name' argument

def greet(customer):
    print("id-8", id(cust))
    print("id-9", id(customer))
    print("id-10", id(customer.name))  # Print the memory address of the 'name' attribute of the 'customer' object
    customer.name = "Pallabi"        # Modify the 'name' attribute of the 'customer' object
    print("id-11", id(customer.name))  # Print the memory address of the modified 'name' attribute
    print("id-12", id("Pallabi"))      # Print the memory address of the string "Pallabi"
    print(customer.name)             # Print the value of the 'name' attribute
    print(cust.name)                 # Print the value of 'name' attribute of 'cust' object
    cust.name = "Avi"                # Try to modify 'name' attribute of 'cust' object (won't affect the class)
    print("id-13", id(cust.name))      # Print the memory address of the modified 'name' attribute
    print(customer.name)             # Print the value of the 'name' attribute
    print(cust.name)                 # Print the value of 'name' attribute of 'cust' object

cust = Customer("Abisekh")
print("id-5", id("Abisekh"))        # Print the memory address of the string "Abisekh"
print("id-6", id(Customer))          # Print the memory address of the Customer class
print("id-7", id(cust))              # Print the memory address of the 'cust' object
greet(cust)                         # Call the greet function with the 'cust' object as argument
print(cust.name)                    # Print the value of 'name' attribute of 'cust' object
print("id-14", id(cust.name))         # Print the memory address of the 'name' attribute of 'cust' object
#11.Predict Output
class ad:
    def __init__(self):
        print(id(self))
w=ad()
print(id(w))
print(id(ad))
#12.Predict Output
class cust:
    def __init__(self):
        print(id(self))
x=cust()
print(x)#x = cust() creates an instance of the cust class, and then print(x) prints out the representation of that instance, which includes the class name and the memory address where the instance is stored. 
#Here the memory address will be printed in hexa-decimal format but it is the same memory address which we can get by using print(id(x)) but print(id(x)) will print the address in decimal format
print(id(x))
#12.Predict Output
class x:
    def __init__(self,a):
        self.a=a
        print("id-1",id(self.a))#id-1 and id-2 will be same because list is mutable object which means we can change or modify list after the we create list;
        #thats why at time of creation of any list the memory address will be same after the modification of the list 
        self.a.append(67)
        print("id-2",id(self.a))
        print(self.a)
y=[12,23,34,45,56]
list=x(y)
print("id-3",id(list.a))
print(list.a)
#13.Predict Output
class Cust:
    def __init__(self,name,age):
        self.name=name
        self.age=age
c1=Cust("Abisekh",24)
c2=Cust("Pallabi",22)
c3=Cust("Avi",24)
list=[c1,c2,c3]#The List containing collection of Objects
for i in list:
    # print(i)#it will print the details of the object like under which class the object comes in and the memory address of the of the objects in hexadecimal
    print(i.name,i.age)#we have to mention the variable name of the class to access them
#14.Predict Output
class Cust:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def stu(self):
        print("My name is",self.name,"age",self.age)
c1=Cust("Abisekh",24)
c2=Cust("Pallabi",22)
c3=Cust("Avi",24)
list=[c1,c2,c3]#The List containing collection of Objects
for i in list:
    i.stu()
#15a.Static Variable/Class Variable
class stat:
    count=0#Static Variable/Class Variable
    def __init__(self):
        self.count=stat.count
        stat.count=stat.count+1
x1=stat()
print(x1.count)
print(stat.count)
x2=stat()
print(x2.count)
print(stat.count)
x3=stat()
print(x3.count)
print(stat.count)
#15b.Static Variable/Class Variable
class MyClass:
    static_var = 0  # This is a static variable
    
    def __init__(self, value):
        self.value = value
        
    def increment_static_var(self):
        MyClass.static_var += 1
        
    def display(self):
        print("Value:", self.value)
        print("Static variable:", MyClass.static_var)


# Creating instances of MyClass
obj1 = MyClass(10)
obj2 = MyClass(20)

# Accessing static variable
print("Static variable before increment:", MyClass.static_var)

# Incrementing static variable using instance method
obj1.increment_static_var()

# Accessing static variable after increment
print("Static variable after increment:", MyClass.static_var)

# Displaying values of objects
obj1.display()
obj2.display()

#16.Aggrigation 
# Here, the Customer class has an "has-a" relationship with the Address class. 
class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
        print("3",id(address))
        print("4",id(self.address))
class Address:
    def __init__(self,city,pincode,state):
        print("5",id(city))
        self.city=city
        print("6",id(self.city))
        self.pincode=pincode
        self.state=state
    def Change_address(self):
        self.city=input("Enter The city: ")
        self.pincode=int(input("Enter The Pincode: "))
        self.state=input("Enter The State: ")    
add=Address("Athpur",743128,"WB")
print("1",id(add))
print("2",id("Athpur"))
cust=Customer("Abisekh","Male",add)
print(cust.address.city)
print(cust.address.pincode)
print(cust.address.state)
print("My Name is:",cust.name,"Gender:",cust.gender,"Address:",cust.address.city,cust.address.pincode,cust.address.state)
cust.address.Change_address()
print("My Name is:",cust.name,"Gender:",cust.gender,"Address:",cust.address.city,cust.address.pincode,cust.address.state)
#16a.Aggrigtion
# Here, the Customer class has an "has-a" relationship with the Address class. 
class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
        print("3",id(address))
        print("4",id(self.address))
class Address:
    def __init__(self,city,pincode,state):
        print("5",id(city))
        self.city=city
        print("6",id(self.city))
        self.pincode=pincode
        self.state=state
    def Change_address(self,new_city,new_pin,new_state):
        self.city=new_city
        self.pincode=new_pin
        self.state=new_state  
add=Address("Athpur",743128,"WB")
print("1",id(add))
print("2",id("Athpur"))
cust=Customer("Abisekh","Male",add)
print(cust.address.city)
print(cust.address.pincode)
print(cust.address.state)
print("My Name is:",cust.name,"Gender:",cust.gender,"Address:",cust.address.city,cust.address.pincode,cust.address.state)
cust.address.Change_address("Kolkata",700001,"WB")
print("My Name is:",cust.name,"Gender:",cust.gender,"Address:",cust.address.city,cust.address.pincode,cust.address.state)
#16b.Aggrigtion
# Here, the Customer class has an "has-a" relationship with the Address class. 
class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
        print("3",id(address))
        print("4",id(self.address))
    def Edit_Profile(self):
        self.address.Change_address()
class Address:
    def __init__(self,city,pincode,state):
        print("5",id(city))
        self.city=city
        print("6",id(self.city))
        self.pincode=pincode
        self.state=state
    def Change_address(self):
        self.city=input("Enter The city: ")
        self.pincode=int(input("Enter The Pincode: "))
        self.state=input("Enter The State: ") 
add=Address("Athpur",743128,"WB")
print("1",id(add))
print("2",id("Athpur"))
cust=Customer("Abisekh","Male",add)
print(cust.address.city)
print(cust.address.pincode)
print(cust.address.state)
print("My Name is:",cust.name,"Gender:",cust.gender,"Address:",cust.address.city,cust.address.pincode,cust.address.state)
cust.Edit_Profile()
print("My Name is:",cust.name,"Gender:",cust.gender,"Address:",cust.address.city,cust.address.pincode,cust.address.state)
#16c.Aggrigtion
# Here, the Customer class has an "has-a" relationship with the Address class. 
class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
        print("3",id(address))
        print("4",id(self.address))
    def Edit_Profile(self):
        self.name=input("Enter The Name: ")
        self.address.Change_address()
class Address:
    def __init__(self,city,pincode,state):
        print("5",id(city))
        self.city=city
        print("6",id(self.city))
        self.pincode=pincode
        self.state=state
    def Change_address(self):
        self.city=input("Enter The city: ")
        self.pincode=int(input("Enter The Pincode: "))
        self.state=input("Enter The State: ") 
add=Address("Athpur",743128,"WB")
print("1",id(add))
print("2",id("Athpur"))
cust=Customer("Abisekh","Male",add)
print(cust.address.city)
print(cust.address.pincode)
print(cust.address.state)
print("My Name is:",cust.name,"Gender:",cust.gender,"Address:",cust.address.city,cust.address.pincode,cust.address.state)
cust.Edit_Profile()
print("My Name is:",cust.name,"Gender:",cust.gender,"Address:",cust.address.city,cust.address.pincode,cust.address.state)
#16d.Aggrigtion
class Customer:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
class Address:
    def __init__(self,city,pincode,state,details):
        self.city=city
        self.pincode=pincode
        self.state=state
        self.details=details
    def Change_address(self):
        self.city=input("Enter The city: ")
        self.pincode=int(input("Enter The Pincode: "))
        self.state=input("Enter The State: ")    

details=Customer("Abisekh","Male")
add=Address("Athpur",743128,"West Bengal",details)
print(f"My name is {add.details.name}, gender {add.details.gender},Address {add.city}, pin {add.pincode}, state {add.state}")
#16e.Aggrigtion
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving {self.make} {self.model}")
class Person:
    def __init__(self, name, car):
        self.name = name
        self.car = car

    def drive_car(self):
        print(f"{self.name} is driving...")
        self.car.drive()
# Creating an instance of Car
my_car = Car("Toyota", "Camry")

# Creating an instance of Person with a reference to the Car object
person = Person("John", my_car)

# Calling the drive_car method of Person, which internally calls the drive method of Car
person.drive_car()
#17.Inheritance
class User:
    def login(self):
        print("Log-in")
    def reg(self):
        print("Registration")
class Student(User):#Student class is the child class which is inheritating the property(such as methods or data-members or the constructor) of the parent class User
    #It means child Student class can use and access all properties(such as methods or data-members or the constructor) of its parent class User but the parent class User can not able to access the properties(such as methods or data-members or the constructor) of its child class Student
    def enroll(self):
        print("Enroll")
    def review(self):
        print("Review")
stu=Student()
#stu=User()#if I do this it will not work because the parent class User can not able to access the properties(such as methods or data-members or the constructor) of its child class Student
stu.enroll()
stu.login()
stu.reg()
stu.review()
#18.
class Vehicle:
    def __init__(self,type,brand,colour):
        self.type=type
        self.brand=brand
        self.colour=colour
class car(Vehicle):#car class don't have any constructor but it is the child class of the parent class Vehicle; so though car class don't have any constructor but it can use the constructor of it's parent class
    pass
x=car("Sedan","BMW","Brown")#passing 3 arguments to the constructor of car class
print("Brand of car:",x.brand,"Type of car:",x.type,"Colour of car:",x.colour)
#18a.
class Vehicle:
    def __init__(self, type, brand, colour):
        self.type = type
        self.brand = brand
        self.colour = colour

class Car(Vehicle):
    def __init__(self, type, brand, colour):
        super().__init__(type, brand, colour)  # Call parent class constructor
        if self.type == "Sedan" and self.brand == "BMW" and self.colour == "Brown":
            self.price = "Starting Price 2Cr"

# x = Vehicle("Sedan", "BMW", "Brown")
y = Car("Sedan", "BMW", "Brown")
print("Brand of car:", y.brand, "Type of car:", y.type, "Colour of car:", y.colour)
print(y.price)
print("Price of car:", getattr(y, 'price', 'Price not available'))  # Check if 'price' attribute exists, otherwise print default message
#19.
class Vehicle:
    def __init__(self,type,brand,colour):
        self.type=type
        self.__brand=brand
        self.colour=colour
class car(Vehicle):#car class don't have any constructor but it is the child class of the parent class Vehicle; so though car class don't have any constructor but it can use the constructor of it's parent class
    pass
x=car("Sedan","BMW","Brown")#passing 3 arguments to the constructor of car class
print("Brand of car:",x.brand,"Type of car:",x.type,"Colour of car:",x.colour)
#19a.
class Vehicle:
    def __init__(self,type,brand,colour):
        self.type=type
        self.__brand=brand
        self.colour=colour
    def Brand(self):
        return self.__brand#Method can access the private variable in side the class and return the private variable to the function call; in that case it will break the private property of the variable
class car(Vehicle):#car class don't have any constructor but it is the child class of the parent class Vehicle; so though car class don't have any constructor but it can use the constructor of it's parent class
    pass
x=car("Sedan","BMW","Brown")#passing 3 arguments to the constructor of car class
print("Brand of car:",x.Brand(),"Type of car:",x.type,"Colour of car:",x.colour)
#19b.
class Vehicle:
    def __init__(self,type,brand,colour):
        self.type=type
        self.__brand=brand
        self.colour=colour
    def __Brand(self):
        return self.__brand#Method can access the private variable in side the class and return the private variable to the function call; in that case it will break the private property of the variable
class car(Vehicle):#car class don't have any constructor but it is the child class of the parent class Vehicle; so though car class don't have any constructor but it can use the constructor of it's parent class
    pass
x=car("Sedan","BMW","Brown")#passing 3 arguments to the constructor of car class
print("Brand of car:",x.Brand(),"Type of car:",x.type,"Colour of car:",x.colour)#it will generate attribute error because the "Brand" method inside of the vehicle class is privte
######VVI######
#19c.
class X:
    def __init__(self,name):
        self.__name=name
        print(id(self.__name))
class Y(X):
    def __init__(self,name):
        super().__init__(name)
        self._X__name="Pallabi"
y=Y("Abisekh")
print(id(y._X__name))
print(y._X__name)
#This example defines two classes, X and Y. Y inherits from X. In the initialization of Y, after calling the superclass constructor with super().__init__(name), it directly modifies the attribute self._X__name (which is actually self.__name of class X) with "Pallabi". This demonstrates how we can access and modify a parent class's "private" attribute in a subclass.
#In 19c, Y inherits from X, and Y directly modifies the "private" attribute of X in its initialization.
#19d.
class X:
    def __init__(self,name):
        self.__name=name
        print(id(self.__name))
class Y:
    def __init__(self,name):#though name parameter getting an argument "Abisekh" but I is unused in the code
        self._X__name="Pallabi"#self._X__name is just a instance variable/attribute of Y class; it can't access private variable "self.__name" of X class because Y class is not inheritating X class 
y=Y("Abisekh")
print(id(y._X__name))
print(y._X__name)
#This example only defines two separate classes, X and Y, without any inheritance relationship. In the initialization of Y, it directly sets self._X__name = "Pallabi". However, since there's no inheritance involved, _X__name is not a private attribute of any parent class. It's just a regular attribute of Y.
#In 19d, there's no inheritance, and Y defines its own attribute _X__name, which is not related to any parent class's private attribute.
#20.Predict Output:
class Parent:
    def __init__(self,num):
        self.__num=num
    def get_num(self):
        return self.__num
class Child(Parent):
    def show(self):
        print("This is a Child Class")
x=Child(24)
print(x.get_num())
x.show()
#20a.Predict Output
class MyClass:
    def __init__(self):
        self.__private_var = "I am private"

    def get_private_var(self):
        return self.__private_var

obj = MyClass()
print(obj.get_private_var())  # This prints "I am private"
#In this example, get_private_var() is a method of the MyClass class, so it can access the private variable __private_var without any issues. 
# When get_private_var() is called from outside the class, it successfully returns the value of the private variable, demonstrating that accessing private variables via methods from outside the class does not raise an AttributeError.
#20b. Predict Output
class MyClass:
    def __init__(self):
        self.__private_var = "I am private"

    def __get_private_var(self):#The Method is private
        return self.__private_var

obj = MyClass()
print(obj.get_private_var())#this will generate attribute error
#21a.Predict Output
class MyClass:
    def __init__(self, value):
        self.instance_var = value  # Declaring an instance variable inside the constructor

    def get_var(self):
        return self.instance_var  # Returning the instance variable

obj = MyClass(10)
print(obj.instance_var)  # Accessing the instance variable directly
#21b.Predict Output
class MyClass:
    def set_var(self, value):
        self.instance_var = value  # Declaring an instance variable inside the method

    def get_var(self):
        return self.instance_var  # Accessing the instance variable

obj = MyClass()

# Trying to directly access instance_var before setting it
# print(obj.instance_var)  # This will raise an AttributeError because instance_var is not defined yet; so we have to call the method first

obj.set_var(10)  # Calling the method to set the instance variable

print(obj.instance_var)  # Accessing the instance variable directly after it has been set
#21c.Predict Output
class MyClass:
    def __init__(self, value):
        self.instance_var = value  # Declaring an instance variable inside the constructor

    def get_var(self):
        self.var = 12  # Initialize var inside the method
        # return self.var  # Returning the instance variable

obj = MyClass(10)
obj.get_var()  # Call the method to set the instance variable 'var'
print(obj.var)  # Accessing the instance variable directly after it has been set
#21d.Predict Output
class MyClass:
    def __init__(self, value):
        self.instance_var = value  # Declaring an instance variable inside the constructor

    def get_var(self):
        self.var = 12  # Initialize var inside the method
        return self.var  # Returning the instance variable

obj = MyClass(10)
print(obj.get_var())  # Accessing the instance variable directly after it has been set
#22a.Predict Output
class Parent:
    def __init__(self,num):
        self.__num=num
    def get_num(self):
        return self.__num
class Child(Parent):
    def __init__(self,val,num):#if The child class has the own consructor then to access the paarent class's constructor we have to use "super" function which is shown in 22b. code
        self.__val=val
    def get_val(self):
        return self.__val
a=Child(10,20)
print("Parent num:",a.get_num())#Child class can't access the Parent class's method or attribute in this case; so that it will generate attribute error 
print("Child num:",a.get_val())
#22b.Predict Output
class Parent:
    def __init__(self,num):
        self.__num=num
    def get_num(self):
        return self.__num
class Child(Parent):
    def __init__(self,val,num):
        super().__init__(num)
        self.__val=val
    def get_val(self):
        return self.__val
a=Child(10,20)
print("Parent num:",a.get_num())
print("Child num:",a.get_val())
#22c.Predict Output
class A:
    def __init__(self):
        self.num=100
    def disp1(self,x):#x is unused; since x is unused datatype of x doesn't matter
        print("Class A:",self.num)
class B(A):
    def disp2(self,y):#y is unused; since y is unused datatype of x doesn't matter
        print("Class B:",self.num)
obj=B()
obj.disp1(200)
obj.disp2("Abisekh")
#23.Polymorphism(Method Overriding)
class Vehicle:
    def __init__(self,type,brand,colour):
        self.type=type
        self.brand=brand
        self.colour=colour
    def Engine(self):
        self.engine="Diesel"
        return self.engine
class car(Vehicle):#car class don't have any constructor but it is the child class of the parent class Vehicle; so though car class don't have any constructor but it can use the constructor of it's parent class
    def Engine(self):
        self.engine="Petrol"
        return self.engine
x=car("Sedan","BMW","Brown")#passing 3 arguments to the constructor of car class
print("Brand of car:",x.brand,"Type of car:",x.type,"Colour of car:",x.colour)
print("Engine Type:",x.Engine())#both Vehicle Class and car Class have the method "Engine" but here I called Engine method for car Class
#24.Use of Super Keyword to access the method of parent class (Super Keyword can access only the methods and the constructor of the parent class)
class Vehicle:
    def __init__(self,type,brand,colour):
        self.type=type
        self.brand=brand
        self.colour=colour
    def Engine(self):
        self.engine="It Can be Diesel also"
        print(self.engine)
class car(Vehicle):#car class don't have any constructor but it is the child class of the parent class Vehicle; so though car class don't have any constructor but it can use the constructor of it's parent class
    def Engine(self):
        self.engine="It Can be Petrol"
        print(self.engine)#First it will excecute the printing statement of "Engine" method of car class then it will be moved to the "Engine" method of Vehicle class using super function
        super().Engine()
x=car("Sedan","BMW","Brown")#passing 3 arguments to the constructor of car class
print("Brand of car:",x.brand,"Type of car:",x.type,"Colour of car:",x.colour)
x.Engine()
#24a.Using Super keyword to access the constructor of parent class
class Phone:
    def __init__(self,price,brand,camera):
        self.__price=price
        self.brand=brand
        self.camera=camera
class Smartphone(Phone):
    def __init__(self,price,brand,camera,os,ram):
        super(). __init__(price,brand,camera)
        self.os=os
        self.ram=ram
phone=Smartphone(50000,"Samsung","200 mp","Android",16)
print(phone.brand)#Accessing the instance variable of parent class
print(phone.os)#Accessing the instance variable of child class
#24b.Predict Output
class Parent:
    def __init__(self,num):
        self.__num=num
    def get_num(self):
        return self.__num
class Child(Parent):
    def __init__(self,num,val):
        super(). __init__(num)
        self.__val=val
    def get_val(self):
        return self.__val
child=Child(10,20)
print(child.get_num())
print(child.get_val())
#24c.Predict Output
class Parent:
    def __init__(self,num):
        self.__num=num
    def get_num(self):
        print(self.__num)
class Child(Parent):
    def __init__(self,num,val):
        super(). __init__(num)
        self.__val=val
    def get_val(self):
        print(self.__val)
child=Child(10,20)
child.get_num()
child.get_val()
#24d. Predict Output
class Parent:
    def __init__(self):
        self.num=10
class Child(Parent):
    def __init__(self):
        self.var=20
obj=Child()
print(obj.num)#It will raise Attribute Error
#24e. Predict Output
class Parent:
    def __init__(self):
        self.num=10
class Child(Parent):
    def __init__(self):
        super().__init__()#The parent class constructor has no parameter in it; so we don't need to pass any parameter to call parent constructor using super keyword
        self.var=20
    def get_var(self):
        print(self.num)#Accessing the Parent class instance variable inside of the Child class directly; same thing is done is code 18a
        print(self.var)
obj=Child()
print(obj.num)
obj.get_var()
#24f. Predict Output
class Parent:
    def __init__(self):
        self.__num=10
    def disp(self):
        print("Parent",self.__num)
class Child(Parent):
    def __init__(self):
        super().__init__()#The parent class constructor has no parameter in it; so we don't need to pass any parameter to call parent constructor using super keyword
        self.__var=20
    def disp(self):
        print("Child",self.__var)
obje=Parent()
obje.disp()#disp method is called for Parent class 
obj=Child()
obj.disp()#disp method is called for Child class
#if the object of the Parent class not build then due to "Method Overriding" the child class object calls the disp method for its own class
#24g. Predict Output
class Parent:
    def __init__(self):
        self.__num=10
    def disp(self):
        print("Parent",self.__num)
class Child(Parent):
    def __init__(self):
        super().__init__()#The parent class constructor has no parameter in it; so we don't need to pass any parameter to call parent constructor using super keyword
        self.__var=20
    def disp(self):
        print("Child",self.__var)
        super().disp()#Here The super keyword accessing the disp method of parent class
obje=Parent()
obje.disp()#disp method is called for Parent class 
obj=Child()
obj.disp()#disp method is called for Child class
#25.Single-Level Inheritance
class Phone:
    def __init__(self,price,brand,camera):
        print(id(self))
        self.price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("Buying a Phone")
    def return_phone(self):
        print("Returning a Phone")
class Smartphone(Phone):
    pass
Smartphone(20000,"Samsung","200 mp").buy()#I can make objects like this also and also can call any method 
Smartphone(20000,"Samsung","200 mp").return_phone()
print(Smartphone(20000,"Samsung","200 mp").camera)
print(id(Smartphone(20000,"Samsung","200 mp")))
#26a.Multi-Level Inheritance
class Product:
    def __init__(self,os,ram):
        self.os=os
        self.ram=ram
class Phone(Product):
    def __init__(self,price,brand,camera,os,ram):
        super(). __init__(os,ram)
        self.price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("Buying a Phone")
    def return_phone(self):
        print("Returning a Phone")
class Smartphone(Phone):
    pass
phone=Smartphone(20000,"Samsung","200 mp","Android",16)
print(phone.os)
print(phone.camera)
phone.buy()
#26b.Multi-Level Inheritance
class A:
    def __init__(self):
        print("Constructor of A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Constructor of B")

class C(B):
    def __init__(self):
        super().__init__()
        print("Constructor of C")
obj=C()
#27.Hierarchical Inheritance (1 Parent class Multiple child class)
class Phone:
    def __init__(self,price,brand,camera):
        self.price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("Buying a Phone")
    def return_phone(self):
        print("Returning a Phone")
class Smartphone(Phone):
    pass
class Featurephone(Phone):
    pass
Smartphone(20000,"Samsung","200 mp").buy()#Object for child 1
Featurephone(20000,"Samsung","200 mp").return_phone()#Object for child 2
print(Smartphone(20000,"Samsung","200 mp").camera)
print(Featurephone(20000,"Samsung","200 mp").price)
#28a.Multiple Inheritance
class Phone:
    def __init__(self,price,brand,camera):
        self.price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("Buying a Phone")
class Product:
    def __init__(self):
        print(id(self))
        self.ram=12 
    def return_phone(self):
        print(id(self))
        print("Returning a Phone")
class Smartphone(Phone,Product):
    pass#Here the smartphone class has no constructor so it will automatically find if there is a constructor in the parent class from which smartphone class is inheritating 
#but if the child is inheritating with multiple classes then it will find the constructor in the parent class which is comming first in order
#for example: class Smartphone(Phone,Product) in this class there are multiple classes("Phone Class" & "Product Class") from which smartphone class is inheritating but it will find the constructor in order which class is in the first position; That is here Phone Class
#If any Constructor is Found in the Phone Class then the arguments will be set in the instance variable of that constructor; once the values are set in constructor then it will not find any other constructor is present in other class or not
#If Phone don't have any constructor then it will automatically move to the next Class which is here Product
#Since here Phone Claass has a constructor then it will not check if there is a constructor in the Product class or not since it will not check if there is a constructor in the Product class or not then the instance can not access the variable inside of the constructor in the Product Class 
#To access all the Contructors of all the class we have to use Super keyword
s=Smartphone(20000,"Samsung","200 mp")
s.buy()
s.return_phone()#Instance can access all the Methods if the Constructor is defined or not
print(s.brand)
print(id(s))
print(s.ram)#In this Code s.ram is not accessable because it is in the constructor of Product Class and the instance will not visit the constructor of the Product Class [Reason Mentioned just above]; So it will generate Attribute error
#28b.Multiple Inheritance
class Phone:
    def buy(self):
        print("Buying a Phone")

class Product:
    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera
        self.ram = 12
        print(id(self))
    def return_phone(self):
        print(id(self))
        print("Returning a Phone")

class Smartphone(Phone, Product):#Here Phone Class is present first in the order but it doesn't have the constructor then it will atomatically check PRoduct Class for the constructor 
    pass

s = Smartphone(20000, "Samsung", "200 mp")
s.buy()
s.return_phone()#Instance can access all the Methods if the Constructor is defined or not
print(s.brand)
print(id(s))  # Output: id of the Smartphone instance
print(s.ram)
#28c.Multiple Inheritance
class Phone:
    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

class Product:
    def __init__(self):
        print(id(self))
        self.ram = 12

    def return_phone(self):
        print("Returning a Phone")

class Smartphone(Phone, Product):
    def __init__(self, price, brand, camera):
        Phone.__init__(self,price, brand, camera)  # Call Phone's constructor
        Product.__init__(self)  # Call Product's constructor

s = Smartphone(20000, "Samsung", "200 mp")
s.buy()
s.return_phone()#Instance can access all the Methods if the Constructor is defined or not
print(s.brand)
print(id(s))  # Output: id of the Smartphone instance
print(s.ram)
#28d.Multiple Inheritance
class Phone:
    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

class Product:
    def __init__(self):
        print(id(self))
        self.ram = 12

    def return_phone(self):
        print("Returning a Phone")

class Smartphone(Phone, Product):
    def __init__(self, price, brand, camera):
        super().__init__(price, brand, camera)  # Call Phone's constructor
        Product.__init__(self)  # Call Product's constructor

s = Smartphone(20000, "Samsung", "200 mp")
s.buy()
s.return_phone()#Instance can access all the Methods if the Constructor is defined or not
print(s.brand)
print(id(s))  # Output: id of the Smartphone instance
print(s.ram)
#29.Predict Output (Find which buy method will execute)
class Phone:
    def __init__(self,price,brand,camera):
        self.price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("Buying a Phone")
class Product:
    def buy(self):
        print(id(self))
        print("Returning a Phone")
class Smartphone(Phone,Product):#Since Phone class is Present first in the order then buy method will execute for the Class which is present first in order; which is here Phone. This is called MRO [Method Resolution Order] 
    pass
s = Smartphone(20000, "Samsung", "200 mp")
s.buy()
#30a. Predict Output
class A:
    def m1(self):
        return 20
class B(A):
    def m1(self):
        return 30
    def m2(self):
        return 40
class C(B):
    def m2(self):
        return 20
obj1=A()
obj2=B()
obj3=C()
print(obj1.m1()+obj3.m1()+obj3.m2())
#30b. Predict Output
class A:
    def m1(self):
        return 20
class B(A):
    def m2(self):
        return 30
    def m3(self):
        return 40
class C(B):
    def m4(self):
        return 20
obj3=C()
print(obj3.m1()+obj3.m2()+obj3.m4())
#Class C inherits from class B, which inherits from class A. So, class C has access to all methods defined in both A and B.
#31a. Predict Output
#######V.V.I.#######
class A:
    def m1(self):
        return 20
class B(A):
    def m1(self):
        val=super().m1()+30#This Super keyword moves to the method "m1" of class A;and takes the return value of the method "m1" of class A and then adds +30 with the value; then returns the final value to the class C
        return val
class C(B):
    def m1(self):
        val=super().m1()+20#This Super keyword moves to the method "m1" of class B; Taking the return value of Class B then adds +20 with the value; then returns the final value to the method call and prints it
        return val
obj3=C()
print(obj3.m1())
#31b. Predict Output
class A:
    def m1(self):
        return 20
class B(A):
    def m1(self):
        val=super().m1()+30
        return val
class C(B):
    def m1(self):
        val=self.m1()+20#This is recursively calling the same method in finite times because this recurssive method don't have any base case; thats why it will execute in finite times and will generate error
        return val
obj3=C()
print(obj3.m1())
#32.Polymorphism (Method Overloading)
class geometry:
    def area(self, a, b=0):
        if b == 0:
            print("Circle Area:", 3.14 * a**2)  # Calculates area of a circle
        elif a == b:
            print("Square Area:", a**2)  # Calculates area of a square
        else:
            print("Rectangle Area:", a * b)  # Calculates area of a rectangle
#Here in the code the same method is calculating Circle area , Square area , Rectangle area depending on the arguments is passed in the method calling; thats why its called Method Overloading
obj = geometry()

obj.area(2, 5)  
obj.area(2,2)    
obj.area(2)       
#33.Polymorphism (OPerator Overloading)
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the addition operator (+)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Overloading the subtraction operator (-)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # Overloading the multiplication operator (*)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # Overloading the equality operator (==)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Overloading the string representation operator (__str__)
    def __str__(self):
        return f"({self.x}, {self.y})"

# Creating two Vector objects
v1 = Vector(1, 2)
v2 = Vector(3, 4)

# Testing addition (+) operator overloading
v3 = v1 + v2
print("v1 + v2 =", v3)  # Output: (4, 6)

# Testing subtraction (-) operator overloading
v4 = v2 - v1
print("v2 - v1 =", v4)  # Output: (2, 2)

# Testing multiplication (*) operator overloading
v5 = v1 * 2
print("v1 * 2 =", v5)  # Output: (2, 4)

# Testing equality (==) operator overloading
print("v1 == v2 ?", v1 == v2)  # Output: False
#34. Example of Abstract Class in Python
from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    
    def make_sound(self):
        return "Meow!"

# Instantiate the subclasses
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!
#Important
#Given an array arr. The task is to find and return the maximum product possible with the subset of elements present in the array.
#case 1: If the array contains only one element, return that element.
#case 2: If there are no negative numbers and no zeros, the product of all elements is the maximum product.
#case 3: If there are zeros and the number of negative numbers is even, multiply all non-zero elements.
#case 4: If the number of negative numbers is odd, exclude the negative number with the smallest absolute value and multiply the rest of the non-zero elements.
class Solution:
    def findProduct(self,arr):
        x=1
        for i in arr:
            x=x*i
        return x
    def findMaxProduct(self, arr):
        if len(arr)==1:
            return arr[0]
        else:
            count=0
            for i in arr:
                if i!=0 and i>0:
                    count+=1
            if count==len(arr):
                x=self.findProduct(arr)
                return x
            else:
                no_of_zeros=0
                
                no_of_negetive=0
                negetive_element=[]
                element=[]
                for i in arr:
                    if i==0:
                        no_of_zeros+=1
                    elif i<0:
                        no_of_negetive+=1
                        negetive_element.append(i)
                        element.append(i)
                    else:
                        element.append(i)
                        
                if no_of_zeros%2==0 and no_of_negetive%2==0:
                    x=self.findProduct(element)
                    return x
                elif no_of_negetive%2==0:
                    x=self.findProduct(element)
                    return x
                elif no_of_negetive%2!=0:    
                    smallest_number=max(negetive_element)
                    element.remove(smallest_number)
                    print(element)
                    if element==[]:
                        return 0
                    else:
                        x=self.findProduct(element)
                        return x                    
arr=[-1,-1,-2,3,4]
sol=Solution()
print(sol.findMaxProduct(arr))