#In this problem, you should write three functions:
#word_count, letter_count, and average_word_length.
#
#word_count should take as input a string. It should return
#the number of words in the string. You may assume that the
#number of words in the string will be one more than the
#number of spaces in the string.
#
#letter_count should take as input a string. It should return
#the number of letters in the string. You may assume that
#the string is only letters and spaces: no punctuation or
#numbers.
#
#average_word_length should take as input a string. It should
#return the average length of the words in the string. You
#can find the average length by dividing the number of letters
#by the number of words.
#
#Your implementation for average_word_length *must* call
#word_count and letter_count.


#Add your code here!
def word_count(string):
    numWords = 0
    for i in string:
        if i == " ":
            numWords += 1
    numWords += 1
    return numWords

def letter_count(string):
    numLetters = 0
    for i in string:
        if i != " ":
            numLetters += 1
    return numLetters

def average_word_length(string):
    words = word_count(string)
    letters = letter_count(string)
    avgLength = letters/words
    return avgLength
#Below are some lines of code that will test your function.
#You can change the value of the variable to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 3.5
a_string = "Up with the white and gold"

print(average_word_length(a_string))
