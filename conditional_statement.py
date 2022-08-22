# 1: Print First 10 natural numbers using while loop
'''
number = int(input("Enter The Number:"))
while (number <= 10):
    print(number)
    number+=1

#output:

Enter The Number:1
1
2
3
4
5
6
7
8
9
10
'''
#------------------------------------------------------------------------------------------------------------------------------------------------

# 2.Calculate the sum of all numbers from 1 to a given number
'''
num = int(input("Enter The Number:"))

total = 0

for i in range(1,num+1):
    total+=i
print("Sum is:",total)

#output:

Enter The Number:10
Sum is: 55
'''

#------------------------------------------------------------------------------------------------------------------------------------------------

# 3.Write a program to print multiplication table of a given number
'''
table = int(input("Enter The Table Number:"))

total = 0
for i in range(1,10+1):
     total = i * table
     print(total)
    
#output:
Enter The Table Number:4
4
8
12
16
20
24
28
32
36
40
'''



#---------------------------------------------------------------------------------------------------------------------------------------------------

# 4.Display numbers from a list using loop

'''

list = [1,2,3,4,5,6]

for i in list:
    print(i)

#output:

1
2
3
4
5
6
'''

#------------------------------------------------------------------------------------------------------------------------------------------------

# 5.Count the total number of digits in a number

'''
num = int(input("Enter The number:"))

count = 0

while num !=0:
    num = num // 10
    count+=1
print(count)

#output:

Enter The number:145698
6

'''

#------------------------------------------------------------------------------------------------------------------------------------------------------

# 6.Print list in reverse order using a loop


'''
list1 = [10,20,30,40,50]

size = len(list1)-1

for i in range(size,-1,-1):
    print(list1[i])

#output:
50
40
30
20
10
'''

#--------------------------------------------------------------------------------------------------------------------------------------------------

# 7.numbers from -10 to -1 using for loopDisplay
'''
for num in range(-10, 0, 1):
    print(num)
    
#output:

-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
'''

#------------------------------------------------------------------------------------------------------------------------------------------------

# 8.Use else block to display a message “Done” after successful execution of for loop

'''
x = "hello world"

for i in x:
    print(i)
else:
    print("done")


#output:


h
e
l
l
o
 
w
o
r
l
d
done

'''


#-----------------------------------------------------------------------------------------------------------------------------------------------

# 9.Write a program to display all prime numbers within a range
'''
num = int(input("Enter The number:"))

for i in range(1,num+1):
    if i > 1:
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
            print(i)
#output:

Enter The number:10
2
3
5
7
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------

# 10.Display Fibonacci series up to 10 terms
'''   
num = int(input("Enter The number:"))

n1 = 0
n2 = 1

count = 0
while count < num:
    print(n1)
    nth = n1+n2
    n1=n2
    n2=nth
    count+=1

#output:

Enter The number:11
0
1
1
2
3
5
8
13
21
34
55

'''

#----------------------------------------------------------------------------------------------------------------------------------------------------

# 11.Find the factorial of a given number

'''
num = int(input("Enter The Num:"))

fact = 1

for i in range(1,num+1):
    fact = fact * i
print("The Factorial of",num,"is",fact)

#output:

Enter The Num:10
The Factorial of 10 is 3628800

'''

#--------------------------------------------------------------------------------------------------------------------------------------------------

# 12.Reverse a given integer number
'''
num = 123456
print(str(num)[::-1])

#output:
654321'''

#--------------------------------------------------------------------------------------------------------------------------------------------------

# 13.Find the sum of the series upto n terms
'''
n= int(input("Enter The number:"))
total = 0
for i in range(1,n+1):
    total+=i
    print(total)

#output:

Enter The number:20
1
3
6
10
15
21
28
36
45
55
66
78
91
105
120
136
153
171
190
210

'''

#--------------------------------------------------------------------------------------------------------------------------

# 14.Calculate the cube of all numbers from 1 to a given number

'''
n = input("Enter The Number:")
qube = 0

