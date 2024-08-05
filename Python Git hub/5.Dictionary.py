#1.Create a Dictionary in python
#Foramt :name of the Dictionary={key:value}
number={"Abisekh Dey" : 8617244589,
    "Pallabi Mondal" : 6289731215,
    "Amita Dey" : 9748188514,
}
print(number)
print(type(number))
print(len(number))
#1a.
student={
    "name":"Abisekh",
    "roll":17632322013,
    "stream":"ECE",
}
print(student)
#2.Access Elements of Dictionary to get the values of the keys of the dictionary
number={
    "Abisekh Dey" : 8617244589,
    "Pallabi Mondal" : 6289731215,
    "Amita Dey" : 9748188514,
}
print(number["Abisekh Dey"],number["Pallabi Mondal"],number["Amita Dey"])
#3.Access Elements of Dictionary using get() function to get the values of the keys of the dictionary
#Format : Dictionary name.get(key)
number={
    "Abisekh Dey" : 8617244589,
    "Pallabi Mondal" : 6289731215,
    "Amita Dey" : 9748188514,
}
print(number.get("Abisekh Dey"),number.get("Pallabi Mondal"),number.get("Amita Dey"))
#4.Print the Keys of the dictionary using keys() function and values using values() function
#Format : Dictionary name.keys()
number={
    "Abisekh Dey" : 8617244589,
    "Pallabi Mondal" : 6289731215,
    "Amita Dey" : 9748188514,
}
print(number.keys())
print(number.values())
#5.Update Values of Dictionary
number={"Abisekh Dey" : 8617244589,
    "Pallabi Mondal" : 6289731215,
    "Amita Dey" : 9748188514,
}
number["Abisekh Dey"]=123
number["Pallabi Mondal"]=456
number["Amita Dey"]=789
print(number)
#6.Add Keys in Dictionary
number={"Abisekh Dey" : 8617244589,
    "Pallabi Mondal" : 6289731215,
    "Amita Dey" : 9748188514,
}
number["Babla Dey"]=7003105772#New Key
print(number)
#7.Add Sub-Dictionry in Dictionary using update() function
#Format : Dictionary name.pop(New Dictionary)
number={"Abisekh Dey" : 8617244589,
    "Pallabi Mondal" : 6289731215,
    "Amita Dey" : 9748188514,
}
more_numbers={#New Dictionary
    "a":123,
    "b":456,
    "c":789,
}
number.update(more_numbers)
print(number)
#8.Remove Key from Dictionary using pop() function
#Format : Dictionary name.pop(key)
number={"Abisekh Dey" : 8617244589,
    "Pallabi Mondal" : 6289731215,
    "Amita Dey" : 9748188514,
}
number.pop("Amita Dey")
print(number)
#9.Remove last Key from Dictionary using popitem() function
#Format : Dictionary name.popitem()
number={"Abisekh Dey" : 8617244589,
    "Pallabi Mondal" : 6289731215,
    "Amita Dey" : 9748188514,
}
number.popitem()#Removes last added key in the dictionary
print(number)
#10.Delete all Keys of Dictionary or Clear Whole Dictionary
number={"Abisekh Dey" : 8617244589,
    "Pallabi Mondal" : 6289731215,
    "Amita Dey" : 9748188514,
}
number.clear()#Removes all keys of the dictionary
print(number)
#11.Printing only Values of keys present in Dictionary using For Loop
number={"Abisekh Dey" : 8617244589,
    "Pallabi Mondal" : 6289731215,
    "Amita Dey" : 9748188514,
}
for i in number:
    print(i)# in general when we write loop like this we mean we just traverse the loop element wise not index wise;
    #but in case of dictionary where elements are the keys itself and each keys have an individual value in the dictionary;
    #so if I write only this print(i) it will print the elements only which is keys here but if we want to print the values of each keys we have to mention print(number[i]) 
for i in number:
    print(number[i])
#12.Printing both Keys and Values present in Dictionary using For Loop using items() function
number={"Abisekh Dey" : 8617244589,
    "Pallabi Mondal" : 6289731215,
    "Amita Dey" : 9748188514,
}
for i in number.items():
    print(i)
for i,j in number.items():# in this case i accesses the keys and j accesses the values of corresponding keys
    print(i,j)
#13.Printing of Nested Dictionaries in a single dictionary
number={
    "number>10" : {
        "a":20,
        "b":40,
        "c":80,
    },
    "number<10" : {
        "x":2,
        "y":4,
        "z":8,
    }
}
print(number["number>10"],number["number<10"],number["number>10"]["c"],number["number<10"]["y"])
#14.Print Sum of Values of Keys present in Dictionary
number={"a":100,"b":200,"c":300}
print("Sum of The Values Are:",number["a"]+number["b"]+number["c"])
print("Sum of The Values Are:",sum(number.values()))
#15.
x=input("Enter The String: ")
n=int(input("Enter The value of n: "))
alpha=[chr(i) for i in range(ord("a"),ord("a")+26)]
reverse_alpha=list(reversed(alpha))
numbers=dict(zip(alpha,reverse_alpha))
#zip(alpha, reverse_alpha) pairs corresponding elements from alpha and reverse_alpha together.
#dict(...) creates a dictionary where each character from alpha is mapped to its corresponding character in reverse_alpha. This dictionary (numbers) represents the mapping of each alphabet character to its reversed counterpart.
prefix=x[0:n-1]
suffix=x[n-1:len(x)]
result=""
for i in range(0,len(suffix)):
    result=result+numbers[suffix[i]]#numbers[suffix[i]] finds the reversed counterpart of the current character using the numbers dictionary.
final_result=prefix+result
print(final_result)
#16a.Implementation of User Defined Dictionary
n=int(input("Enter The Size of The Dictionary: "))
d={input(f"{i+1}.Enter The Key: "):int(input(f"{i+1}.Enter The Value of Dictionary: "))for i in range(n)}
print(d)
#16b.Implementation of User Defined Dictionary
n=int(input("Enter The Size of The Dictionary: "))
d=dict((input(f"{i+1}.Enter The Key: "),int(input(f"{i+1}.Enter The Value of Dictionary: ")))for i in range(n))
print(d)
#16c.Implementation of User Defined Dictionary
n=int(input("Enter The Size of The Dictionary: "))
d={}
for i in range(n):
    key=input(f"{i+1}.Enter The Key: ")
    value=int(input(f"{i+1}.Enter The Value of Dictionary: "))
    d[key]=value
print(d)
#16d.Implementation of User Defined Dictionary
n=int(input("Enter The Size of The Dictionary: "))
d={}
i=0
while i<n:
    key=input(f"{i+1}.Enter The Key: ")
    value=int(input(f"{i+1}.Enter The Value of Dictionary: "))
    d[key]=value
    i+=1
print(d)