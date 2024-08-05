#List Functions:
#1.len(iterable):
#Returns the number of items in the iterable.
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(length)  # Output: 5
#List Methods:
#2.list.append(x):
#Adds an element x to the end of the list.
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
#3.list.extend(iterable):
#Extends the list by appending elements from the iterable.
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]
#4.list.insert(i, x):
#Inserts an element x at the specified index i.
my_list = [1, 2, 3]
my_list.insert(1, 10)
print(my_list)  # Output: [1, 10, 2, 3]
#5.list.remove(x):
#Removes the first occurrence of element x from the list.
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]
#6.list.pop([i]):
#Removes and returns the item at the specified index i. If no index is provided, it removes and returns the last item.
my_list = [1, 2, 3]
popped_item = my_list.pop(1)
print(popped_item)  # Output: 2
#7.list.clear():
#Removes all items from the list.
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []
#8.list.index(x[, start[, end]]):
#Returns the index of the first occurrence of element x. Raises a ValueError if x is not found.
my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)  # Output: 1
#9.list.count(x):
#Returns the number of occurrences of element x in the list.
my_list = [1, 2, 3, 2]
count = my_list.count(2)
print(count)  # Output: 2
#10.list.sort(key=None, reverse=False):
#Sorts the items of the list in place.
my_list = [3, 1, 4, 1, 5, 9, 2]
my_list.sort()
print(my_list)  # Output: [1, 1, 2, 3, 4, 5, 9]
#11.list.reverse():
#Reverses the elements of the list in place.
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]
#12.list.copy():
#Returns a shallow copy of the list.
my_list = [1, 2, 3]
copy_list = my_list.copy()
print(copy_list)  # Output: [1, 2, 3]
#13.list.__getitem__(i) (Indexing):
#Returns the element at index i.
my_list = [1, 2, 3]
element = my_list[1]
print(element)  # Output: 2
#14.list.__setitem__(i, x) (Assignment):
#Sets the element at index i to the value x.
my_list = [1, 2, 3]
my_list[1] = 10
print(my_list)  # Output: [1, 10, 3]
#15.list.__delitem__(i) (Deletion):
#Deletes the element at index i.
my_list = [1, 2, 3]
del my_list[1]
print(my_list)  # Output: [1, 3]
#16.list.__contains__(x) (Membership):
#Returns True if the element x is in the list, False otherwise.
my_list = [1, 2, 3]
contains = 2 in my_list
print(contains)  # Output: True
#17.Find Sum of all numbers in list
x=[12,23,34,45,56]
print("Sum is:",sum(x))
#18.Find The Greatest number in list
numbers = [10, 5, 20, 15, 8]
greatest_number = max(numbers)
print("The greatest number is:", greatest_number)
#19.Find The Greatest number in list
numbers = [10, 5, 20, 15, 8]
smallest_number = min(numbers)
print("The smallest number is:", smallest_number)
#20.Predict Output
x=[12,23,34,45,56]
y=["Red","Blue","Green"]
print("Maximum Number is:",max(x))
print("Minimum Number is:",min(x))
print("Maximum Number is:",max(y,key=len))
print("Minimum Number is:",min(y,key=len))