for num in range(1,int(n)+1):
    qube = num ** 3
    print(qube)
    
    
#output:

Enter The Number:5
1
8
27
64
125
'''

#-----------------------------------------------------------------------------------------------------------------------

# 15.Use a loop to display elements from a given list present at odd index positions
'''
list = [1,2,3,4,5]

for num in range(0,len(list),2):
    print(list[num])


#output:

1
3
5
'''
#----------------------------------------------------------------------------------------------------------------------

# 16.Name the keyword which helps in writing code involves condition

'''ANS.if,elif,else'''

#----------------------------------------------------------------------------------------------------------------------

# 17.Write the syntax of simple if statement
'''
if condition:
    block_of_code
'''

#---------------------------------------------------------------------------------------------------------------------

# 18.Is there any limit of statement that can appear under an if block.
'''
NO
'''


#-------------------------------------------------------------------------------------------------------------------------

#19.Write a program to check whether a person is eligible for voting or not. (accept age from user)
'''
age = int(input("Enter The Age:"))

if(age >=18):
    print("The Candidate is eligible for the vote")
else:
    print("The Candidate is not eligible for vote")
    
#output:

Enter The Age:14
The Candidate is not eligible for vote
'''

#------------------------------------------------------------------------------------------------------------------------

# 20.Write a program to check whether a number entered by user is even or odd.
'''
num = int(input("Enter The number:"))

if(num % 2 == 0):
    print("The given number is a even number")
else:
    print("The given number is a odd number")

#output:

Enter The number:2
The given number is a even number

'''

#---------------------------------------------------------------------------------------------------------------------

# 21.a program Write to check whether a number is divisible by 7 or not.


'''
num = int(input("Enter The number:"))

if (num % 7 == 0):
    print("The Given number is divisible by 7")
else:
    print("The given number is not divisible by 7")

#output:

Enter The number:14
The Given number is divisible by 7

Enter The number:11
The given number is not divisible by 7
'''

#-----------------------------------------------------------------------------------------------------------------------

# 22.Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".

'''
num = int(input("Enter the num:"))

if (num % 5 == 0):
    print("Hello")
else:
    print("Bye")

#output:

Enter the num:25
Hello

Enter the num:12
Bye

'''

#----------------------------------------------------------------------------------------------------------------------

# 23.Write a program to calculate the electricity bill (accept number of unit from user)
# according to the following criteria :
#    Unit                                                     Price  
#First 100 units                                             no charge
#Next 100 units                                              Rs 5 per unit
#After 200 units                                             Rs 10 per unit
#(For example if input unit is 350 than total bill amount is Rs2000)
'''
nu = int(input("Enter The Number of units:"))
amount = 0

if (nu <= 100):
    print("nocharges")
elif (nu >=100) and (nu <=200):
    amount = (nu-100)*5
    print(amount)
else:
    amount = 500+(nu - 200) * 10
    print(amount)

#output:
Enter The Number of units:95
nocharges

Enter The Number of units:150
250

Enter The Number of units:350
2000
'''

#------------------------------------------------------------------------------------------------------------------------

# 24.Write a program to display the last digit of a number

'''
num=int(input("Enter any number:"))
print("Last digit of number is ",num%10)

#output:
Enter any number:10
Last digit of number is  0

'''
#----------------------------------------------------------------------------------------------------------------------

# 25.Write a program to check whether the last digit of a number( entered by user ) is 
#divisible by 3 or not.

'''
num = int(input("Enter The number:"))

if num % 3 == 0:
    print("The given number is divisible by 3")
else:
    print("The given number is not divisible by 3")

#output:

Enter The number:257
The given number is not divisible by 3

Enter The number:18
The given number is divisible by 3
'''

#--------------------------------------------------------------------------------------------------------------------

# 26.Write a program to accept percentage from the user and display the grade
#according to the following criteria:
#
#        Marks                                    Grade
#         > 90                                        A
#         > 80 and <= 90                              B
#         >= 60 and <= 80                             C
#         below 60                                    D
#
'''
per = int(input("Enter The Percentage:"))

