import random

#first wAY TO IMPORT MY_FUNCTIONS.PY
from my_functions import greet

#SECOND WAY TO IMPORT MY_FUNCTIONS.PY
import my_functions

#functions

#inbuilt function to open a file and write inside it
with open("data.txt","a") as file:
    # file.write("99\n")
    # file.write("68\n")

    for temp in range(100):
        x = random.randint(-10,65)
        file.write(str(x) + "\n")
with open("data.txt","r") as file:
    content = file.read()
    print(content)

#how to call greet if you use the first style of importing myfunction
greet()

#SECOND WAY TO CALL GREET FROM MY FUNCTIONS.PY IF YOU USED THE SECOND WAY OF IMPORT
my_functions.greet()
my_functions.greeting("Blair")