# Exercise 1: Person :ballot_box_with_check:

#Use a dictionary to store information about a person you know.Store their first name, last name, age, and the city in which they live. You

#should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

#This is solution
person = {
'first_name': 'Iqra',
'last_name': 'Waseem',
'age': 45,
'city': 'UAE',
}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])


# Exercise 2: Glossary :ballot_box_with_check:

#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

# Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 

#their meanings as values.

#Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 

#the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 

#each word-meaning pair in your output.

#This is solution
glossary = {
'string': 'A series of characters.',
'comment': 'A note in a program that the Python interpreter ignores.',
'list': 'A collection of items in a particular order.',
'loop': 'Work through a collection of items, one at a time.',
'dictionary': "A collection of key-value pairs.",
}
word = 'string'
print(f"\n{word.title()}: {glossary[word]}")
word = 'comment'
print(f"\n{word.title()}: {glossary[word]}")
word = 'list'
print(f"\n{word.title()}: {glossary[word]}")
word = 'loop'
print(f"\n{word.title()}: {glossary[word]}")
word = 'dictionary'
print(f"\n{word.title()}: {glossary[word]}")


# Exercise 3: Glossary 2 :ballot_box_with_check:
#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

#calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 

#to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {
'string': 'A series of characters.',
'comment': 'A note in a program that the Python interpreter ignores.',
'list': 'A collection of items in a particular order.',
'loop': 'Work through a collection of items, one at a time.',
'dictionary': "A collection of key-value pairs.",
'key': 'The first item in a key-value pair in a dictionary.',
'value': 'An item associated with a key in a dictionary.',
'conditional test': 'A comparison between two values.',
'float': 'A numerical value with a decimal component.',
'boolean expression': 'An expression that evaluates to True or False.',
}
for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")


# Exercise 4: Rivers :ballot_box_with_check:

#Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

#Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

#Use a loop to print the name of each river included in the dictionary.

#Use a loop to print the name of each country included in the dictionary.

#This is soulation 
rivers = {
'Sepik': ' Guinea.',
' Mississippi': 'United States',
'Volga': ' Russias ',
'Zambezi ': ' Africa.',
'yangtze': 'china',
}
for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")
print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river.title()}")
print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(f"- {country.title()}")


# Exercise 5: Pets :ballot_box_with_check:

#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

#owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 

#each pet

#This is solution 
# Creating dictionaries for different pets
pet1 = {'animal': 'Dog', 'owner': 'John'}
pet2 = {'animal': 'Cat', 'owner': 'Alice'}
pet3 = {'animal': 'Parrot', 'owner': 'Bob'}
pet4 = {'animal': 'Fish', 'owner': 'Eva'}
# Storing the dictionaries in a list called pets
pets = [pet1, pet2, pet3, pet4]
# Looping through the list and printing information about each pet
for pet in pets:
    print(f"Pet: {pet['animal']}")
    print(f"Owner: {pet['owner']}")
    print()










