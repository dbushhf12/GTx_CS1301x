story = "A"
text = "B"
role = "C"
director = "D"
cast = "F"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#In Bryan Cranston's autobiography, he describes how after
#his success on Breaking Bad, he developed a scoring system
#for evaluating new scripts that he received.
#
#First, he would assign the script a grade -- A, B, C, D, or
#F -- in each of five categories: Story, Text, Role, Director,
#and Cast.
#
#Then, he would tally those grades into a total score for the
#script, according to the following chart:
#
#            A   B   C   D   F
# Story     +6  +5  +4  +2  +0
# Text      +5  +4  +3  +1  +0
# Role      +4  +3  +2  +1  +0
# Director  +3  +2  +1  +0  +0
# Cast/Misc +2  +1  +0  +0  +0
#
#For example: an A story, B text, C role, D directory, and
#F cast would get a score of 12: +6 for the story, +4 for the
#text, +2 for the role, +0 for the director, and +0 for the
#cast.
#
#Then, based on that score, the script would be assigned a
#category (note these are slightly different from the image
#because we've excluded the time variable):
#
# 20: Perfect score
# 17 to 19: Must do
# 14 to 16: Seriously consider
# 12 to 13: On the bubble
# 11 or below: Pass
#
#The variables above give the letter grades assigned to each
#of the five components. Write a program that calculates the
#total score he would assign to the script represented by
#these variables. Then on the next line, print the category
#he would assign to that script. For example, for the values
#above, this program would print:
#
#12
#On the bubble
#
#HINT: This is a *long* program. It's not particularly
#complex -- you're doing the same thing over and over, However,
#that 'same thing' required 4-8 lines each time you do it. Our
#answer is 46 lines long! So, don't think you're off-track just
#because you're writing a lot of lines.


#Add your code here!
finalScore = 0

if story == "A":
    story = 6
elif story == "B":
    story = 5
elif story == "C":
    story = 4
elif story == "D":
    story = 2
elif story == "F":
    story = 0

if text == "A":
    text = 5
elif text == "B":
    text = 4
elif text == "C":
    text = 3    
elif text == "D":
    text = 1    
elif text == "F":
    text = 0    
    
if role == "A":
    role = 4
elif role == "B":
    role = 3
elif role == "C":
    role = 2
elif role == "D":
    role = 1    
elif role == "F":
    role = 0    
    
if director == "A":
    director = 3
elif director == "B":
    director = 2
elif director == "C":
    director = 1
elif director == "D":
    director = 0    
elif director == "F":
    director = 0      

if cast == "A":
    cast = 2
elif cast == "B":
    cast = 1
elif cast == "C":
    cast = 0
elif cast == "D":
    cast = 0    
elif cast == "F":
    cast = 0     
    
finalScore = story + text + role + director + cast
print(finalScore)

if finalScore == 20:
    print("Perfect score")
elif finalScore >=17 and finalScore < 20:
    print("Must do")
elif finalScore >=14 and finalScore < 17:
    print("Seriously consider")
elif finalScore >=12 and finalScore < 14:
    print("On the bubble")
elif finalScore < 12:
    print("Pass")
