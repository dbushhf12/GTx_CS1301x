#In this problem, your goal is to write a function that can
#either count all the vowels in a string or all the consonants
#in a string.
#
#Call this function count_letters. It should have two
#parameters: the string in which to search, and a boolean
#called find_consonants. If find_consonants is True, then the
#function should count consonants. If it's False, then it
#should instead count vowels.
#
#Return the number of vowels or consonants in the string
#depending on the value of find_consonants. Do not count
#any characters that are neither vowels nor consonants (e.g.
#punctuation, spaces, numbers).
#
#You may assume the string will be all lower-case letters
#(no capital letters).


#Add your code here!
def count_letters(search_string, find_consonants):
    consonantList = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    vowelList = ["a","e","i","o","u"]
    consonantCounter = 0
    vowelCounter = 0
    if find_consonants:
        for i in search_string:
            if i in consonantList:
                consonantCounter +=1
        return consonantCounter
    elif not find_consonants:
        for i in search_string:
            if i in vowelList:
                vowelCounter += 1
        return vowelCounter


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 14, then 7.

a_string = "up with the white and gold"

print(count_letters(a_string, True))
print(count_letters(a_string, False))
