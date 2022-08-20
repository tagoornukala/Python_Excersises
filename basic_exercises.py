 # 1.Write a program to find sum of number.
'''
num1 = int(input("Enter The First Number:"))
num2 = int(input("Enter The Second Number:"))
sum = num1 + num2
#By using arthematic operator(+) adding two values

print("The Sum Value IS:",sum)

#output:
Enter The First Number:10
Enter The Second Number:20
The Sum Value IS: 30'''

#---------------------------------------------------------------------------------------------------------------------------------------------------

# 2.WAP to find the number is strong number or not 
'''
n = int(input("Enter The NUmber:"))

num = str(n)
given_num = n
length = len(num)
total = 0

while(length > 0):
    digits = n % 10
    fact = 1
    for i in range(1,digits+1):
        fact = fact * i
    total = total + fact
    n = n//10
    length = length -1
if given_num == total:
    print("the given number is strong")
else:
    print("the given number is not a strong number")

#output:
    enter the number :145
    the given number is strong'''
#--------------------------------------------------------------------------------------------------------------------------------------------------

# 3.Python Program to Find the Square Root
'''
num = int(input("Enter The Number:"))

#By using arthematic operator exponential(**) For Calculating The Power of num.
sqrt = num ** 0.5

print("The Squareroot of",num,'is',sqrt)

#output:
Enter The Number:25
The Squareroot of 25 is 5.0
'''

#---------------------------------------------------------------------------------------------------------------------------------------------------

# 4.Python Program to Calculate the Area of a Triangle
'''
base = int(input("Enter The base value:"))
height = int(input("Enter The Height value:"))

#Formula For area of triangle is height*base//2 
area_of_triangle = height * base // 2

print("The Area of Traingele is:",area_of_triangle)

#output:
Enter The base value:10
Enter The Height value:20
The Area of Traingele is: 100
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

# 5.Python Program to Solve Quadratic Equation
'''
a = int(input("Enter The a value:"))
b = int(input("Enter The b value:"))
c = int(input("Enter The c value:"))

d = b**2-4*a*c
if(d < 0):
    d=-d
    numerator = -b+d ** 0.5
    denominator = 2 * a
    total = numerator/denominator
    print(total)
else:
    numerator = -b+d ** 0.5
    denominator = 2 * a
    total = numerator/denominator
    print(total)
    
#output:
#enter the value :10
#enter the value :20
#enter the value :30
Enter The a value:10
Enter The b value:20
Enter The c value:30
0.4142135623730951   
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------


# 6.Python Program to Swap Two Variables
'''
num1 = 10

num2 = 20

#Lets taking a Temp Varibale by assiging the num1 value

temp = num1
num1 = num2
num2 = temp


print("After Swapping The num1 value is:",num1)
print("After Swapping The num2 value is:",num2)

#output:
After Swapping The num1 value is: 20
After Swapping The num2 value is: 10
'''

#---------------------------------------------------------------------------------------------------------------------------------------------------------

# 7.Python Program to Convert Kilometres to Miles
'''
kilometer = int(input("Enter The Kilometers:"))

#Here 0.621371 mile is equel to 1 kilometer
convertion = kilometer * 0.621371

print("After Convertion of",kilometer,'is equel to',convertion,'miles')

#output:
Enter The Kilometers:2
After Convertion of 2 is equel to 1.242742 miles
'''

#------------------------------------------------------------------------------------------------------------------------------------------------------

# 8.Python Program to Check Leap Year
'''
year = int(input("Enter The Year:"))

# not divided by 100 means not a century year
# year divided by 4 is a leap year

if(year % 4 == 0) and (year % 100 != 0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")

#output:
Enter The Year:2024
2024 is a leap year

Enter The Year:2021
2021 is not a leap year

'''
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------
    
# 9.Python Program to Check Prime Number
'''
num = int(input("Enter The Number:"))

if(num > 1):
    for i in range(2,num):
        if(num % i) ==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is  not a prime number")
    

#output:

Enter The Number:5
5 is a prime number

Enter The Number:9
9 is not a prime number
'''

#------------------------------------------------------------------------------------------------------------------------------------------------------

# 10.Python Program to Find the Factorial of a Number

