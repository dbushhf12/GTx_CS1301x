#Write a function called mock. mock should take one
#parameter, a string. You may assume that the string will
#have only lowercase letters and spaces.
#
#Your function should return the same string, but any letter
#at an even index should be converted to uppercase.
#
#For example: mock("abcd efgh ijkl") would return
#"AbCd eFgH IjKl".
#
#Remember, you can use the ordinal function ord() to get the
#number associated with a single letter. For example,
#ord("a") returns 97. The number associated with lowercase
#letters is always 32 larger than the number associated with
#the equivalent uppercase letter. ord("a") is 97, and
#ord("A") is 65. ord("z") is 122, and ord("Z") is 90.
#
#Remember, you can use the character function chr() to
#convert a number back to a letter. For example, chr(65) will
#return "A".
#
#HINT: Treat all characters the same initially, then worry
#about taking care of spaces afterwards.


#Write your function here!
def mock(string):
    stringUpper = ""
    counter = 0
    for i in string:
        if counter%2 == 0 and ord(i) != 32:
            i = ord(i) - 32
            i = chr(i)
            stringUpper += i
            counter += 1
        elif counter%2 != 0 and ord(i) != 32:
            stringUpper += i
            counter += 1
        elif ord(i) == 32:
            stringUpper += " "
            counter += 1        
    return stringUpper


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "AbCd eFgH IjKl".

print(mock("abcd efgh ijkl"))
