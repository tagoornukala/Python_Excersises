# 1.Accept 10 numbers from the user and display their average.
'''
sum = 0
for i in range(1,11):
    num = int(input("Enter The number:"))
    sum+=num
avg = sum /10
print(avg)


#output:
Enter The number:10
Enter The number:20
Enter The number:30
Enter The number:40
Enter The number:50
Enter The number:60
Enter The number:70
Enter The number:80
Enter The number:60
Enter The number:20
44.0
'''

# 2.Write a program to display sum of odd numbers and even numbers
#that fall between 12 and 37(including both numbers)
'''
even = 0
odd = 0
for i in range(12,37+1):
    if (i % 2 == 0):
        even+=i
    if (i % 2 != 0):
        odd+=i
print("The sum of even numbers is",even)
print("The sum of odd numbers is",odd)
    
#output:
The sum of even numbers is 312
The sum of odd numbers is 325
'''

#3.Write a program to display all the numbers which are divisible by 11 but not by 2 between 100 and 500.
'''

for i in range(100,500):
    if (i % 11 == 0) and (i % 2 != 0):
        print(i)
#outout:
121
143
165
187
209
231
253
275
297
319
341
363
385
407
429
451
473
495
'''


# 4.Write a program to print numbers from 1 to 20 except multiple of 2 & 3
'''
num = int(input("Enter The number:"))

for i in range(1,num+1):
    if(i % 2 != 0) and (i % 3 !=0):
        print(i)


#output:

Enter The number:20
1
5
7
11
13
17
19
'''

# 5.Write a program that keep on accepting number from
# the user until user enters Zero. Display the sum and average of all the numbers.
'''
sum = 0
for i in range(1,10+1):
    num = int(input("Enter the "))
    if num == 0:
        break
    sum+=num
print("sum",sum)
avg = sum / i
print(avg)


#output:

Enter the 10
Enter the 20
Enter the 30
Enter the 0
sum 60
15.0
'''
        
# 6.Write a program to accept decimal number and display its binary number.
'''
def decimal_convertion(num):
    if (num > 1):
        decimal_convertion(num // 2)
    print(num % 2)
num = int(input("Enter The number"))
decimal_convertion(num)

#output:

Enter The number25
1
1
0
0
1

'''

# 7.Convert the following loop into for loop : 

##x = 4 
##
##while(x<=8):
##    print(x*10)
##    x+=2 

'''
for i in range(4,9,2):
    print(i*10)
#output:
40
60
80

'''

# 8.What is nested loop?
'''
In python,A loop inside the loop is called a nested loop

'''


# 9.Write a program to convert temperature in Fahrenheit to Celsius.
'''
temp = int(input("Enter The Fahrenheit:"))

celsius = ((temp-32)*5)/9

print("The temperature in celsius is:",celsius)

#output:
Enter The Fahrenheit:24
The temperature in celsius is: -4.444444444444445
'''


# 10.Write a Python program to get the Fibonacci series between 0 to 50.  

#Note : The Fibonacci Sequence is the series of numbers : 
#
#0, 1, 1, 2, 3, 5, 8, 13, 21, .... 
#
#Every next number is found by adding up the two numbers before it. 
#
#Expected Output : 1 1 2 3 5 8 13 21 34 
#

'''
x = 0
y = 1

while (y <50):
    print(y)
    x,y = y,x+y
    
#output:

1
1
2
3
5
8
13
21
34
'''


# 11.Write a Python program which iterates the integers from 1 to 50.
#For multiples of three print "Fizz" instead of the number and for the multiples of
#five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz". 

##Sample Output : 
##
##fizzbuzz 
##
##1 
##
##2 
##
##fizz 
##
##4 
##
##Buzz 

'''
for i in range(51):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
        continue
    elif ( i % 3 == 0):
        print("Fizz")
        continue
    elif (i % 5 == 0):
        print("Buzz")
        continue
    print(i)

#output:
FizzBuzz
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
'''


# 12.Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. 

#Note : Use 'continue' statement. 

#Expected Output : 0 1 2 4 5 
'''
for i in range(0,6):
    if (i == 3) or (i == 6):
        continue
    print(i,end=' ')
        
#output:

0 1 2 4 5
'''

#-------------------------------------------------------------------------------------------------------------------------
#Pattern Programs.

# 1.Write a program to print the following Patterns
#  1 2 3 4 5 
#  1 2 3 4 5  
#  1 2 3 4 5 
#  1 2 3 4 5 
#  1 2 3 4 5


'''
for row in range(1,6):
    for col in range(1,6):
        print(col,end=" ")
    print()

#output:

1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5

'''


# 2.Write a program to print the following Pattern
#  5 4 3 2 1 
#  5 4 3 2 1
#  5 4 3 2 1
#  5 4 3 2 1
#  5 4 3 2 1

'''
for row in range(5,0,-1):
    for col in range(5,0,-1):
        print(col,end=' ')
    print()


#output:

5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
'''

