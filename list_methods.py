#list methods:

# 1.append():Adds An element at the end of the list
'''
lst = ['one','two','three','four']

lst.append('five')
print(lst)


#output:
['one', 'two', 'three', 'four', 'five']


lst1 = ['apple','banana','cherry']
lst2 = ['ford','bmw','audi']

lst1.append(lst2)

print(lst1)

#output:
['apple', 'banana', 'cherry', ['ford', 'bmw', 'audi']]
'''

#-----------------------------------------------------------------------------------------------------------------------------

# 2.clear():remove an element at the end of the list
'''
lst = [1,2,3,4,5,6]

lst.clear()
print(lst)

#output:
[]
'''

#---------------------------------------------------------------------------------------------------------

# 3.copy():returns a copy of the list
'''
lst = [10,20,30,40,55,66]

lst1 = lst.copy()
print(lst1)

#output:
[10, 20, 30, 40, 55, 66]

'''

#--------------------------------------------------------------------------------------------------------------------

# 4.count():returns the number of elements with the specified value
'''
x = [20,14,5,22,63,45,12]
print(x.count(12))

#output:
1
'''


#--------------------------------------------------------------------------------------------------------------------------------------

# 5.extend():Add the elements of a list (or any iterable), to the end of the current list
'''
lst = [1,4,5,2,6,2,4,5,6,8]
lst2 = [89,55,69,52,63,12,32]


lst.extend(lst2)

print(lst)


#output:
[1, 4, 5, 2, 6, 2, 4, 5, 6, 8, 89, 55, 69, 52, 63, 12, 32]
'''

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 6.insert():adds an element at the specified position
'''
x = ["python","java","php"]

x.insert(2,'c++')

print(x)

#output:
['python', 'java', 'c++', 'php']

'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

# 7.pop():removes the element at the specified position
'''
lst = [1,2,3,4,5,6,7,8]

lst.pop()
print(lst)

#output:
[1, 2, 3, 4, 5, 6, 7]
'''
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

# 8.remove():remove the first item with the specified value
'''
lst = [55,66,77,88,99,55,66,33,11]

lst.remove(55)

print(lst)

#output:
[66, 77, 88, 99, 55, 66, 33, 11]
'''




