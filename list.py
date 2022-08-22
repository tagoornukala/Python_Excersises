
#1.Take 10 integer inputs from user and store them in a list and print them on screen.
'''
val = 10

list = []

while val > 0:
    num = int(input("enter The number"))
    list.append(num)
    val = val-1
print(list)

#output:
enter The number1
enter The number2
enter The number3
enter The number4
enter The number5
enter The number6
enter The number7
enter The number8
enter The number9
enter The number10
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
#----------------------------------------------------------------------------------------------------------------------------------------------
#2.Take 10 integer inputs from user and store them in a list.
#Again ask user to give a number. Now, tell user whether that number is present in list or not.
#( Iterate over list using while loop ).
'''
val = 10
lst = []

while val > 0:
    num = int(input("Enter the number:"))
    lst.append(num)
    val = val-1
print(lst)

num1 = int(input("Enter The number:"))
if num1 in lst:
    print("Yes")
else:
    print("no")

#output:
Enter the number:12
Enter the number:25
Enter the number:63
Enter the number:45
Enter the number:78
Enter the number:96
Enter the number:85
Enter the number:45
Enter the number:63
Enter the number:232
[12, 25, 63, 45, 78, 96, 85, 45, 63, 232]
Enter The number:15
no
'''
#------------------------------------------------------------------------------------------------------------------------------------------------
#3.
#Take 20 integer inputs from user and print the following:
#number of positive numbers
#number of negative numbers
#number of odd numbers
#number of even numbers
#number of 0s.
'''
val = 20
lst = []
negitivecount = 0
positivecount = 0
oddcount = 0
evencount = 0
zero = 0
while val > 0:
    num = int(input("Enter The number:"))
    lst.append(num)
    val = val-1
print(lst)

for i in lst:
    if i > 0:
        positivecount = positivecount + 1
for i in lst:
    if i < 0:
        negitivecount = negitivecount + 1
for i in lst:
    if i % 2 == 0:
        evencount = evencount + 1
for i in lst:
    if i % 2 != 0:
        oddcount = oddcount + 1
for i in lst:
    if i == 0:
        zer0 = zero+1
print("Positive:",positivecount,"Negitive:",negitivecount,"Even:",evencount,"odd:",oddcount,"zero:",zero)

#output:
Enter The number:10
Enter The number:25
Enter The number:26
Enter The number:24
Enter The number:13
Enter The number:15
Enter The number:17
Enter The number:-5
Enter The number:-5
Enter The number:-6
Enter The number:-4
Enter The number:-7
Enter The number:-5
Enter The number:23
Enter The number:26
Enter The number:45
Enter The number:96
Enter The number:45
Enter The number:12
Enter The number:12
[10, 25, 26, 24, 13, 15, 17, -5, -5, -6, -4, -7, -5, 23, 26, 45, 96, 45, 12, 12]
Positive: 14 Negitive: 6 Even: 9 odd: 11 zero: 0
>>> 

'''
#-----------------------------------------------------------------------------------------------------------------------------------------------
#4.Take 10 integer inputs from user and store them in a list.
#Now, copy all the elements in another list but in reverse order.
'''
val = 10

lst = []

while val > 0:
    num = int(input("Enter The number:"))
    lst.append(num)
    val = val-1
print(lst)

lst1 = lst
print(lst1[::-1])


#output:
Enter The number:10
Enter The number:20
Enter The number:30
Enter The number:40
Enter The number:50
Enter The number:60
Enter The number:70
Enter The number:80
Enter The number:34
Enter The number:22
[10, 20, 30, 40, 50, 60, 70, 80, 4, 22]
[22, 4, 80, 70, 60, 50, 40, 30, 20, 10]
'''
#---------------------------------------------------------------------------------------------------------------------------------------------------

#5.Write a program to find the sum of all elements of a list.
'''
list = [1,2,3,4,5,6]
print(sum(list))

#output:
21
'''
#---------------------------------------------------------------------------------------------------------------------
#6.Write a program to find the product of all elements of a list.
'''
list = [1,2,3,4,5,6]

product = 1

for i in list:
    product = product * i
print(product)

#output:
720
'''
#---------------------------------------------------------------------------------------------------------------------

#7.Initialize and print each element in new line of a list inside list.
'''
lst = [1,2,3,4,5,6]
b = str(lst)
c = b.split(',')
for i in c:
    print(i,"\n")

#output:
[1 

 2 

 3 

 4 

 5 

 6] 

'''
#-----------------------------------------------------------------------------------------------------------------------
#8.Find largest and smallest elements of a list.
'''
list = [1,5,6,7,8,9,10,2]
print(min(list))
print(max(list))

#output:
1
10
'''
#----------------------------------------------------------------------------------------------------------------------
#9.Write a program to print sum, average of all numbers, smallest and largest element of a list.
'''
list = [11,15,14,12,18,20]
print("sum:",sum(list))
print("avg:",sum(list)/len(list))
print("min:",min(list))
print("max:",max(list))

#output:
sum: 90
avg: 15.0
min: 11
max: 20
'''

#-----------------------------------------------------------------------------------------------------------------------

#10.Write a program to check if elements of a list are same or not it read from front or back. E.g.-
#2	3	15	15	3	2

'''
lst = [2,3,15,15,3,2]
rev = lst[::-1]

if lst == rev:
    print("same")
else:
    print("not same")

#output:
same'''
#--------------------------------------------------------------------------------------------------------------------------

#11.Take a list of 10 elements. Split it into middle and store the elements in two dfferent lists. E.g.-
#INITIAL list :
#58	24	13	15	63	9	8	81	1	78

#After spliting :
#58	24	13	15	63
#9	8	81	1	78
'''
list = [58,24,13,15,63,9,8,81,1,78]
print(list[:5])
print(list[5:])

#output:
[58, 24, 13, 15, 63]
[9, 8, 81, 1, 78]
'''

#-------------------------------------------------------------------------------------------------------------------------

#12.
#Ask user to give integer inputs to make a list. Store only even values given and print the list.
val = 5
lst = []
while val >0:
    num = int(input("enter the number:"))
    if (num % 2 == 0):
        lst.append(num)
    val=val-1
    print(lst)

#output:

    '''
enter the number:1
[]
enter the number:2
[2]
enter the number:5
[2]
enter the number:3
[2]
enter the number:4
[2, 4]
'''
