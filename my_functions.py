def greet():
    print("Hello, welcome to python")


def greeting(user):
    print(f"Hello, {user}!")
greeting("Jim")
greeting("Ahmed")

def area_circle(radius, precision):
    a = 3.14 * radius**2
    result = round(a, precision)
    print(f"The area is {result}")

area_circle(2.9, 2)

def volume_cylinder(r,h):
    v = 3.14 * r**2 * h
    return v
print(volume_cylinder(10.5, 12.8))