#exercises given by batch no:-4


# 1.WAP to reverse a number
'''
Number = int(input("Please Enter any Number: "))    
Reverse = 0    
while(Number > 0):    
    Reminder = Number %10    
    Reverse = (Reverse *10) + Reminder    
    Number = Number //10    
     
print("after reversing the number is",Reverse)

#output:
Please Enter any Number: 12345
after reversing the number is 54321

'''


# 2. WAP to count  the number
# occurrence/frequency  of a  each character in a string
'''
string = input("Please enter your own String : ")
char = input("Please enter your own Character : ")

count = 0
for i in range(len(string)):
    if(string[i] == char):
        count = count + 1

print(count)

#output:

Please enter your own String : tagoor
Please enter your own Character : o
2
'''
# 3.WAP  to check length of two string is equal or not
'''
num1 = input("Enter The num1:")
num2 = input("Enter The num2:")

if(len(num1) == len(num2)):
    print("The givne two strings length is same")
else:
    print("The given two string length is not same")


#output:

Enter The num1:tagoor
Enter The num2:ajayku
The givne two strings length is same

Enter The num1:tagoor
Enter The num2:ajay
The given two string length is not same
'''


# 4.Python program to print even numbers up to 100
'''
for i in range(0,100,2):
    print(i)

#output:

0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
'''

#------------------------------------------------------------------------------------------------------------------------------------------------


# 5.Write a program in python to find greatest among three integers

'''
num1 = int(input("Enter The num1:"))
num2 = int(input("Enter The num2:"))
num3 = int(input("Enter The num3:"))

if(num1 > num2) and (num1 > num3):
    largest = num1
elif (num2 > num3) and (num2 > num1):
    largest = num2
else:
    largest = num3
print(largest)


#output:
Enter The num1:10
Enter The num2:20
Enter The num3:30
30
'''


#-----------------------------------------------------------------------------------------------------------------

#Problem Statement given by batch:-1

#Q. Given an integer,n, perform the following conditional actions:
#
#=>If  is odd, print Weird
#=>If  is even and in the inclusive range of  2 to 5 , print "Not Weird"
#=>If  is even and in the inclusive range of 6 to 20, print "Weird"
#=>If  is even and greater than 20, print "Not Weird"
#
##Input Format:
##------------
##
##A single line containing a positive integer, n.
##
##Constraints:
##-----------
##=> 1<=n<=100
##
##Output Format:
##-------------
##
##Print "Weird" if the number is weird. Otherwise, print "Not Weird".
##
##sample input 1:
##------
##    3
##
##output 1:
##------
##    Weird
##
##explanation 1:
##------------
##    n=3
##    n is odd and odd numbers are weird, so print "Weird".
##
##sample input 2:
##------
##    24
##
##------------------------------or------------------------------------------
##output 2:
##------
##    Not Weird
##
##explanation 2:
##------------
##    n=24
##    n>20  and nis even,so it is  print " Not Weird".


n= int(input("Enter The number:"))


if (n % 2 != 0):
    print("Weird")
elif (n % 2 == 0) and (n >= 2) and (n <= 5):
    print("Not Weird")
elif (n % 2 == 0) and (n >= 6) and (n <= 20):
    print("Weird")
else:
    print("Not Weird")


#output:
'''

Enter The number:3
Weird

Enter The number:24
Not Weird
'''
































