#Write a function called semihemisphere. semihemisphere
#should return which semihemisphere a latitude-longitude
#coordinate pair is in: Northwest, Northeast, Southwest,
#or Southeast. A point in the Northern and Western
#hemispheres would be Northwest; in the Southern and Eastern
#hemispheres would be Southeast; etc.
#
#semihemisphere will take as input two floats: latitude
#and longitude. Latitude is a number between -90 and 90
#representing the North-South position on the globe (-90
#for the South pole, 90 for the North pole). Longitude is
#a number between -180 to 180 representing the East-West
#position on the globe (-180 is the furthest west, and 180
#is the furthest east).
#
#The Southern hemisphere is from -90° to 0° latitude. The
#Northern hemisphere is from 0° to 90° latitude. The
#Eastern hemisphere is from 0° to 180° longitude. The
#Western hemisphere is from -180° to 0° longitude.


#Add your code here!
def semihemisphere(lat, long):
    if lat > 0 and lat <= 90:
        lat_semi = "North"
    elif lat >= -90 and lat < 0:
        lat_semi = "South"
    if long > 0 and long <=180:
        long_semi = "east"
    elif long >= -180 and long < 0:
        long_semi = "west"
    return lat_semi + long_semi

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print Northwest, Southeast, Northeast, Southwest
print(semihemisphere(67, -84.4))
print(semihemisphere(-71.1, 86.3))
print(semihemisphere(67.1, 12.1))
print(semihemisphere(-11.6, -62.3))
