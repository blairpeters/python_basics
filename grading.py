score = int(input("Enter score: "))

#if statements
if score > 90:
    print("A")
elif 80 <= score < 90:
    print("A-")
elif 70 <= score < 80:
    print("B")
elif 60 <= score < 70:
    print("B-")
elif 50 <= score < 60:
    print("C")
elif 40 <= score < 50:
    print("C-")
elif 30 <= score < 40:
    print("D")
elif 20 <= score < 30:
    print("D-")
elif 10 <= score < 20:
    print("E")
else:
    print("F")
