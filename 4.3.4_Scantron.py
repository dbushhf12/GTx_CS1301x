#Write a function called grade_scantron. grade_scantron should
#take as input two lists: answers and key. Each list contain
#strings. Each string will be only one letter, a character
#from A to E. grade_scantron should return how many questions
#the student got "right", where a student gets a question
#right if their answer for a problem matches the answer key.
#
#In other words, if value of the first item in answers matches
#the value of the first item in key, the student gets a point.
#If it does not, the student does not get a point.
#
#If the lists do not have the same number of items, return
#-1 to indicate that the answer key did not belong to the
#same test as the student's answers.\
#
#Hint: in the past, lots of people have tried to do this using
#the index() method. That won't work! You'll need to track the
#index yourself.


#Write your function here!
def grade_scantron(answers, key):
    
    temp1 = answers
    temp2 = key
    index = 0
    grade = 0
    
    if len(temp1) != len(temp2):
        return -1
    else:
        while len(temp1) > 0:
            x = temp1.pop(0)
            y = temp2.pop(0)
            if x == y:
                grade += 1
        return grade
            


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 7
test_answers = ["A", "B", "B", "A", "D", "A", "B", "A",]
test_key = ["A", "B", "B", "A", "D", "E", "B", "A", "D"]
print(grade_scantron(test_answers, test_key))
