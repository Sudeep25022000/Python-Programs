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

#password checker
#print('*' * 10)# * is printed 10X
username = input('Username: ')
password = input('Password: ')
print(f'{username}, your password, {password}, is {len(password)} letters long')
#Type-2
username = input('Username: ')
password = input('Password: ')
password_len = len(password)
hidden_password = '*' * password_len
print(f'{username}, your password, {hidden_password}, is {password_len} letters long')

#Lists
li1 = [1,2,3,4,5]
li2 = ['a','b','c']
li3 = [1,2,3,'a','b',True,False]
#  Lists are like Arrays.
amazon_cart = ['Mobile','Dumbell','Beauty']
print(amazon_cart)
print(amazon_cart[2])

#List Slicing
print(amazon_cart[0:2])#from 0 - 1 not including 2
print(amazon_cart[0::2])#print all stepping two indexes.
#changing the lists in the cart ie...
amazon_cart[0] = 'Laptop'
print(amazon_cart[0])#1st index changed to Laptop.
#assigning amazon_cart to a new list named as new_cart ie
new_cart = amazon_cart 
#here new_cart is echoed** to amazon_cart ie any changes made will reflect in amazon_cart. We didn't copy. But...we need to copy. Let's ee how below. 
new_cart[0] = 'groceries'
print(new_cart)
print(amazon_cart)
#value changes in both the string IMP!!!

#But below we need are copying the value. SO this is how it's done
amazon_cart = ['Mobile','Dumbell','Beauty']
new_cart = amazon_cart[:]
#above the value is copied ie no change will be reflected in the amazon_cart
new_cart[0] = 'groceries'
print(new_cart)
print(amazon_cart)
#above we saw the value changed is reflected in new_cart but not in amazon_cart

#Matrix: array with another array inside it.
matrix = [
          [1,2,3],
          [3,4,5],
          [6,7,8]
        ]
print(matrix)
print(matrix[0][1])#prints (0,1) array pos value

#adding in to the Arrays by using append()
#append() adds element to the last of the matrix
basket = [1,2,3,4,5]
basket.append(100)#1st append or add 100 to the list
new_list = basket#then, assign basket to new_list; else it may display an error!! 
print(basket)
print(new_list)

#insert
basket.insert(4,100)#we can intsert anywhere. Here we've inserted in position 4 the string 100
#inserts add n increases the len of array
print(basket)

#extend: adds value at end of array
basket = [1,2,3,4,5]
basket.extend([100])
print(basket)

#pop() ele
basket.pop()#pops out the last element
new_list = basket.pop(0)#pops 0th index
print(basket)
print(new_list)#prints the pop out element.

#remove ele
new_list = basket.remove(4)#remove 4th ele
print(new_list)

#compile
new_list = basket[:]#remove the entire new_list
new_list.clear()
print(new_list)

#array.index(): finds the index of the mentioned string in the braces, suppose...
vowel = ['a','e','i','o','u']
print('Index of e is: ' + str(vowel.index('e')))
#print('Index of e is: ' + str(vowel.index('e',0,1)))
#above displays error!! because the content 'e' ain't there in the list betwwen 0th and 1th index.

print('d' in vowel)#if 'd' is present it would have return true but here as it isn't here then it return false.

#array.count()
print(vowel.count('e'))# as there is one 'e' it will return the output as 1. Basically returns the number of ocurrances of the string.

#array.sort()
vowel.sort()
print(vowel)
#this will sort the list.

#array.sorted()
vowel.sort()
print(sorted(vowel))#doesn't affect the array, ie array remains intact. Does the same as sort()

#copy(): just copies the list for us.
new_vowel = vowel.copy()

#array.reverse():simply reverses the content in the index.
vowel.reverse()
print(vowel)

#