if (per >= 90):
    print("Grade A")
elif (per > 80) and (per <=90):
    print("Grade B")
elif (per >= 60) and (per <=80):
    print("Grade C")
else:
    print("Grade D")

#output:

Enter The Percentage:90
Grade A

Enter The Percentage:83
Grade B

Enter The Percentage:65
Grade C

Enter The Percentage:56
Grade D
'''

#--------------------------------------------------------------------------------------------------------------------

# 27.Write a program to accept the cost price of a bike and
#display the road tax to be paid according to the following criteria :


##   Cost price (in Rs)                                       Tax
##        > 100000                                             15 %
##        > 50000 and <= 100000                                10%
##        <= 50000                                             5%

'''
pr = int(input("Enter The bike price:"))

if (pr > 100000):
    tax = 15/100*pr
elif (pr > 50000) and (pr <= 100000):
    tax = 10/100*pr
else:
    tax = 5/100*pr
print("The Tax is paid for the bike is:",tax)


#output:
Enter The bike price:150000
The Tax is paid for the bike is: 22500.0

Enter The bike price:100000
The Tax is paid for the bike is: 10000.0

Enter The bike price:60000
The Tax is paid for the bike is: 6000.0
'''

#--------------------------------------------------------------------------------------------------------------------

# 28.Write a program to check whether an years is leap year or not.
'''
year = int(input("Enter The Year:"))

if (year % 4 == 0) and (year != 100):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
    
#output:
Enter The Year:2020
2020 is a leap year

Enter The Year:2021
2021 is not a leap year
'''
#-------------------------------------------------------------------------------------------------------------------------

# 29Write a program to accept a number from 1 to 7 and display the name
#of the day like 1 for Sunday , 2 for Monday and so on.
'''
number = int(input("Enter The number:"))

if (number == 1):
    print("sunday")
elif (number == 2):
    print("monday")
elif (number == 3):
    print("tuesday")
elif (number == 4):
    print("wednesday")
elif (number == 5):
    print("thursday")
elif (number == 6):
    print ("friday")
elif (number == 7):
    print("saturday")
else:
    print("please enter the number b/w 1 to 7")

#output:
Enter The number6
friday
'''

#-------------------------------------------------------------------------------------------------------------------------

# 30.Write a program to accept a number from 1 to 12 and display name of the month
#and days in that month like 1 for January and number of days 31 and so on
'''

num = int(input("Enter The num:"))

if num==1:
    print("January")
    print("No of days is 31")
elif num==2:
    print("February")
    print("No of days is 28")
elif num==3:
    print("March")
    print("No of days is 31")
elif num==4:
    print("April")
    print("No of days is 30")
elif num==5:
    print("May")
    print("No of days is 31")
elif num==6:
    print("June")
    print("No of days is 30")
elif num==7:
    print("July")
    print("No of days is 31")
elif num==8:
    print("August")
    print("No of days is 31")
elif num==9:
    print("September")
    print("No of days is 30")
elif num==10:
    print("October")
    print("No of days is 31")
elif num==11:
    print("November")
    print("No of days is 30")
elif num==12:
    print("December")
    print("No of days is 31")
else:
    print("Please enter number between 1 to 12")

#output:
Enter The num:5
May
No of days is 31
'''

#-----------------------------------------------------------------------------------------------------------------------


# 31.What do you mean by statement?

'''
A statement is an instruction that a Python interpreter can execute.
'''


#----------------------------------------------------------------------------------------------------------------------

# 32.Write the logical expression for the following:
# A is greater than B and C is greater than D

'''
a > b and c > d
'''

#---------------------------------------------------------------------------------------------------------------------

# 33.Accept any city from the user and display monument of that city.
#                  City                                Monument
#                  Delhi                               Red Fort
#                  Agra                                Taj Mahal
#                  Jaipur                              Jal Mahal

'''
city = input("Enter The city:")

if city.lower() == "delhi":
    print("Monument name is:Red Fort")