'''
num = int(input("Enter The number:"))
factorial = 1

for i in range(1,num+1):
    factorial = factorial * i
print("The Factorial of",num,"is",factorial)
    
#output:
Enter The number:10
The Factorial of 10 is 3628800
'''
#------------------------------------------------------------------------------------------------------------------------------------------------

# 11.Python Program to Print the Fibonacci sequence

'''
num = int(input("Enter The number:"))

n1 = 0
n2 = 1
count = 0

while(count < num):
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count+=1


#output:
    
Enter The number:7
0
1
1
2
3
5
8

'''

#------------------------------------------------------------------------------------------------------------------------------------------------

# 12.Python Program to Check Armstrong Number

''''
number = input("Enter The  number:")
sum = 0
for i in number:
    sum += int(i)**3
#print(sum)
number=int(number)
if(number == sum):
    print(number,"is an armstromng number")
else:
    print(number,"is not an armstrong number")

#output:

Enter The  number:153
153 is an armstromng number

Enter The  number:111
111 is not an armstrong number
'''

#------------------------------------------------------------------------------------------------------------------------------------------------

# 13.Python Program to Find Armstrong Number in an Interval

'''
lower = int(input("Enter The lower numbers:"))
upper = int(input("Enter The Upper number:"))


for num in range(lower,upper+1):
    #print(num)
    total =0
    num =str(num)
    for i in num:
        lengt = len(num)
        product = (int(i) ** lengt) 
        total = total + product
    
    if( total == int(num)):
        print(total)

#output:
    
Enter The lower numbers:1
Enter The Upper number:500
1
2
3
4
5
6
7
8
9
153
370
371
407
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------

#14. Python Program to Find the Sum of Natural Numbers
'''
num= input("Enter The Numbers:")
total = 0
for i in range(1,int(num)):
    total += i
print("SUM:",total)


#output:

Enter The Numbers:10
SUM: 45

Enter The Numbers:6
SUM: 15
'''

#----------------------------------------------------------------------------------------------------------------------------------------------

# 15.Python Program to Find the Factors of a Number

'''
num = int(input("Enter The Number:"))

for i in range(1,num+1):
    if (num % i) ==0:
        print("The Factors of",num,"is",i)


#output:

Enter The Number:12
The Factors of 12 is 1
The Factors of 12 is 2
The Factors of 12 is 3
The Factors of 12 is 4
The Factors of 12 is 6
The Factors of 12 is 12

'''

#----------------------------------------------------------------------------------------------------------------------------------------------


# 16.Python Program to Convert Decimal to Binary, Octal and Hexadecimal
'''
def decimal_convertion(num): #num = 34
    if (num > 1):
        decimal_convertion(num//2)
    print(num % 2,end="")
decimal_convertion(34)


#output:

100010

print('\n')

def octal_convertion(num):
    if(num > 1):
        octal_convertion(num//8)
    print(num % 8,end="")
octal_convertion(141)


#output:

0215


def hexdecimal_convertion(num):
    if(num > 1):
        hexdecimal_convertion(num//16)
    print(num % 16,end="")
hexdecimal_convertion(141)

#output:
0813

'''

#------------------------------------------------------------------------------------------------------------------------------------------------

# 17.Python Program to Find LCM
'''
num1 = int(input("Enter The Number1:"))
num2 = int(input("Enter The Number2:"))
if(num1 > num2 ):   # Use If condition to find the greatest number among these two.
    heighest = num1
else:
    heighest = num2
while(True):
    if(heighest % num1 == 0 and heighest % num2 == 0):   
        print(heighest)
        break;
    heighest= heighest+ 1 


#output:

Enter The Number1:10
Enter The Number2:24
120

'''

#------------------------------------------------------------------------------------------------------------------------------------------------

#18.Python Program to Find HCF
'''
num1 = int(input("Enter The Num1 value:"))
num2 = int(input("Enter The Num2 value:"))

if (num1 < num2):
    lowest = num1
else:
    lowest = num2
for i in range(1,lowest+1):
    if(num1 % i ==0) and (num2 % i == 0):
        hcf = i
print(hcf)

#output:
Enter The Num1 value:25
Enter The Num2 value:15
5
    
'''




































