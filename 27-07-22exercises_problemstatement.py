# exercises given by batch no:3

# 1.Write a program to get all vowels from given string
'''
str = input("enter The string:")
for num in str:
    if (num in 'aeiou'):
        print(num)
#output:

enter The string:tagoor
a
o
o
'''

# 2.Write a program to calculate the simple interest
'''
principel = int(input("Enter The Principle:"))
rate = int(input("Enter The rate of interest:"))
time = int(input("Enter The time period is:"))

si = (principel * rate * time)/100

print("The simple intrest is:",si)

#output:

Enter The Principle:3
Enter The rate of interest:8
Enter The time period is:6
The simple intrest is: 1.44
'''

# 3.Python Program to Find Sum of Series 1 + 1/2 + 1/3 + 1/4 + ……. + 1/N

'''
num = int(input("Enter The num:"))

sum = 0
for i in (1,num+1):
    sum = (1/i)+sum
print("sum",sum)

#output:

Enter The num:5
sum 1.1666666666666667

s=

'''

# 4.Python Program to Find the Sum of the Series 1/1!+1/2!+1/3!+…1/N!
'''
num = int(input("Enter The num:"))

sum = 0
fact = 1

for i in range(1,num+1):
    fact = fact * i
    sum = (1/i)+fact
print("sum",sum)

#output:

Enter The num:5
sum 120.2
'''



# 5.Python Program to Replace All Occurrences of ‘a’ with $ in a String


'''
x = "supraja"

for i in x:
    if(i == 'a'):
        print('$')
    else:
        print(i)
        

#output:

s
u
p
r
$
j
$
'''
#-------------------------------------------------------------------------------------------------

# problem statement given by batch no:4


##Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
##
##You may assume that each input would have exactly one solution, and you may not use the same element twice.
##
##You can return the answer in any order.
##
## 
##
##Example 1:
##
##Input: nums = [2,7,11,15], target = 9
##Output: [0,1]
##Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
##Example 2:
##
##Input: nums = [3,2,4], target = 6
##Output: [1,2]
##Example 3:
##
##Input: nums = [3,3], target = 6
##Output: [0,1]

nums = [2,7,11,15]

target=9

for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if target==(nums[i]+nums[j]):
            print("indices are:",i,j)
'''
output:
indices are: 0 1
'''



















