
#Solve without using builtin methods:

#1. WAP to print middle charector of the string
'''
string = "python"
print(string[2:4])

#output:
th
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------


#2. WAP to print half reverse of the string 

#Input: KNOWLEDGE
#Output: EGDELKNOW
'''
string = 'KNOWLEDGE'
print(string[-4:]+string[4:5]+string[:4])

#output:
EDGELKNOW
'''

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#3. WAP to remove all the vouels from the given string
'''
string = "tAgOor"

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""

for char in string:
    if char not in vowels:
        result = result + char

print(result)

#output:
tgr
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------

# 4. WAP to insert * in front of every vouels in the string.

#Input: BANANA
#Output: B*AN*AN*A
'''
string = 'BANANA'

for i in string:
    if i == 'A' or i == 'E' or i == 'I' or i =='O' or i == 'U' or i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        print('*'+i,end="")
    else:
        print(i,end="")
#output:
B*AN*AN*A
'''

#------------------------------------------------------------------------------------------------------------------------------------------------

#5. WAP to count number of words in the string.
'''
string = 'DjangoFrameWork'

print(len(string))

#output:
15
'''
#-----------------------------------------------------------------------------------------------------------------------------------------------

#6. WAP to remove extra space from the given string
'''
string = 'D j a n g o F r a m e w o r k'

print(string.replace(" ",''))

#output:
DjangoFramework
'''

#----------------------------------------------------------------------------------------------------------------------------------------------

#7. WAP to insert string in between the given string
#Input: Ojas technologies 
#Output: Ojas innovative technologies 
'''
string = 'ojas technologies'
print('ojas {} technologies'.format('innovative'))

#output:
ojas innovative technologies
'''

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#8. WAP to find the ascci value of given char
'''
string = 'A'
print("The ASCII value of '" + string + "' is", ord(string))

#output:
The ASCII value of 'A' is 65
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------

#9. insert ojas in front of every string
'''
string1 = 'ojas '

string2 = 'innovative'

string3 = 'technologies'

print(string1+string2)
print(string1+string3)

#output:
ojas innovative
ojas technologies
'''

#-------------------------------------------------------------------------------------------------------------------------------------------------

# 10. insert ojas in every extra space in the string
'''
string = 'a dcefgh'
print(string.replace(' ','ojas'))


#output:
aojasdcefgh
'''





