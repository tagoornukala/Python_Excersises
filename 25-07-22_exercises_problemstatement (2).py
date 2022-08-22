#Task Form Team:1

# 1.WAP for eligibility of a canditate voter_id,
# suppose age between (18 to 80 years old) using flow control conditions?
'''
age = int(input("Enter The Age:"))

if (age >= 18) and (age <=80):
    print("The Canditate Eligibility For Vote")
else:
    print("The Canditate Not Eligible For Vote")

#output:
Enter The Age:18
The Canditate Eligibility For Vote

Enter The Age:15
The Canditate Not Eligible For Vote
'''
#---------------------------------------------------------------------------------------------------------------------

#2.WAP for calculating student marks in 5-subjects,and find  grades,(suppose grade A,B,C and Fail)?
'''
telugu = int(input("Enter The Telugu Marks:"))
hindhi = int(input("Enter The Hindhi Marks:"))
english = int(input("Enter The english Marks:"))
maths = int(input("Enter The Maths Marks:"))
sciens = int(input("Enter The sciens Marks:"))

total = telugu+hindhi+english+maths+sciens

avg = total / 500

per = avg * 100

if(telugu >=35 and hindhi>=35 and english >=35 and maths >= 35 and sciens >=35 ):
    print("pass")
    if(per >=70):
        print("the candidate pass with distinction Gratde A")
    elif(per >=60):
        print("the candidate pass with first class Grade B")
    elif(per >=50):
        print("the candidate pass with second class Grade c")
else:
    print("fail")

#output:
Enter The Telugu Marks:90
Enter The Hindhi Marks:48
Enter The english Marks:78
Enter The Maths Marks:65
Enter The sciens Marks:89
pass
the candidate pass with distinction Gratde A


Enter The Telugu Marks:35
Enter The Hindhi Marks:65
Enter The english Marks:78
Enter The Maths Marks:35
Enter The sciens Marks:67
pass
the candidate pass with second class Grade c

Enter The Telugu Marks:55
Enter The Hindhi Marks:65
Enter The english Marks:78
Enter The Maths Marks:79
Enter The sciens Marks:62
pass
the candidate pass with first class Grade B
'''

#----------------------------------------------------------------------------------------------------------------------
#3.WAP for finding  even or odd number using (if .. else ... condition)?

'''
num = int(input("Enter The number:"))

if(num % 2 == 0):
    print("It is a Even Number")
else:
    print("It is a odd number") 


#output:
Enter The number:4
It is a Even Number

Enter The number:9
It is a odd number
'''

#----------------------------------------------------------------------------------------------------------------------

#4.WAP calculating area of a circle, result in positive integers only not in float values
#(hint: pi=3.14,using int() function)?
'''
radius = int(input("Enter the radius of circle:"))

area = 3.14 * radius * radius
print(round(area))

#output:

Enter the radius of circle:15
706
'''

#-----------------------------------------------------------------------------------------------------------------------


#5.WAP for finding  variables A and B are having the same memory location?
'''
a = int(input("Enter The A value:"))
b = int(input("Enter The B value:"))

if(a == b):
    print("If The Memory Location Is Same")
else:
    print("If The Memory Location Is Not Same")


#output:
Enter The A value:10
ENter The B value:10
True

Enter The A value:10
Enter The B value:20
If The Memory Location Is Not Same
'''

#----------------------------------------------------------------------------------


#Problem Task:
#Task From Team-2:
#----------------------------------------------------------------------------------------------
#The provided code stub reads and integer ,n, from STDIN. For all non-negative integers , print .
#i <n ,print i **2.
#Example:
#n=3
#The list of non-negative integers that are less than n=3 is [0,1,2] . Print the square of each
#number on a separate line.
#0
#1
#4
#Input Format:
#The first and only line contains the integer, .
#Constraints:
#1<=n<=20 
#Output Format:
#Print n  lines, one corresponding to each i.
#Sample Input 0:
#
#5
#
#Sample Output 0:
#
#0
#1
#4
#9
#16

num = input("Enter The Number:")
sqr = 0
for i in range(0,int(num)):
    sqr = i ** 2
    print(sqr)


#output:
'''
Enter The Number:5
0
1
4
9
16
'''
























