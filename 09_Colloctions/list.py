#list are used to store multiple items in a single variable.
# Lists are ordered, changeable, and allow duplicate values.
# Lists are defined by placing items inside square brackets [].
# Example usage:
my_list = [1, 2, 3, "apple", "banana", True, 3.14]
print(my_list)  # Output: [1, 2, 3, 'apple', 'banana', True, 3.14]

my_list1 = [501, 502, 503, "Ramu", "Somu", "Krishan", 80.5, 90.5, 100.5]

#How to access elements in a list
print(my_list1) # Output: [501, 502, 503, 'Ramu', 'Somu', 'Krishan', 80.5, 90.5, 100.5]
print(my_list1[3]) # Output: Ramu
print(my_list1[-1]) # Output: 100.5 
print(my_list1[4]) # Output: Somu
print(my_list1[6]) # Output: 80.5
print(my_list1[0:4]) # Output: [501, 502, 503, 'Ramu']
print(my_list1[2:]) # Output: [503, 'Ramu', 'Somu', 'Krishan', 80.5, 90.5, 100.5]
print(my_list1[:5]) # Output: [501, 502, 503, 'Ramu', 'Somu']
print(my_list1[-4:-1]) # Output: ['Krishan', 80.5, 90.5]   

#inserting elements in a list
my_list1.insert(0, "List") #Insert() method inserts an element at the specified position
print(my_list1)

my_list1.append(1000) #append() method adds an element at the end of the list
print(my_list1)

my_list1.extend(["Item50", 2000]) #extend() method adds multiple elements at the end of the list
print(my_list1)

#Removing elements from a list
my_list1.remove("Item50") #remove() method removes the specified element from the list
print(my_list1)

my_list1.pop() #pop() method removes the last element from the list
print(my_list1)

my_list1.pop(5) #pop() method removes the element at the specified position
print(my_list1)

del my_list1[0] #del keyword removes the element at the specified position
print(my_list1)

#Clearing the list
my_list1.clear() #clear() method removes all elements from the list
print(my_list1)



#For loop to iterate through a list
fruits = ["apple", "banana", "cherry"]
print(fruits)
for i in fruits:
    print(i)

print("-----")   
#Looping through the index numbers
for i in range(len(fruits)):
    print(fruits[i])

print
#list comprehension
list = ["English", "Maths", "Science", "History"
        , "Geography", "Computer"]
newlist = []
for i in list:
    if "o" in i:
        newlist.append(i)
print(newlist)

print("-----")
#Sorting a list
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort() #sort() method sorts the list in ascending order
print(numbers)

numbers.sort(reverse=True) #sort() method sorts the list in descending order
print(numbers)

#Copying a list
myList = ["Auto", "Bike", "Bus", "Train"]
newAutoList = myList.copy() #copy() method copies the listprint(newAutoList)
print(newAutoList)

print("-----")
#Joining two lists
list1=["Candy", "Chocolate", "Ice-cream"]
list2=["Juice", "Soda", "Water"]
list3 = list1 + list2
print(list3)
