#Now let's make things a little more challenging.
#
#Last exercise, you wrote a function called word_count that
#counted the number of words in a string essentially by
#counting the spaces. However, if there were multiple spaces
#in a row, it would incorrectly add additional words. For
#example, it would have counted the string "Hi   David" as
#4 words instead of 2 because there are two additional
#spaces.
#
#Revise your word_count method so that if it encounters
#multiple consecutive spaces, it does *not* count an
#additional word. For example, these three strings should
#all be counted as having two words:
#
# "Hi David"
# "Hi   David"
# "Hi                 David"
#
#Other than ignoring consecutive spaces, the directions are
#the same: write a function called word_count that returns an
#integer representing the number of words in the string, or
#return "Not a string" if the input isn't a string. You may
#assume that if the input is a string, it starts with a
#letter word instead of a space.

#Write your function here!
def word_count(my_string):
    singleSpace = 0
    multipleSpace = 0
    try:
        for i in range(0, len(my_string)):
            if my_string[i] == " ":
                singleSpace += 1
            if my_string[i] == " " and my_string[i+1] == " ":
                multipleSpace += 1
    except:
        return "Not a string"
    else:
        actual = (singleSpace - multipleSpace) + 1
        return actual


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#Word Count: 4
#Word Count: 2
#Word Count: Not a string
#Word Count: Not a string
#Word Count: Not a string

print("Word Count:", word_count("Four words are here!"))
print("Word Count:", word_count("Hi   David"))
print("Word Count:", word_count(5))
print("Word Count:", word_count(5.1))
print("Word Count:", word_count(True))
