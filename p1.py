#!/usr/bin/python3
'''
counter = 100
miles = 1000.0
name = "Swamy"

print (counter)
print (miles)
print (name)
'''

'''
a = b = c= 1

print (a)

'''
'''
a,b,c = 1,2,"swamy"

print (c)

'''

'''
var1 = 12
var2 = 13

print (var1)

'''

'''
var1 = 12
var2 = 13

del var1
print (var1)

'''
'''
var1 = 12
var2 = 13

del var1, var2
print (var1)

'''

#Strings
'''
str = 'Hello world'

print  ("Line-1", str)
print ("Line-2",str[0])
print (str[1])

print (str[2:5])

print (str[3:])
print (str * 2)
print (str + "TEST" )

'''

#Python Lists
'''
list = ['abcd', 786 , 2.23, 'samu',70.2]
tinylist = [123,'swamy']
print (list)
print (list[0])
print (tinylist)
print (list + tinylist)

print (list + tinylist)
print (tinylist * 2)
'''

#Tuples in python
'''
tuple = ('abcd', 1234, 'john', 404.5)
print (tuple)
print (tuple[3])
'''

'''
tuple = ('abcd', 1234, 'john', 404.5)
tuple[2] = 2000
print (tuple)
print (tuple[3])
'''

#Dictonary

'''

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values
'''


#Conversion
'''
x = 'swamy'

str(x)

print(x)
'''


#if statement
'''
var1 = 100
if var1:
    print ("1 - got a true expression value")
    print (var1)

var2 = 0
if var2:
    print ("2 - got a true expression value")
    print (var2)

var3 = 20
if var3:
    print ("3 - got a true expreccion value")
    print (var3)
print ("Good bye")

'''


#if else statement
'''
var1 = 00
if var1:
    print ("1 - got a true expression")
    print (var1)
else:
    print ("1 - got a false expression")
    print (var1)

var2 = 30
if var2:
    print ("2 - got true expression")
    print (var2)
else:
    print ("2-got fallse expression")
    print (var2)

print ("good bye")
'''

#elif statement
'''
var = 100
if var == 200:
    print ("1-got true expression")
    print (var)
elif var == 150:
    print ("2-got true expression")
    print (var)
elif var == 100:
    print ("3-got true expression")
    print (var)
else:
    print ("4-got false expression")
    print (var)
print ("Good bye!")
'''

'''
var = 100
if var < 200:
    print ("Expression value is less than 200")
    if var == 150:
        print ("Which is 150")
    elif var == 100:
        print ("which is 100")
    elif var == 50:
        print ("which is 50")
    elif var < 50:
        print ("expression value is less than 50")
else:
    print ("Could not find true expression")
print ("Good bye")

'''


#Python while Loop Statements
'''
count = 0 
while (count < 11 ):
      print ("The count is :",count)
     # print (count)
      count = count + 1
print ("Good bye!")

'''
'''
var = 1 
while var == 1 : # This constructs an infinite loop
    num = input("Enter a number :")
    print ("you entered : ", num)
print ("good bye")

'''



#Using else Statement with While Loop
'''
count = 0 
while count < 5:
    print (count,"is lessthan 5")
    count = count + 1
else:
    print (count, "is not lessthan 5")
'''

#Single Statement Suites

flag = 1
while (flag) : print ('Given flag is really true!') 
print ("Good bye")

#Python for Loop Statements

