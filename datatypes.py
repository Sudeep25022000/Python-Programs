#Fundamental Data Types in Python
#int
#float
#bool
#str
#list
#tuple
#set
#dict
#complex


#Classes -> Custom Data Types

#Specialized Data Types

#None: absence of value

#printing type of output
print(type(2+4))#<class 'int'>
print(type(2-4))#<class 'int'>
print(type(2*4))#<class 'int'>
print(type(2/4))#<class 'float'>
print(type(20+0.44))#<class 'float'>
print(2 ** 3)#ie 2^3=8
print(2 // 4)#0
print(type(2 // 4))#<class 'float'>
print(5 // 4)#1
print(bin(5))#returns binary num ie 0b101
print(int('0b101',2))#returns decimal and 2 here is for binary num

#math function
print(round(3.1))#3
print(round(3.9))#4
print(abs(-20))#20

#order of precedence in python basics
# ()
# ** power
# * /
# + -

#multiple declairation
a,b,c = 1,2,3
print(a);
print(b);
print(c);
#output
#1
#2
#3

#storing and operating
diff = a/b
print(diff)
# we can only concatinate str with str.
#long string - 
#tripple quote to use multiline display
long_string = '''
WOW
0 0
___
'''
print(long_string)
#concatinating two strings - only works with string. No int float ...
f_name = 'Sudeep'
l_name = 'Swain'
full_name = f_name + ' ' + l_name
print(full_name)

#typecasting
print(type(str(100.12)))
print(type(int(str(100))))
#print(type(int(str(100.20)))) error!!
a = str(100)
b = int(a)
c = type(b)
print(c)

#escape sequence
weather = 'It\'s sunny'
#here so as to print 's we need \' which is the escape sequence. ie whatever comes after \ it's gonna accept the string whatever comes after  this.
print(weather)
#\t = tab before printing
#\n = new license

#Formatted String
f_name = 'Sudeep'
l_name = 'Swain'
age = 20
print('Hey! My name is ' + f_name + l_name +' and I\'m' + str(age) + ' old.')
#str(age) because the print can only concatinate strings together.
#Type - 2
print(f'Hey! My name is {f_name} {l_name} and I\'m {age} old.')
#Type - 3
print('Hey! My name is {} {} and I\'m {} old.'.format(f_name, l_name, age))
#Type - 4 The nos indicate the value passed as parameter
print('Hey! My name is {1} {0} and I\'m {2} old.'.format(f_name, l_name, age))
#display a char in a string
full_name = 'Sudeep Rn Swain'
print(full_name[5])

#print a selected nos of string
#[start:stop]         
print(full_name[0:8])

#[start:stop:stepover]
      #default stepover is 1 bcoz we are jummping 1 by 1. 
#here stepover is 2 ie jumps strings by 2.
print(full_name[0:8:2])
print(full_name[0:])#go all the way to the end from first string.
print(full_name[:5])#default 0 till 5
print(full_name[-1])# (-) means the string starts printed from the backward like here the bakward string is 'n' and it's printed
print(full_name[::-2])#will be printed from back to front skipping 2 digits
#full_name[0] = 'B'#error!!, because we cann't change the value in the string; the only way is to re-assign.

#len()-used to find the len of the string.
print(len('Hello'))
#Type-2
greet = 'Hello! Welcome to BBSR'
print(greet[0:len(greet)])

#upper() makes string CAPTALIZE
#Type-1
print(greet.upper())
#Type-2
print(greet.capitalize())

#lower
print(greet.lower())

#find()-finds the position
print(greet.find('to'))

#replace('s1','s2')- replaces the string with the given string. First string is the word to be replaced and the second string is the word that has to be written to be replace.
greet2 = greet.replace('BBSR','CTC')
print(greet2)

#boolean
name = 'Sudeep'
is_intelligent = False
print(name + ' is genius: ' + str(is_intelligent))
is_intelligent = True
print(name + ' is humble: ' + str(is_intelligent))
print(bool(0))#retuns False
print(bool(1))#returns True

#input complications
birth_year=input('What\'s your birth year: ')#input string is always assigned after getting converted into str format
current_age = 2020 - int(birth_year)#type casting the birth year to int to perform mathematical operation on it.
print(f'Your age is {current_age}')