elif city.lower() == "agra":
    print("Monument name is:Taj Mahal")
elif city.lower() == "jaipur":
    print("Monument name is:Jal Mahal")
else:
    print("please enter the correct city")

#output:

Enter The city:Delhi
Monument name is:Red Fort

Enter The city:Agra
Monument name is:Taj Mahal

Enter The city:jaipur
Monument name is:Jal Mahal
'''
#-------------------------------------------------------------------------------------------------------------------------

# 34.Write the output of the following if a = 9
'''       
if (a > 5 and a <=10):
    print("Hello")    
else:    
    print("Bye")

#output:
Hello

'''
#---------------------------------------------------------------------------------------------------------------------

# 35.Write a program to check whether a number entered is three digit number or not.
'''
num = input("Enter The number")

l= len(num)

if (l == 3):
    print("The given number is 3 digits")
else:
    print("The given number is not 3 digits")


#output:

Enter The number123456
The given number is not 3 digits

Enter The number123
The given number is 3 digits
'''

#----------------------------------------------------------------------------------------------------------------------

# 36.Write a program to check whether a person is eligible for voting or not.(voting age >=18)
'''
age = int(input("Enter the age:"))

if (age >= 18):
    print("The Candidate is eligible for the vote")
else:
    print("The Candidate is not eligible for the vote")



#output:


Enter the age:15
The Candidate is not eligible for the vote

Enter the age:32
The Candidate is eligible for the vote
'''

#---------------------------------------------------------------------------------------------------------------------

# 37.Write a program to check whether a person is senior citizen or not.

'''
age = int(input("Enter THe age:"))

if(age >=60):
    print("The person is senior citizen")
else:
    print("The person is not a senior citizen")

#output:

Enter THe age:60
The person is senior citizen

Enter THe age:55
The person is not a senior citizen

'''

#-----------------------------------------------------------------------------------------------------------------------

# 38.Write a program to find the lowest number out of two numbers excepted from user.

'''
num1 = int(input("Enter The num1:"))
num2 = int(input("Enter The num2:"))

if (num1 > num2):
    print("The lowest number is",num2)
else:
    print("The lowest number is",num1)

#output:
Enter The num1:10
Enter The num2:20
The lowest number is 10

'''

#----------------------------------------------------------------------------------------------------------------------

# 39.Write a program to find the largest number out of two numbers excepted from user.
'''
num1 = int(input("Enter The num1:"))
num2 = int(input("Enter The num2:"))

if (num1 > num2):
    print("The largest number is:",num1)
else:
    print("The largest number is :",num2)


#output:

Enter The num1:20
Enter The num2:10
The largest number is: 20

Enter The num1:10
Enter The num2:20
The lrgest number is : 20

'''
#-----------------------------------------------------------------------------------------------------------------------

# 40.Write a program to check whether a number (accepted from user) is positive or negative.
'''
num = int(input("Enter The num:"))

if (num >= 0):
    print("The given number is positive number")
else:
    print("The given number is negative number")

#output:
Enter The num:15
The given number is positive number

Enter The num:-5
The given number is negative number
'''

#---------------------------------------------------------------------------------------------------------------------

# 41.Write a program to check whether a number is even or odd.

'''
num = int(input("Enter The number:"))

if (num % 2 == 0):
    print("The Given number is even")
else:
    print("The Given number is odd")


#output:
Enter The number:4
The Given number is even

Enter The number:5
The Given number is odd

'''

#------------------------------------------------------------------------------------------------------------------------

# 42.Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.
'''
num = int(input("Enter the number:"))

if (num % 2 == 0) and (num % 3 == 0):
    print("The given number is divisible by both 2 and 3")
else:
    print("The given number is not divisible by both 2 and 3")

#output:

Enter the number:6
The given number is divisible by both 2 and 3

Enter the number:7
The given number is not divisible by both 2 and 3
'''

#---------------------------------------------------------------------------------------------------------------------

# 43.Write a program to find the largest number out of three numbers excepted from user.

'''
num1 = int(input("Enter The num1:"))
num2 = int(input("Enter The num2:"))
num3 = int(input("Enter The num3:"))

