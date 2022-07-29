#A significant part of introductory physics is calculating
#the net force on an object based on several different
#magnitudes and directions. If you're unfamiliar with how
#this works, we recommend checking out this WikiHow article:
#https://www.wikihow.com/Find-Net-Force
#
#Each force acting on the object is defined by its angle and
#magnitude. The process for calculating net force is:
#
# - For each force, break the force into its horizontal and
#   vertical components. The horizontal component can be
#   calculated as magnitude * cos(angle), and the vertical
#   component can be calculated as magnitude * sin(angle).
# - Sum all the horizontal components to find the total
#   horizontal force, and sum the vertical components to find
#   the total vertical force.
# - Use the Pythagorean theorem to calculate the total
#   magnitude: sqrt(total_horizontal ^ 2 + total_vertical ^ 2)
# - Use inverse tangent to calculate the angle:
#   atan2(total_vertical, total_horizontal)
#
#Write a function called find_net_force. find_net_force should
#take one parameter as input: a list of 2-tuples. Each 2-tuple
#in the list is a (magnitude, angle) pair. angle will be in
#degrees between -180 and 180.
#
#Return a 2-tuple containing the final magnitude and angle of
#all the forces. angle should again be in degrees. You should
#round both magnitude and angle to one decimal place, which
#you can do using round(magnitude, 1) and round(angle, 1).
#
#To do this, you'll need to use a few functions from the math
#module in Python. The line below will import these:

from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt

#sin, cos, and tan are the trigonometric functions for sine,
#cosine, and tangent. Each takes one argument, an angle in
#radians, and returns its sine, cosine, or tangent.
#
#asin, acos, and atan2 are their inverse functions. Each
#takes two arguments, a vertical component and a horizontal
#component (in that order), and returns the corresponding
#angle in radians.
#
#Note that sin, cos, and tan all assume the angle is in
#radians, and asin, acos, and atan2 will all return an
#angle in radians. So, you'll need to convert your angles to
#radians before or after using these functions, using things
#like this: angle_in_radians = radians(angle)
#           angle_in_degrees = degrees(angle_in_radians)

#sqrt will find the square root of a number, e.g. sqrt(4) = 2.
#Note that you should only need sin, cos, atan2, degrees,
#radians, and sqrt: we've imported the others just in case you
#want to use them.


#Add your function here!
# - For each force, break the force into its horizontal and
#   vertical components. The horizontal component can be
#   calculated as magnitude * cos(angle), and the vertical
#   component can be calculated as magnitude * sin(angle).
# - Sum all the horizontal components to find the total
#   horizontal force, and sum the vertical components to find
#   the total vertical force.
# - Use the Pythagorean theorem to calculate the total
#   magnitude: sqrt(total_horizontal ^ 2 + total_vertical ^ 2)
# - Use inverse tangent to calculate the angle:
#   atan2(total_vertical, total_horizontal)
    #each tuple contains magnitude, angle (-180 to 180 degrees)
from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt
    
def find_net_force(list_of_tuples):
    horizontal_force = []
    vertical_force = []
    total_horizontal = 0
    total_vertical = 0
    total_magnitude = 0
    angle = 0
    for single_tuple in list_of_tuples:
        angle_in_radians = radians(single_tuple[1])        
        h = single_tuple[0] * cos(angle_in_radians)
        v = single_tuple[0] * sin(angle_in_radians)
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
    
#asin, acos, and atan2 are their inverse functions. Each
#takes two arguments, a vertical component and a horizontal
#component (in that order), and returns the corresponding
#angle in radians.
#
#Note that sin, cos, and tan all assume the angle is in
#radians, and asin, acos, and atan2 will all return an
#angle in radians. So, you'll need to convert your angles to
#radians before or after using these functions, using things
#like this: angle_in_radians = radians(angle)
#           angle_in_degrees = degrees(angle_in_radians)    

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: (87.0, 54.4)

forces = [(10, 90), (10, -90), (100, 45), (20, 180)]
print(find_net_force(forces))
