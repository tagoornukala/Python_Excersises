#1.
#Calculate income tax for the given income by adhering to the below rules
#Taxable Income    Rate (in %)
#First $10,000    0
#Next $10,000    10
#The remaining    20
#Expected Output:

#For example, suppose the taxable income is 45000 the income tax payable is

#10000*0% + 10000*10%  + 25000*20% = $6000.
'''
a = int(input("enter the salary: "))
if(a>0)and(a<10000):
    print("no income tax")
elif(a>10000)and(a<20000):
    a = a-10000
    r = a*0.01
    print("tax will be: ",r)
elif(a>20000):
   tax_payable = 0
   tax_payable = 10000 * 10 / 100
   tax_payable += (a - 20000) * 20 / 100
print("Total tax to pay is", tax_payable)

#output:
enter the salary: 45000
Total tax to pay is 6000.0
>>> 
'''

#-------------------------------------------------------------------------------------------------------------------------------------------------
# 2.Count the length of list with out using any inbuilt function.
'''
lst = [1,2,5,6,9,88,22]
count = 0
for i in lst:
    count = count+1
print(count)

#output:
7
'''

#----------------------------------------------------------------------------------------------------------------------------------------------
'''
#3.Write a Python program to create a histogram from a given list of integers.

a =[1,3,5,7,8]
for i in a:
    print("x"*i)

#output:

x
xxx
xxxxx
xxxxxxx
xxxxxxxx
'''
#-------------------------------------------------------------------------------------------------------------------------------------------------
#4. Take input from user and if input is string print String

#if input is integer/float print integer
#if input is mix of string and integer print Error
#HINT Can be done using ASCII code
'''
inpt=input("Enter the string ")
int_counter=0
str_counter=0
for i in inpt:
    if ord(i)>48 and ord(i)<57:
        int_counter+=1
    elif (ord(i)>97 and ord(i)<122) or (ord(i)>65 and ord(i)<90) :
        str_counter+=1

if int_counter >0 and str_counter ==0:
    print("Integer")
elif int_counter == 0 and str_counter >0:
    print("String")
else:
    print("Error")

#output:
Enter the string 123456
Integer
'''
#-----------------------------------------------------------------------------------------------------------------------------
#5.Python program to check if a string is palindrome or not'''
'''
ip=input("enter word:")
r=ip[-1::-1]
if r==ip:
    print("palindrome")
else:
    print("not palindrome")
#output:enter word:
enter word:abba
palindrome
'''


#------------------------------------------------------------------------------------------------------------------------------------------------

#2<=n<=10
#0<=marks[i]<=100
#length of marks arrys=3
#The query_name is 'beta'. beta's average score is .
#Input Format
#The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.
#Constraints
#Output Format
#Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
#Sample Input 0
#3
#Krishna 67 68 69
#Arjun 70 98 63
#Malika 52 56 60
#Malika
#Sample Output 0
#56.00
#Explanation 0
#marks for Mallika are{52,56,60} whose average is ((52+56+60)/3)=56
#Marks for Malika are  whose average is 
#Sample Input 1
#2
#Harsh 25 26.5 28
#Anurag 26 28 30
#Harsh
#Sample Output 1
#26.50
#https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
'''
krishna = [67,68,69]
Arjun = [70,98,63]
malika = [52,56,60]
krishna_sum = 67+68+69
krishna_avg = krishna_sum/3
print(round(krishna_avg))
Arjun_sum = 70+98+63
Arjun_avg = Arjun_sum/3
print(round(Arjun_avg/3))
malika_sum = 52+56+60
malika_avg = malika_sum/3
print(round(malika_avg))
if(krishna_avg<Arjun_avg)and(krishna_avg<malika_avg):
    print("the minimal avg of krisha: ",krishna_avg)
elif(Arjun_avg<krishna_avg)and(Arjun_avg<malika_avg):
    print("the minimal avg of Arjun: ",Arjun_avg)
else:
    print("the minimal avg of malika: ",malika_avg)
#output:68
26
56
the minimal avg of malika:  56.0

'''


