# 3.Write a program to print the following Pattern
 # 5 5 5 5 5 
 # 4 4 4 4 4 
 # 3 3 3 3 3 
 # 2 2 2 2 2 
 # 1 1 1 1 1
'''
for row in range(5,0,-1):
    for col in range(5,0,-1):
        print(row,end=" ")
    print()

# output:
5 5 5 5 5 
4 4 4 4 4 
3 3 3 3 3 
2 2 2 2 2 
1 1 1 1 1
'''

# 4.Write a program to print the following Pattern
#  1
#  1 2
#  1 2 3
#  1 2 3 4
#  1 2 3 4 5
'''
for row in range(1,6):
    for col in range(1,row+1):
        print(col,end=" ")
    print()

#output:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''

# 5.Write a program to print the following Pattern
#  1 
#  2 2 
#  3 3 3 
#  4 4 4 4 
#  5 5 5 5 5
'''
for row in range(1,6):
    for col in range(1,row+1):
        print(row,end=' ')
    print()

# output:
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
'''

# 6.Write a program to print the following Pattern
#  1 
#  2 3  
#  4 5 6 
#  7 8 9 10 
#  11 12 13 14 15
'''
num = 1
for row in range(1,6):
    for col in range(1,row+1):
        print(str(num)+" ",end='')
        num+=1
    print()

#output:
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15

'''

# 7.Write a program to print the following Pattern
#  5 
#  4 4 
#  3 3 3 
#  2 2 2 2 
#  1 1 1 1 1
'''
for row in range(5,0,-1):
    for col in range(6,row,-1):
        print(row,end=" ")
    print()

#output:
5 
4 4 
3 3 3 
2 2 2 2 
1 1 1 1 1 
'''

# 8.Write a program to print the following Pattern
#  1 
#  2 3 
#  3 4 5 
#  4 5 6 7 
#  5 6 7 8 9 
'''
for row in range(1,6):
    for col in range(1,row+1):
        print((row+col)-1,end=' ')
    print()

#output:

1 
2 3 
3 4 5 
4 5 6 7 
5 6 7 8 9
'''

# 9.Write a program to print the following Pattern
#  A 
#  B C
#  D E F
#  G H I J
#  K L M N O
'''
count = 65
for row in range(1,6):
    for col in range(1,row+1):
        print(chr(count),end=" ")
        count+=1
    print()

#output:

A 
B C 
D E F 
G H I J 
K L M N O 
'''

   
# 10.Write a program to print the following Pattern
#   * * * * * 
#   * * * * * 
#   * * * * * 
#   * * * * * 
#   * * * * * 

''''
for row in range(1,6):
    for col in range(1,6):
        print('*',end=' ')
    print()

#output:
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 

'''


# 11.11.Write a program to print the following Pattern
#   * 
#   * * 
#   * * * 
#   * * * * 
#   * * * * *
'''
for row in range(1,6):
    for col in range(1,row+1):
        print('*',end=' ')
    print()


#output:
* 
* * 
* * * 
* * * * 
* * * * *

'''


# 12.Write a program to print the following Pattern
#    * * * * * 
#    *       * 
#    *       * 
#    *       * 
#    * * * * * 

'''
n = 5
for row in range(1,n+1):
    for col in range(1,n+1):
        if(col == 1 or col == n) or (row == 1 or row == n):
            print('*',end="")
        else:
            print(" ",end="")
    print()

# output:

*****
*   *
*   *
*   *
*****
'''



# 13.Write a program to print the following Pattern
#          * 
#        * * * 
#      * * * * * 
#    * * * * * * *
'''
num = 1
for row in range(4,0,-1):
    for col in range(row,0,-1):
        print(' ',end=' ')
    print(' *'*num)
    num+=2


#output:
               
         *
       * * *
     * * * * *
   * * * * * * *
'''

# 14.Display Multiplication Table in given range using Nested for loops
'''
for rows in range(1,11):
       for columns in range(1,11):
           print(rows*columns," ",end="")
       print("")

#output:
1  2  3  4  5  6  7  8  9  10  
2  4  6  8  10  12  14  16  18  20  
3  6  9  12  15  18  21  24  27  30  
4  8  12  16  20  24  28  32  36  40  
5  10  15  20  25  30  35  40  45  50  
6  12  18  24  30  36  42  48  54  60  
7  14  21  28  35  42  49  56  63  70  
8  16  24  32  40  48  56  64  72  80  
9  18  27  36  45  54  63  72  81  90  
10  20  30  40  50  60  70  80  90  100

'''
    
    
# 15.Display Prime Numbers in the given range using nested for loops
'''
for i in range(2,100):
    for j in range(2,i):
        if (i % j) == 0:
            break
    else:
        print(i,end=' ')

#output:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
'''
# 16.Write a program to print the following Pattern
##                 1
##              3  2
##            6 5  4
##        10  9 8  7




# 17.Write a program to print the following Pattern
##10  9  8   7
##      6   5  4
##           3  2
##               1



        
                   


