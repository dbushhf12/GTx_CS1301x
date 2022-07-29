#Write a function called word_lengths, which takes in one
#parameter, a string, and returns a dictionary where each
#word of the string is mapped to an integer representing how
#how long that word is. You should ignore punctuation, and
#all the words should be lowercase. You can assume that the
#only punctuation marks in the string will be periods,
#commas, question marks, exclamation points, and apostrophes.
#
#For example:
#  word_lengths("I ate a bowl of cereal out of a dog bowl today.")
#  -> {'i':1, 'bowl':4, 'today':5, 'out':3, 'dog':3, 'ate':3,
#      'a':1, 'of':2, 'cereal':6}
#
#Hint: Use the split() method to split by spaces, and don't
#forget to remove punctuation marks.  Remember also: strings
#are immutable, so operations like my_string.lower() don't
#change the value of my_string like list methods: to save
#those results, you'd write my_string = my_string.lower().
#
#Your dictionary should not have any duplicate keys (in fact,
#Python won't allow a dictionary to have duplicate keys).


#Write your function here!
def word_lengths(string):
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
    
    
    for var in range(0, len(string_list)):
        my_dict[string_list[var]] = length_list[var]
    
    return my_dict
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#{'dog': 3, 'today': 5, 'of': 2, 'ate': 3, 'bowl': 4, 'out': 3, 'a': 1, 'cereal': 6, 'i': 1}
#
#The order of the keys may differ, but that's okay!
print(word_lengths("I ate a bowl of cereal out of a dog bowl today."))
