#stores data


#data structures
#lists,sets,tuples,dictionary

#### 1) LISTS [] #####

people = ["Jack","Jane","Ahmed","Hussein","Miriam"]

scores = [87, 45, 67, 52, 91, 21, 66, 77, 81]
# print(people[0])
# print(people)
# people.append("Jack")
# print(people)
# people.clear() #empties the list
# print(people)
# people.sort() #alphabetical sort
# print(people)
# scores.sort() #lowest to highest
# print(scores)
# people.sort(reverse=True) #highest to lowest
# print(people)
# print(scores[-1]) # -1 prints the last item on the list
# print(sum(scores))
# print(len(scores))
# print(sum(scores) / len(scores))
#
# #slicing...cutting some bit of it...eg when told get me the top three people
# scores.sort()
# print(scores)#sorts it in ascending
# print(scores[-2:]) #gives the last two numbers of the ascending numbers
# print(scores[:2])  #gives the first two numbers in the sorted
# print(scores[::2]) #selects every second element starting from index 0
# print(scores[1::2]) #This selects every second element, starting from index 1.
# print(scores[3:5]) #note that 5 is not included in slicing..so you will print index 3 and 4 only

#### 2) SETS {} #### ---set removes duplicates

# numbers = {87, 89, 87, 67, 54}
# print(numbers) # will not duplicate the 87 even though it appears twice above...in the display only one 87 is printed

#### 3) TUPLE () #### --- DATA YOU DONT WANT TO CHANGE ACCIDENTALLY..IMMUTABLE DATA

days = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")

#### 4) DICTIONARY {}  #### ---- CONTAINS KEY AND VALUE PAIRS

person = {"name": "Zillow", "City": "Marsabit", "age": 19}
print(person["name"]) #note that printing a dictionary uses the keys not index position
print(person["City"])
print(person["age"])

watu = [
    {"name": "Sila",  "age": 19},
    {
        "name": "Juan",
        "age": 59 },
    {
        "name": "Julia","age": 16 }


]
print(watu[2]) #prints the third dictionary
print(watu[2]["name"]) # prints  thirds person name