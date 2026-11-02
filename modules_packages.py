#Modules are basically files. in our case eg is my_function file etc
#packages are basically folders. in a large products the files will be in folders which we then call packages eg my_package which is created  by right click folder --> New --> python package

# import my_functions
#
# print(my_functions.volume_cylinder(10,10))

#imagine you have 2 files with the same name
#you will use the as keyword to rename one of the function to a new name eg import my_functions as new_name_function
#now you will use the new name to access the methods eg print(new_name_functions.volume_cylinder(10,10))

#importing packages

from my_package import shapes
print(shapes.triangle(2,4,5))


#you can also import as follows
from my_package.shapes import *
print(circle(10))