if (num1 > num2) and (num1 > num3):
    largest = num1
elif (num2 > num3) and (num2 >num1):
    largest = num2
else:
    largest = num3
print("The largest number is",largest)

#output:
Enter The num1:10
Enter The num2:25
Enter The num3:15
The largest number is 25

Enter The num1:30
Enter The num2:15
Enter The num3:11
The largest number is 30

Enter The num1:10
Enter The num2:25
Enter The num3:45
The largest number is 45
'''

#----------------------------------------------------------------------------------------------------------------------

# 44.Accept the temperature in degree Celsius of water and check whether
# it is boiling or not (boiling point of water in 100 oC.
'''
temp = int(input("Enter The temperature:"))

if (temp >= 100):
    print("Water is boiling")
else:
    print("Water is not boiling")

#output:

Enter The temperature:60
Water is not boiling

Enter The temperature:101
Water is boiling
'''

#------------------------------------------------------------------------------------------------------------------------

# 45.Accept the age of 4 people and display the youngest one and oldest one?
'''
per1 = int(input("Enter The age of person1:"))
per2 = int(input("Enter The age of person2:"))
per3 = int(input("Enter The age of person3:"))
per4 = int(input("Enter The age of person4:"))

if (per1 > per2) and (per1 >per3) and (per1 > per4):
    print("The oldest person is:",per1)
elif (per2 > per3) and (per2 > per4) and (per2 > per1):
    print("The oldest person is:",per2)
elif (per3 > per1) and (per3 > per2) and (per3 >per4):
    print("The oldest person is:",per3)
else:
    print("The oldest person is:",per4)
if (per1 < per2) and (per1 < per3) and (per1 < per4):
    print("The youngest person is:",per1)
elif (per2 < per3) and (per2 < per4) and (per2 < per1):
    print("The youngest person is:",per2)
elif (per3 < per1) and (per3 < per2) and (per3 < per4):
    print("The youngest person is:",per3)
else:
    print("The youngest person is:",per4)

#output:
Enter The age of person1:10
Enter The age of person2:25
Enter The age of person3:36
Enter The age of person4:48
The oldest person is: 48
The youngest person is: 10
'''

#----------------------------------------------------------------------------------------------------------------------

# 46.Accept the following from the user and calculate the percentage of class attended:

#a.     Total number of working days
#
#b.     Total number of days for absent
#After calculating percentage show that, If the percentage is less than 75,
#than student will not be able to sit in exam.
'''
numd = int(input("Enter The number of days:"))
numab = int(input("Enter The number of days absent:"))

per = (numd-numab)/numd*100

if (per >= 75):
    print("The student will be able to write the exams")
else:
    print("The student will not be able to write the exams")

#output:

Enter The number of days:30
Enter The number of days absent:5
The student will be able to write the exams

Enter The number of days:25
Enter The number of days absent:15
The student will not be able to write the exams
'''

#----------------------------------------------------------------------------------------------------------------------

# 47.Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.

#Note :

#An equilateral triangle is a triangle in which all three sides are equal.
#
#A scalene triangle is a triangle that has three unequal sides.
#
#An isosceles triangle is a triangle with (at least) two equal sides.
#
'''

s1 = int(input("Enter first side of triangle:"))
s2 = int(input("Enter first side of triangle:"))
s3 = int(input("Enter first side of triangle:"))


if (s1 == s2 == s3):
    print("It is a equilateral traingle")
elif (s1==s2 and s2!=s3) or (s2==s3 and s2!=s1) or (s1==s3 and s1!=s2):
    print("It is a scalene traingle")
else:
    print("It is a isosceles traingle")



#output:

Enter first side of triangle:10
Enter first side of triangle:10
Enter first side of triangle:10
It is a equilateral traingle


Enter first side of triangle:10
Enter first side of triangle:20
Enter first side of triangle:30
It is a scalene traingle


'''












