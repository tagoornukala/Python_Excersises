
#                                   5-Exercises
#                                   -----------


#============================================================================================================================================

#1. WAP to find the target value of 5 in the given list of 1,5,7,8,90,6,and 23 elements?
'''
list=[1,5,7,8,90,6]

t=5

print(t in list)
'''
#============================================================================================================================================

#2. WAP to sort the given list of elements 1,5,7,8,90,6,and 23, without using sort() function?

list=[1,5,7,8,90,6,23]
new_list = []

while list:
    minimum = list[0]
    for x in list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)

print(new_list)
    
#============================================================================================================================================

#3. WAP to calcalte the compound interest of 3 years with the priciple amount of RS:10000 and rate of return is 5 percentage for annum.
#  and display the total amount to pay on  the end of the year.?

'''t = 3
p = 10000
r = 5
CI = 10000*((1+5/100)**3)#formula ci = p*(1+r/100)**t
print(round(CI))
#output:11576'''


#==========================================================================================================================================

#4. WAP to calculate the sum of the given matrix   [[x1,x2,x3],[x4,x5,x6],[x7,x8,x9]], where x1,x2....x9 values must take from command-line
#   arguments?
"""
1 2 3
4 5 6  
7 8 9   

sum is : 45
"""

""" 1 2 3
    4 5 6  
    7 8 9   
sum is : 45   """
'''a = []
for i in range(1,10):
    a.append(i)
s = 0
for i in a:
    s = s+i
print("sum of matrix: ",s)
#output:45
'''

#=============================================================================================================================================

#5. WAP pattern program

"""
     * * * * *
      * * * *
       * * *
        * *
         *
        * *
       * * *
      * * * * 
     * * * * *
"""

a = int(input("enter the value: "))
for i in range(1,a+1):
    if i == 1:
        print("* "*a)
    else:
        space = " "*(i-1)
        print(space+"* "*(a-(i-1)))
for i in range(2,a+1):
    if i ==a:
        print("* "*a)
    else:
        space= " "*(a-i)
        print(space+"* "*(i))
#output:
"""  * * * * *
      * * * *
       * * *
        * *
         *
        * *
       * * *
      * * * * 
     * * * * *     """

#--------------------------------------------------------------------------------------------------------------------------------------------------------------


#Problem statement


#You are required to enter a word that consists of x and y 
#that denote the number of Zs and Os respectively. The input word is considered similar to word zoo if 2 * x = y


#Determine if the entered word is similar to word zoo.

#For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.

#Input format

    #First line: A word that starts with several Zs and continues by several Os.
    #Note: The maximum length of this word must be 20.

    

#Output format

#Print Yes if the input word can be considered as the string zoo otherwise, print No.

#instruction

#if input = zzzoooooo then print "yes".
#if input = zzooo print "no
'''
a = input("enter the word: ")
b = input("enter the word: ")
word = a+b
while(len(word)<20):
    if(word[0]=='z'):
        if(2 * len(a) == len(b)):
            print("yes")
            break
        else:
            print("no")
            break
    else:
        print("the word length is not start with z: ")
        break
else:
    print("the word length is more than 20")

#output:enter the word: zz
#enter the word: oo
#no
#enter the word: zz
#enter the word: oooo
#yes
#enter the word: zzzzzz
#enter the word: oooooooooooooo
#the word length is more than 20
#enter the word: edfg
#enter the word: thu
#the word length is not start with z: 
'''  





























