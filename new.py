from collections import Counter
import re
word = "Aashutosh Dahal"
char = word[0]
print(char)
word = 'Aashutosh Dahal'.replace('Aashutosh', 'Aashu')
splitword = word.split(" ")
for word in splitword:
    print(word)
print(word.count('a'))
csv = "aashutoshdahal;nepal;aashutoshdahal22@gmail.com"
my_data = csv.split(";")
for data in my_data:
    print(data)
print(my_data[2])

phrase = 'Do or  do not  there is no   try'
phrase_no_space = re.sub(r'\s+', '', phrase)
print(phrase)
print(phrase_no_space)
long_text = ("This is a multiline, \n"
             "a long string with lots of text,\n"
             "I'm wrapping it in a tripele quotes to make it work.")
print(long_text)
long_text = "This is a multiline, \n"\
    "a long string with lots of text,\n"\
    "I'm wrapping it in a tripele quotes to make it work."
print(long_text)  # WE CAN USE "\" BACKSLASH TO REPLACE THE BRACKET
regulartext = "@#$%^This is a text with some space at the start   "
# lstrip() removes the spaces from the begining of the text
# rstrip() removes the spaces from the ending of the text
# strip() removes from both
nospacetext = regulartext.rstrip()
cleantext = regulartext.lstrip("@#$%^")
nospacetextend = regulartext.strip("@#$%^")
print(nospacetext)
print(cleantext)
print(nospacetextend)
text = "HELLO i am aashutosh dahal"
lowertext = text.lower()  # lower() lowers the uppercase
print(lowertext)
titlecase = text.title()
print(titlecase)  # title() changes the first letter of a text to uppercase
swapcase = text.swapcase()
print(swapcase)
word = 'beach'
number_chars = 32
char = '$'
char1 = '#'
word_justified = word.rjust(number_chars, char)
wordjustified = word.ljust(number_chars, char1)
print(word)
print(word_justified)
print(wordjustified)
a = 3
b = 3
c = 4
print(a is b)  # identity operators
print(a is not c)
a = [1, 2, 3, 4, 5]
print(3 in a)
print(12 not in a)  # amembership operators
num = 69
print(f"Is num even?\n{True if num%2==0 else False}")
author = 'aashutosh dahal'
a_name = author.title()
print(f'This is a book by {a_name}.')
print(f"This is a book by {author.title()}.")


def comp(c):
    if c % 2 == 0:
        return ("Learn python")
    else:
        return ("Learn JavaScript")


print(f"Hello bish, tell me what i should learn. {comp(2)}")
names = ['Ria', 'Lana', 'Jade', 'Doe']
names1 = ['Ria', 'Lana', 'Jade', 'Doe']
names2 = ['Ria', 'Lana', 'Jade', 'Doe']
names1.append("Joe")  # inserts another name at the end of the list
# inserts wherever it is defined for eg here it is 2 so Joe is inserted in 3rd posistion
names.insert(2, "Joe")
names[3] = "PANT"
names.pop()
del names[2]
names2.clear()
print(names[-1])  # negative index starts the indentation from backwards
print(names1)
print(names)
tuple = ("apple", "banana", "cat", "dog")
print(len(tuple))  # calulate lenght of the tuple

thistuple = ('apple',)
# type keyword defines the type of the expesssion here due to the comma it is a tuple
print(type(thistuple))
# TUPLES HAVE COMMAS SEPERATING THEM AND ARE NOT EDITABLE

thetuple = ("apple")
print(type(thetuple))

difftuple = (123, 'ABCD', True, 'male', 40)
print(difftuple)

# list is orderd and changable duplication allowed
a = [1, 2, 3, 4, 5]  # this is a list
# tuple are ordered and unchangable allows duplication
a = ('1', '2', '3', '4', '5')  # this is a tuple
# set unordered and unchangable dont allow duplication
a = {'1', 2, '3', '4', 5}  # this is set
# dictionary are ordered and unchangable dont allow duplication
a = {'apple': 1, 'banana': 2, 'carrot': 3,
     'grade': 'A'}  # this is a dictionary

names = ("Aashutosh", "Dahal", "Aashu")
ages = (2, 4, 6)
zipped = zip(names, ages)
print(tuple(zipped))
for (x, y) in zipped:
    print(x, y)  # this zipes numbers and names in a vertical manner
fruits = ['apple', 'banana', 'orange', 'grape']
# this indexed the lists starting from 1
for index, fruits in enumerate(fruits, start=1):
    print(f"Index {index} contains {fruits}")
# this indeced the list starting from 0 because there is no start so it defaults to 0
for index, fruits in enumerate(fruits):
    print(f"Index {index} contains the fruits named {fruits}")
text = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 2, 3, 4, 5]
text_count = Counter(text)
common_elements = text_count.most_common(2)
print(common_elements)

words = ['apple', 'banana', 'clit', 'apple', 'banana', 'citrus']
words_counts = Counter(words)
most_common_words = words_counts.most_common(2)
print(most_common_words)

# RANGE
mynames = ["Aashutosh", "Aashu", "Puntu", "Muju", "Histi"]
for index in range(len(mynames)):
    print(f"at index {index} my name is {mynames[index]}")

for index in range(-5):  # negative index gives nothing
    print(index)

for index in range(10, 50, 5):  # start stop index
    print(index)

for index in range(-5, 0):
    print(index)

for index in reversed(range(10)):  # reverses the index deu to the "reversed"
    print(index)

# LIST COMPREHENSION
my_list = []
for num in range(5):
    my_list.append(num)
print(my_list)

mylist = [num for num in range(5)]
print(mylist)

nums = [1, 2, 3, 4, 5]  # creating a list of numbers
sq_nums = []  # creating an empty list
for num in nums:
    sq_nums.append(num*num)
print(sq_nums)

numbers = [num*10 for num in range(10)]
print(numbers)

new_list = [num for num in range(50) if num > 20 and num % 2 == 0]
print(new_list)

# using list comprehension in words using python
language = [letter for letter in "Python"]
print(language)

lang = [letter.upper() for letter in "python"]
print(lang)
