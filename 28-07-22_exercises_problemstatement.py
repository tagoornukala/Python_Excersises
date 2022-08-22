#exercises given by batch no:2

#1.WAP in python arrange string characters
#such that lowercase letters should come first

'''
str = "TaGoOr"

lower = []
upper = []

for char in str:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
str1 = ' '.join(lower+upper)
print(str1)

#output:
a o r T G O
'''
#-------------------------------------------------------------------------------------------------------------------------------------------------
#2.WAP to print sum of prime numbers in given
#list input :- 2 4 5 6 7 3 8 output :- 17
'''
a = [2,4,5,6,7,3,8]
sum = 0
for i in a:
    prime = 0
    for j in range(2,i-1):
        if (i % j == 0):
            prime+=1
    if prime == 0 and i != 1:
        sum+=i
print(sum)
#output:
17
'''
#-----------------------------------------------------------------------------------------------------------------------------------------------
#3.when do we use nested for loop.Write an example.
'''
The "inner loop" will be executed one time for each iteration of the "outer loop":
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    
'''

#-----------------------------------------------------------------------------------------------------------------------------------------
#4.WAP in python remove all characters from a string
#except integers(ex:- STR="H56U1E9JIG3l4w2" ,o/p:-5619342(only display integers) )
'''
a = "H56U1E9JIG3l4w2"
b = ""
for i in a:
    if i.isdigit():
        b+=i
print(b)

#output:
5619342
'''
#----------------------------------------------------------------------------------------------------------------------------------------------
#5.WAP to take a list and find the possition of
#the item .(eg=  [45,12,66,2,33] if i take 66 then it shows the index 2)

'''
list = [45,12,66,2,33]

print(list.index(66))

#output:
2
'''


#------------------------------------------------------------------------------------------------------------------------------------------------------
#Problem statement batch no:3

#Python Program to accept three distinct digits and print all possible combinations from the digits.
#
#Case 1:
#Enter first number:1
#Enter second number:2
#Enter third number:3
#1 2 3
#1 3 2
#2 1 3
#2 3 1
#3 1 2
#3 2 1
#
#Case 2:
#Enter first number:5
#Enter second number:7
#Enter third number:3
#5 7 3
#5 3 7
#7 5 3
#7 3 5
#3 5 7
#3 7 5

'''
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])



#output:
Enter first number:1
Enter second number:2
Enter third number:3
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''













