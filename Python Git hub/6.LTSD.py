#1.Iplementation of User Defined List Containing different Datatypes in it
n=int(input("Enter The size of The List: "))#Assuming n=6
x=[int(input(f"{i+1}.Enter The Element of List[{i}]: "))for i in range(n-3)]
for i in range(n-3,n-2):
    print("Tuple Input")
    y=tuple(input(f"{i+1}.Enter The element of The Character Tuple[{i}]: ")for i in range(n))
    sub_y=tuple(int(input(f"{i+1}.Enter The Element of Integer Sub Tuple[{i}]: "))for i in range(n))
    lsub_y=list(float(input(f"{i+1}.Enter The Element of Float List[{i}]: "))for i in range(n))
    sub_y=sub_y+(lsub_y,)
    y=y+(sub_y,)
    x.append(y)
for i in range(n-2,n-1):
    print("Set Input")
    z={input(f"{i+1}.Enter The Element of Character Set[{i}]: ")for i in range(n)}
    x.append(z)
for i in range(n-1,n):
    print("List Input")
    a=[input(f"{i+1}.Enter The Element of Character List[{i}]: ")for i in range(n-3)]
    b=[int(input(f"{i+1}.Enter The Element of Integer List[{i}]: "))for i in range(n)]
    a.append(b)
    x.append(a)
print(x)

print("Final List:")
print("Integers:", x[:n-3])#It will Print x[0] to x[n-3] items 
print("Tuples:", x[n-3])
print("Sets:", x[n-2])
print("Lists:", x[n-1])

#1a.Iplementation of User Defined List Containing different Datatypes in it
n=int(input("Enter The size of The List: "))#Assuming n=6
x=[int(input(f"{i+1}.Enter The Element of List[{i}]: "))for i in range(n)]

print("Tuple Input")
y=tuple(input(f"{i+1}.Enter The element of The Character Tuple[{i}]: ")for i in range(n))
sub_y=tuple(int(input(f"{i+1}.Enter The Element of Integer Sub Tuple[{i}]: "))for i in range(n))
lsub_y=list(float(input(f"{i+1}.Enter The Element of Float List[{i}]: "))for i in range(n))
sub_y=sub_y+(lsub_y,)
y=y+(sub_y,)
x.append(y)

print("Set Input")
z={input(f"{i+1}.Enter The Element of Character Set[{i}]: ")for i in range(n)}
x.append(z)

print("List Input")
a=[input(f"{i+1}.Enter The Element of Character List[{i}]: ")for i in range(n)]
b=[int(input(f"{i+1}.Enter The Element of Integer List[{i}]: "))for i in range(n)]
a.append(b)
x.append(a)
print(x)
print(len(x))

print("Final List:")
print("Integers:", x[:n])#It will Print x[0] to x[n] items 
print("Tuples:", x[n:n+1])
print("Sets:", x[n+1:n+2])
print("Lists:", x[n+2:n+3])

#2.Iplementation of User Defined Tuple Containing different Datatypes in it
n=int(input("Enter The size of The List: "))#Assuming n=6
x=tuple(int(input(f"{i+1}.Enter The Element of List[{i}]: "))for i in range(n-3))
for i in range(n-3,n-2):
    print("Tuple Input")
    y=tuple(input(f"{i+1}.Enter The element of The Character Tuple[{i}]: ")for i in range(n))
    sub_y=tuple(int(input(f"{i+1}.Enter The Element of Integer Sub Tuple[{i}]: "))for i in range(n))
    lsub_y=list(float(input(f"{i+1}.Enter The Element of Float List[{i}]: "))for i in range(n))
    sub_y=sub_y+(lsub_y,)
    y=y+(sub_y,)
    x=x+y
for i in range(n-2,n-1):
    print("Set Input")
    z={input(f"{i+1}.Enter The Element of Character Set[{i}]: ")for i in range(n)}
    x=x+(z,)
for i in range(n-1,n):
    print("List Input")
    a=[input(f"{i+1}.Enter The Element of Character List[{i}]: ")for i in range(n-3)]
    b=[int(input(f"{i+1}.Enter The Element of Integer List[{i}]: "))for i in range(n)]
    a.append(b)
    x+=(a,)
print(x)

print("Final Tuple:")
print("Integers:", x[:n-3])#It will Print x[0] to x[n-3] items 
print("Tuples:", x[n-3])
print("Sets:", x[n-2])
print("Lists:", x[n-1])

#3.Iplementation of User Defined Set Containing different Datatypes in it(Except Unhashable Datatype like list and set)
n=int(input("Enter The size of The List: "))#Assuming n=6
x={int(input(f"{i+1}.Enter The Element of List[{i}]: "))for i in range(n)}

print("Tuple Input")
y=tuple(input(f"{i+1}.Enter The element of The Character Tuple[{i}]: ")for i in range(n))
sub_y=tuple(int(input(f"{i+1}.Enter The Element of Integer Sub Tuple[{i}]: "))for i in range(n))
y=y+(sub_y,)
x.add(y)#x.update((y,)) This will generate same as this x.add(y)

print("Set Input")
z={input(f"{i+1}.Enter The Element of Character Set[{i}]: ")for i in range(n)}
x.update(z)

print("List Input")
a=[input(f"{i+1}.Enter The Element of Character List[{i}]: ")for i in range(n)]
x.update(a)
print(x)
print(len(x))