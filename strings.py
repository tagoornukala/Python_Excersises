#1. How would you confirm that 2 strings have the same identity?
'''
string1 = "Tagoor"
string2 = "Nukala"

print(id(string1))
print(id(string2))
print(string1 == string2)

#output:
2881226794352
2881226794544
False

str1 = "Tagoor"
str2 = "Tagoor"

print(id(str1))
print(id(str2))

print(str1 == str2)

#output:
1492628529520
1492628529520
True
'''

#----------------------------------------------------------------------------------------------------------------------------------------------

# 2.How would you check if each word in a string begins with a capital letter?
'''
str = "Tagoor"

print(str.istitle())
print('\n')

str2 = "tagoor"
print(str2.istitle())

#output:

True


False
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------

# 3.Check if a string contains a specific substring
'''

str1 = "lists are mutable"
print('mutable' in str1)
print('imutable' in str1)
#output:
True
False
'''

#------------------------------------------------------------------------------------------------------------------------------------------------


# 4.Find the index of the first occurrence of a substring in a string
'''
stri = "lists are mutable"

print(stri.find('are'))

print(stri.find('lists'))

print(stri.find('mutable'))

#output:

6
0
10
'''

#------------------------------------------------------------------------------------------------------------------------------------------------

# 5.Count the total number of characters in a string
'''
str1 = "Tagoor Ajay Kumar"

print(len(str1))

#output:
17
'''

#------------------------------------------------------------------------------------------------------------------------------------------------

# 6.Count the number of a specific character in a string
'''
str1 = "Hello world good morning"

print(str1.count('l'))

#output:
3
'''

#------------------------------------------------------------------------------------------------------------------------------------------------

# 7.Capitalize the first character of a string
'''
string = "tuple is a imutable"

print(string.capitalize())

#output:
Tuple is a imutable
'''


#-------------------------------------------------------------------------------------------------------------------------------------------------

# 8.What is an f-string and how do you use it?

'''
name = 'tagoor'
food = 'chiken'

print(f'my name is {name} and i like the {food}') 

#output:
my name is tagoor and i like the chiken
'''

#----------------------------------------------------------------------------------------------------------------------------------------------

# 9.Search a specific part of a string for a substring
'''
string = "tagoor ajay kumar"

print(string.index('j'))


#output:
8
'''


#----------------------------------------------------------------------------------------------------------------------------------------------

# 10.Interpolate a variable into a string using format()

'''
print('The {}  a {}'.format('is','pen'))
#output:
The is  a pen
'''

#----------------------------------------------------------------------------------------------------------------------------------------------

# 11.Check if a string contains only numbers
'''
str1 = "tag12345"

print(str1.isnumeric())

#output:
False
'''

#----------------------------------------------------------------------------------------------------------------------------------------------

# 12.Split a string on a specific character
'''
string = "Set doest follow the insertion order"

print(string.split())

#output:
['Set', 'doest', 'follow', 'the', 'insertion', 'order']

'''

#---------------------------------------------------------------------------------------------------------------------------------------------------

# 13.Check if a string is composed of all lower case characters

'''

string = "global variable"

print(string.islower())

string1 = "Local Variable"

print(string1.islower())

#output:
True
False
'''

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
# 14.Check if the first character in a string is lowercase
'''
string = "sTATIC VARIABLE"

print(string[0].islower())

string1 = "Non Static Variable"
print(string1[0].islower())

#output:
True

False
'''

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 15.Can an integer be added to a string in Python?
'''
ANS:No It will show type Error
'''

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 16.Reverse the string “hello world”
'''
str = "hello world"

print(str[::-1])

#output:
dlrow olleh

'''

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 17.Join a list of strings into a single string, delimited by hyphens
'''
list = ['t','a','g','o','o','r']

print('-'.join(list))

#output:
t-a-g-o-o-r
'''

#-----------------------------------------------------------------------------------------------------------------------

# 18. Check if all characters in a string conform to ASCI
'''
string = 'T'

print(string.isascii())

#output:
True
'''
#-----------------------------------------------------------------------------------------------------------------------------------------

# 19.Uppercase or lowercase an entire string
'''
string = 'function'

print(string.upper())

print(string.lower())

#output:
FUNCTION
function'''


#-----------------------------------------------------------------------------------------------------------------------

# 20.Uppercase first and last character of a string
'''
string = 'class'

print(string[0].upper()+string[1:-1]+string[-1].upper())

string2 = 'tagoor'
print(string2[0].upper()+string2[1:-1]+string2[-1].upper())
#output:
ClasS
TagooR
'''


#-------------------------------------------------------------------------------------------------------------------------------------

# 21.Check if a string is all uppercase
'''
string = 'STRINGS'

print(string.isupper())

#output:
True'''
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

# 22. When would you use splitlines()?

#splitlines() splits a string on line breaks.
'''
string = "list is a mutable\nlist supports indexing\nlist have methods"

print(string.splitlines())

#output:
['list is a mutable', 'list supports indexing', 'list have methods']
'''

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 23.Give an example of string slicing

string = 'tuple is immutable'
'''
print(string[:5])
print(string[6:8])
print(string[9:])
print(string[-9:])
print(string[-12:-10])
print(string[-18:-13])
#output:

tuple
is
immutable
immutable
is
tuple
'''

#-------------------------------------------------------------------------------------------------------------------------------------------------

# 24.Convert an integer to a string
'''
inti = 10

stri = str(inti)
print(stri,type(stri))

#output:
10 <class 'str'>

'''

# ------------------------------------------------------------------------------------------------------------------------------------

# 25.Check if a string contains only characters of the alphabet
'''
string = 'tagoor1332'

print(string.isalpha())

string1 = 'tagoor'
print(string1.isalpha())

#output:

False
True
'''


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 26.Replace all instances of a substring in a string

'''
string = 'tagoor ajay'

print(string.replace('ajay','nukala'))

#output:

tagoor nukala
'''

#------------------------------------------------------------------------------------------------------------------------------------------------

# 27.Return the minimum character in a string
'''
string = 'list'

print(min(string))

#output:
i
'''

#------------------------------------------------------------------------------------------------------------------------------------------------

# 28.Check if all characters in a string are alphanumeric
'''
string = 'set10'

string1 = 'ser.10'
print(string.isalnum())
print(string1.isalnum())

#output:
True
False
'''

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 29.Remove whitespace from the left, right or both sides of a string
'''
string = '   Hello Goodmorning'

print(string.strip())
print(string.rstrip())
print(string.lstrip())
#output:
Hello Goodmorning
   Hello Goodmorning
Hello Goodmorning
'''

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 30.Check if a string begins with or ends with a specific character?
'''
string = 'Hyderabad'

print(string.startswith('Hy'))

print(string.endswith('ad'))

#output:
True
True
'''
