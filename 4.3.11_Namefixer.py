#You've been sent a list of names. Unfortunately, the names
#come in two different formats:
#
#First Middle Last
#Last, First Middle
#
#You want the entire list to be the same. For this problem,
#we'll say you want the entire list to be First Middle Last.
#
#Write a function called name_fixer. name_fixer should take
#as input the list of strings. You may assume that every string
#will match one of the two formats above: either First Middle Last
#or Last, First Middle. 
#
#name_fixer should return a list of names all structured as
#First Middle Last. If the name was already structured as
#First Middle Last, it should remain unchanged. If it was
#structured as Last, First Middle, then Last should be moved
#to the end after a space and the comma removed.
#
#The names should appear in the same order as the original list.
#
#For example:
#
#name_list = ["David Andrew Joyner", "Hart, Melissa Joan", "Cyrus, Billy Ray"]
#name_fixer(name_list) -> ["David Andrew Joyner", "Melissa Joan Hart", "Billy Ray Cyrus"]


#Add your code here!
def name_fixer(list_of_names):
    new_list = []
    for i in list_of_names:
        if "," in i:
            x = i.rfind(",")
            y = i[:x]
            i = i[x+2:] + " " + y
            new_list.append(i)
        else:
            new_list.append(i)
    return new_list



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#["David Andrew Joyner", "Melissa Joan Hart", "Billy Ray Cyrus"]
name_list = ["David Andrew Joyner", "Hart, Melissa Joan", "Cyrus, Billy Ray"]
print(name_fixer(name_list))
