#Recall Coding Problem 4.3.9 (Advanced), the free body
#diagram problem. If you were unable to solve that, we've
#included the sample answer in the dropdown in the top left
#-- feel free to use that to write your answer to this
#problem.
#
#Revise your code from that problem to use a file instead of
#a list as its parameter. Name this new function
#find_net_force_from_file. The function should take one
#parameter, the name of a file. The function should return
#the net magnitude and direction, just as it did in the other
#problem.
#
#Each line of the file will have two numbers, both integers:
#the first number will be the magnitude, and the second
#number will be the angle (in degrees, from -180 to 180).
#There will be a space between them.
#
#HINT: You may have multiple functions in your code if you
#want!
#
#HINT 2: Try to write this such that you can reuse as much
#of your earlier code as possible. Remember, when loading
#from a file, any text you load is initially a string. You'll
#almost certainly need to use the split() method.

from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt

#Add your function here!
def find_net_force_from_file(filename):
    #file management
    read_file = open(filename, "r")
    list_file = read_file.readlines()
    new_list = []
    read_file.close()
    
    for i in list_file:
        i = i.split()
        new_list.append(i)
   
    #define variables
    horizontal_force = []
    vertical_force = []
    total_horizontal = 0
    total_vertical = 0
    total_magnitude = 0
    angle = 0
    
    for single_tuple in new_list:
        angle_in_radians = radians(float(single_tuple[1]))        
        h = float(single_tuple[0]) * cos(angle_in_radians)
        v = float(single_tuple[0]) * sin(angle_in_radians)
        horizontal_force.append(h)
        vertical_force.append(v)
        
    for i in horizontal_force:
        total_horizontal += i
        
    for i in vertical_force:
        total_vertical += i
        
    total_magnitude = round(sqrt((total_horizontal**2) + (total_vertical**2)),1)
    angle = atan2(total_vertical, total_horizontal)
    angle_in_degrees = round(degrees(angle),1)
    
    return total_magnitude, angle_in_degrees

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: (87.0, 54.4)
print(find_net_force_from_file("a_few_angles.txt"))
