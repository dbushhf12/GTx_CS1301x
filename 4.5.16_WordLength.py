#Recall last exercise that you wrote a function, word_lengths,
#which took in a string and returned a dictionary where each
#word of the string was mapped to an integer value of how
#long it was.
#
#This time, write a new function called length_words so that
#the returned dictionary maps an integer, the length of a
#word, to a list of words from the sentence with that length.
#If a word occurs more than once, add it more than once. The
#words in the list should appear in the same order in which
#they appeared in the sentence.
#
#For example:
#
#  length_words("I ate a bowl of cereal out of a dog bowl today.")
#  -> {3: ['ate', 'dog', 'out'], 1: ['a', 'a', 'i'],
#      5: ['today'], 2: ['of', 'of'], 4: ['bowl'], 6: ['cereal']}
#
#As before, you should remove any punctuation and make the
#string lowercase.
#
#Hint: To create a new list as the value for a dictionary key,
#use empty brackets: lengths[wordLength] = []. Then, you would
#be able to call lengths[wordLength].append(word). Note that
#if you try to append to the list before creating it for that
#key, you'll receive a KeyError.


#Write your function here!
def length_words(string):
    temp_str = string.lower()
    string_list = []
    length_list = []
    punct_library = "!()%$><.,:;{}[]+=_-"
    my_dict = {}

    
    for char in temp_str:
        if char in punct_library:
            temp_str = temp_str.replace(char, "")
    
    split_string = temp_str.split()
    for i in split_string:
        string_list.append(i)
        length_list.append(len(i))
    
    for i in length_list:
        my_dict[i] = []
        for j in string_list:
            if len(j) == i:
                my_dict[i].append(j)
                
    
    return my_dict    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#{1: ['i', 'a', 'a'], 2: ['of', 'of'], 3: ['ate', 'out', 'dog'], 4: ['bowl', 'bowl'], 5: ['today'], 6: ['cereal']}
#
#The keys may appear in a different order, but within each
#list the words should appear in the order shown above.
print(length_words("I ate a bowl of cereal out of a dog bowl today."))
