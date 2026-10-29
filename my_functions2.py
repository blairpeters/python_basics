#functions that receives three arguments only
def add(x, y, z):
    return x +y + z
# res = add(1, 2, 3)
# print(res)

#a function that can receive any number of arguments
def addition(*nums): #note: if you want to add another parameter it has to come before *num--that would also mean the first number in the arguments is that parameter
    # total = sum(nums) #using the sum inbuilt function to get the total of the numbers

    #getting the total using a for loop
    total = 0
    for num in nums:
        total += num
    return total

print(addition(1, 2, 3,4,5,6))
#key and word arguments (kwargs) functions
def save(**data):
    #note:with open makes sure the file is closed otherwise we would have to use file.close()
    with open("values.txt", "w") as file: #as it is w does not save the data...to make sure the data remains use a instead
        #for loop to write the data give the value.txt file
        for key, value in data.items():
            file.write(f"{key}: {value}\n")

save(dob='2025-01-18', gender='female', age=20, name='Liza')

#say you have a student,who has some scores that need to be filled then maybe an attribute say the course
#note that the arguments have to be in the following format below
def some_function(name, *scores, **details):
    pass

some_function("Hellen", 10,90,85, gender="female", course="IT")

def cylinder(r, h):
    #writing the documentation of the function using triple quotes
    """
    Calculates the volume and surface area of a cylinder
    parameters:
     r: radius of the cylinder
     h: height of the cylinder
    :return: volume and surface area
    """
    v = 3.14 * r * r * h
    sa = 3.14 * r**2 *2  + 3.14 * r * 2 * h
    return sa, v
surf_area, volume = cylinder(7, 15) #note that the variables here should be as they were return at return to avoid wrong value at wrong place
print(surf_area, volume)

#lamda functions
dividing = lambda x, y: x / y

area_circle = lambda radius: 3.14 * radius * radius
print(dividing(5, 5))
print(area_circle(5))


