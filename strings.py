name = "Joy"
sentence = "My home area is called \"xyz\"" #escape character to allow quotes inside a string
print(sentence.upper())
print(sentence.capitalize()) # makes first letter capital
print(sentence.title()) #capitalizes every first letter of every word in the sentence variable
print(name.count("J"))
print(len(sentence))
replaced_sentence = sentence.replace("home", "city")
print(replaced_sentence)
k = "123"
print(sentence.isnumeric())