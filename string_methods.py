#string Methods:

#1.capitalize():Converts the first character to upper case
'''
str = "python"

print(str.capitalize())

#output:
Python
'''

#--------------------------------------------------------------------------------------

# 2.casefold():converts string into lower case
'''
str = "PYTHON"

print(str.casefold())

#output:
python
'''

#------------------------------------------------------------------------------------------

#3.center():Returns a centered string
'''
str = "tagoor"

print(str.center(50))

#output:
                      tagoor                      
'''

#------------------------------------------------------------------------------------------------------------

#4.count():Returns the number of times a specific value occurs in a string
'''
str = "data types"
print(str.count('a'))
#output:
2
'''

#------------------------------------------------------------------------------------------------------------------------

#5.encode():retuns an encode version of string


'''
str = "My name is  tagoor"

True
print(str.encode())


#output:
b'My name is  tagoor'
'''

#--------------------------------------------------------------------------------------------------------------------------------------

#6.endswith():returns true if the string ends with the specified value.
'''
str = "tagoor"

print(str.endswith('r'))

#output:
True
'''

#--------------------------------------------------------------------------------------------------------------------------------------------

#7.expandtabs(): set the tab size of the string.
'''
str = "f\tu\tn\tc\tt\ti\to\tn\ts"

print(str.expandtabs(1))

#output:
f u n c t i o n s
'''


#---------------------------------------------------------------------------------------------------------------------------------------

#8.find:serching the string for a specified value and,
#returns the position of where it was found
'''
str = "advanced concepets"

print(str.find('on'))

#output:
10
'''
#--------------------------------------------------------------------------------------------------------------------------------------------------

#9.format():Formats specified values in a string
'''
str = "python have {} many {}"
print(str.format('so','modules'))


#output:
python have so many modules
'''

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

# 10.index:searching the string for a specified value and
# returns the position of where it was found
'''
str = "welcome to ojas"

print(str.index('to'))

#output:
8
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 11.isalnum()	Returns True if all characters in the string are alphanumeric
'''
str = "python304"

print(str.isalnum())

#output:
True
'''


#--------------------------------------------------------------------------------------------------------------------------

# 12.isalpha():returns true if all characters in the string are in the alphabet.
'''
str = "PythonB"
print(str.isalpha())

#output:
True
'''

#---------------------------------------------------------------------------------------------------------------------------------------------------

# 13.isascii():Returns True if all characters in the string are ascii characters
'''
str  = "python304"

print(str.isascii())

#output:
True
'''

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 14.isdecimal():Returns True if all characters in the string are decimals
'''
str = '\u1234678'

print(str.isdecimal())

#output:
True
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 15.isdigit():returns true if all characters in the string are digits.
'''
str = "258933"
print(str.isdigit())

#output:
True
'''

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 16.isidentifier():returns true if string is an identifier.
'''
str = "demo"
print(str.isidentifier())

#output:
True
'''

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 17.islower():Returns True if all characters in the string are lower case
'''
str = "tagoor"

print(str.islower())

#output:
True
'''


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 18.isnumeric():Returns True if all characters in the string are numeric
'''
str = "123456"
print(str.isnumeric())

#output:
True
'''

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 19.isprintable():Returns True if all characters in the string are printable
'''
str ="Hello! Are you #1?"

print(str.isprintable())

str1 = "Hello!\n Are you #1?"
print(str1.isprintable())
#output:
True
False
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 20.isspace():Returns True if all characters in the string are whitespaces
'''
str  =" "
print(str.isspace())

str = ""
print(str.isspace())

#output:
True
False
'''

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 21.istitle():Returns True if the string follows the rules of a title
'''
str = "Tagoor"
print(str.istitle())

#output:
True
'''
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 22.isupper():Returns True if all characters in the string are upper case
'''
str = "PYTHON"
print(str.isupper())

#output:
True
'''

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 23.join():Converts the elements of an iterable into a string
'''
str = ("python","is","easy","compare","to","other","languages")

print("#".join(str))

#output:
python#is#easy#compare#to#other#languages
'''


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 24.ljust():Returns a left justified version of the string
'''
str = "python"

x = str.ljust(10)

print(x,"is a dynamically typed")

#output:
python     is a dynamically typed
'''

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 25.lower():Converts a string into lower case
'''
str = "DyNAMIC"

print(str.lower())

#output:
dynamic
'''

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 26.lstrip()	Returns a left trim version of the string
'''
str  = "   Tagoor "

print(str.lstrip())



#output:
Tagoor
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 27.maketrans():Returns a translation table to be used in translations
'''
str = "Hello Tagoor"

mystr = str.maketrans("T","t")

print(str.translate(mystr))


#output:
Hello tagoor
'''


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 28.partition():Returns a tuple where the string is parted into three parts
'''
str = "python supports both scripting and dynamic"

print(str.partition('both'))


#output:
('python supports ', 'both', ' scripting and dynamic')

'''


# 29.replace()	Returns a string where a specified value is replaced with a specified value
'''
str  = "i learn java"

print(str.replace("java","python"))
      
#output:
i learn python
'''

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 30.rfind():Searches the string for a specified value and returns the last position of where it was found
'''
str  = "python is a lanuage"

print(str.rfind('is'))


#output:
7
'''

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 31.rindex()	Searches the string for a specified value and returns the last position of where it was found
'''
str = "python is a "

print(str.rindex('is'))


#output:
7
'''

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 32.rstrip():Returns a right trim version of the string
'''
str = "    python       "
print(str.rstrip())


#output:
   python
'''


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 33.split():Splits the string at the specified separator, and returns a list
'''
str  = "tagoor"

print(str.split())

#output:
['tagoor']
'''

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#34.startswith():Returns true if the string starts with the specified value
'''
str = "python"

print(str.startswith('p'))

#output:
True
'''

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 35.title():Converts the first character of each word to upper case
'''
str  ="python"

print(str.title())

#output:
Python
'''
