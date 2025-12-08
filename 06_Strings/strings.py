#strings are surrounded by single quotation or double quotation marks 
name = "Kumar"
print(name)

#multi-line strings
story = '''This is a multi-line 
string. Let's go to another line.
Now one more line'''
print(story)

#How to access the string 
name = "This is a string"
print(name[1]) #index started with 0, so 1 is nothing but h

#loop through letters in the word "Rama"
for i in "Rama":
    print(i)

#how to find the length of the string 
#len() finction gives us the length of a string
first_name = "Vinod"
print(len(first_name))

#how to check, if the a specific string is present or not?
sampleText = "Never stop learning in the life to move forward"
print("stop" in sampleText) #this will return True or Flase 


sampleText = "Never stop learning in the life to move forward"
if("money" in sampleText):
    print("yes, It is present")
else:
    print("it's not available")
    
#----------------






