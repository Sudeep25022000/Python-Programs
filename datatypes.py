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
print('Hey! My name is ' + f_name + l_name + ' and I\'m' + str(age) + ' old.')
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
print(full_name[0:])  #go all the way to the end from first string.
print(full_name[:5])  #default 0 till 5
print(
    full_name[-1]
)  # (-) means the string starts printed from the backward like here the bakward string is 'n' and it's printed
print(full_name[::-2])  #will be printed from back to front skipping 2 digits
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
greet2 = greet.replace('BBSR', 'CTC')
print(greet2)

#boolean
name = 'Sudeep'
is_intelligent = False
print(name + ' is genius: ' + str(is_intelligent))
is_intelligent = True
print(name + ' is humble: ' + str(is_intelligent))
print(bool(0))  #retuns False
print(bool(1))  #returns True

#input complications
#birth_year=input('What\'s your birth year: ')#input string is always assigned after getting converted into str format
#current_age = 2020 - int(birth_year)#type casting the birth year to int to perform mathematical operation on it.
#print(f'Your age is {current_age}')

#password checker
#print('*' * 10)# * is printed 10X
#username = input('Username: ')
#password = input('Password: ')
#print(f'{username}, your password, {password}, is {len(password)} letters long')
#Type-2
#username = input('Username: ')
#password = input('Password: ')
#password_len = len(password)
#hidden_password = '*' * password_len
#print(f'{username}, your password, {hidden_password}, is {password_len} letters long')

#Lists
li1 = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 3, 'a', 'b', True, False]
#  Lists are like Arrays.
amazon_cart = ['Mobile', 'Dumbell', 'Beauty']
print(amazon_cart)
print(amazon_cart[2])

#List Slicing
print(amazon_cart[0:2])  #from 0 - 1 not including 2
print(amazon_cart[0::2])  #print all stepping two indexes.
#changing the lists in the cart ie...
amazon_cart[0] = 'Laptop'
print(amazon_cart[0])  #1st index changed to Laptop.
#assigning amazon_cart to a new list named as new_cart ie
new_cart = amazon_cart
#here new_cart is echoed** to amazon_cart ie any changes made will reflect in amazon_cart. We didn't copy. But...we need to copy. Let's ee how below.
new_cart[0] = 'groceries'
print(new_cart)
print(amazon_cart)
#value changes in both the string IMP!!!

#But below we need are copying the value. SO this is how it's done
amazon_cart = ['Mobile', 'Dumbell', 'Beauty']
new_cart = amazon_cart[:]
#above the value is copied ie no change will be reflected in the amazon_cart
new_cart[0] = 'groceries'
print(new_cart)
print(amazon_cart)
#above we saw the value changed is reflected in new_cart but not in amazon_cart

#Matrix: array with another array inside it.
matrix = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
print(matrix)
print(matrix[0][1])  #prints (0,1) array pos value

#adding in to the Arrays by using append()
#append() adds element to the last of the matrix
basket = [1, 2, 3, 4, 5]
basket.append(100)  #1st append or add 100 to the list
new_list = basket  #then, assign basket to new_list; else it may display an error!!
print(basket)
print(new_list)

#insert
basket.insert(
    4, 100
)  #we can insert anywhere. Here we've inserted in position 4 the string 100
#inserts add n increases the len of array
print(basket)

#extend: adds value at end of array
basket = [1, 2, 3, 4, 5]
basket.extend([100])
print(basket)

#pop() ele
basket.pop()  #pops out the last element
new_list = basket.pop(0)  #pops 0th index
print(basket)
print(new_list)  #prints the pop out element.

#remove ele
new_list = basket.remove(4)  #remove 4th ele
print(new_list)

#compile
new_list = basket[:]  #remove the entire new_list
new_list.clear()
print(new_list)

#array.index(): finds the index of the mentioned string in the braces, suppose...
vowel = ['a', 'e', 'i', 'o', 'u']
print('Index of e is: ' + str(vowel.index('e')))
#print('Index of e is: ' + str(vowel.index('e',0,1)))
#above displays error!! because the content 'e' ain't there in the list betwwen 0th and 1th index.

print(
    'd' in vowel
)  #if 'd' is present it would have return true but here as it isn't here then it return false.

#array.count()
print(
    vowel.count('e')
)  # as there is one 'e' it will return the output as 1. Basically returns the number of ocurrances of the string.

#array.sort()
vowel.sort()
print(vowel)
#this will sort the list.

#array.sorted()
vowel.sort()
print(
    sorted(vowel)
)  #doesn't affect the array, ie array remains intact. Does the same as sort()

#copy(): just copies the list for us.
new_vowel = vowel.copy()

#array.reverse():simply reverses the content in the index.
vowel.reverse()
print(vowel)

#Reversing the list using stepover [::-1]
vowel = ['a', 'e', 'i', 'o', 'u']
print(vowel[::-1])  #stepover is -1 ie it prints from the backward direction.

#prints from 1-100
print(list(range(1, 100)))
#Type-2
print(list(range(101)))
#the value of range should be the range ie to be displayed plus 1. Hence it will prnt from 1-100.

#joining the lists into a string
#Type-1
sentence = ' '  #empty string
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'sudeep'])
print(new_sentence)
#Type-2
new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'sudeep'])
print(new_sentence)

#list unpacking
a, b, c, *others, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Unpacked lists mentioned below- ')
print(a)  #prints first item
print(b)  #prints second item
print(c)  #prints third item
print(others)  #prints rest of the items after the thirs item in the list
print(d)  #prints the last string in the item ie 9.
#if there won't hve been any d element then the element or the var 'others' would have print from 4-9, but as there's an element or var after others then it didn't print the last element.

#None = nothing
anyone = None
print('Anyone: ' + str(anyone))

#Dictonary
dictionary = {'a': [1, 2, 3], 'b': 2, 'c': True}

print(dictionary['b'])  #displays the value stored in b ie 2
#displys the way values are assigned to dictionary
print(dictionary)

#Type-2
dictionary2 = [{
    'a': [1, 2, 3],
    'b': 'hello',
    'c': True
}, {
    'a': [4, 5, 6],
    'b': 'hello',
    'c': True
}]
print(dictionary2[0]['a'][2])
#here 0 = 1st braces in dictionary2 Arrays
#here 'a' denotes the 'a' variable.
#here 2 denotes 3rd elemnt in 'a' array

#from dictionary list above to the prev.
print(dictionary['a'][1])
# returns the 'a' var 2nd obj ie 2.

#Developer Fundamental-II
#Till now we have only used string to denote key
#We can use the number and predefined values to denaote the string even. Let's check out how...
dictionary3 = {
    123: [1, 2, 3],
    #[100] : 2,
    #error in this line bcoz it ain't immutable
    True: True
}

print(dictionary3[123])  #Works
#print(dictionary3[100])#ERROR!! Doesn't work. Unhashable type list: this key is not immutable ie the value cannt be changed but a list can be changed.
print(dictionary3[True])  #Works

#Dictonary Word
#Suppose
dictionary4 = {'a': [1, 2, 3], 'b': 2, 'c': True, True: False}
#Case-1
#print(dictionary['d'])
#this will result into an error because there's no 'd' keyword
#Case-2
print(dictionary4.get('d'))
#above won't display an error rather it would display 'none'
#Case-3
print(dictionary4.get('d', 25022000))
#above would display 25022000 as there is no defined keyword in  dictionary4.
#Case-4
#dict build in function

f_name = dict(name='Sudeep')
print(f_name)
#Here name do not need to be kept with quotes as keywords doesn't require quotes when declared under dict() predefined function.

print('a' in dictionary4)  #true
print('d' in dictionary4)  #false
#return true if exist else false.

#keys()
print('a' in dictionary4.keys())  #returns true as 'a' is a keyword
print(2 in dictionary4.
      keys())  #returns false as '2' is a value in 'b' not a keyword

#values()
print('b' in dictionary4.values())  #returns false as 'b' is a keyword
print(2 in dictionary4.values())  #returns true as 2 is a value in 'b'.

#items()
print(dictionary4.items())
#as items represent all included so we write in this way.

#Let's confuse
print('TRUE' in dictionary4.keys())  #False

print('TRUE' in dictionary4.items())  #False

#clear()
#dictionary4.clear()#clears content in the list
#print(dictionary4)

#copy()
dictionary5 = dictionary4.copy()  #copies one list to other
print(dictionary5)

#pop()
print(
    dictionary5.pop(True)
)  #displays the pop items of the key popped(mostly pops the last ele or keys and values).
#Type-2
print(dictionary5.popitem())
#randomly pops a keys and values

#update()
print(dictionary5.update({'c': 20}))
print(dictionary5)  #prints the updated list
#updates the value of c = 20

#Tuple
my_tuple = (1, 2, 3, 4, 5)
#my_tuple[1] = 'z'#ERROR!! Because tuple doesn't support assignment.
print(my_tuple[1])  #printing a tuple

#Normal dictionary
user = {
    'a': ['a', 'b', 'c'],
    'ABC': ['A', 'B', 'C'],
    123: [1, 2, 3],
    False: False,
    age: 20
}

#Let's dictionary using tuple
user_tuple = {
    'a': ['a', 'b', 'c'],
    'ABC': ['A', 'B', 'C'],
    (1, 2): [1, 2, 3],
    False: False,
    age: 20
}
print(user_tuple[(1, 2)])
#tuple is same as lists.

#tuple has two methods
#count()
#index()

my_tuple = (1, 2, 3, 4, 5, 5)

print(my_tuple.count(5))  #displays 2 as there are 2 5's in the tuple

print(
    my_tuple.index(5)
)  #displays 4 as there are 2 5's in the tuple and pos of 1st 5 is 4th pos.

print(len(my_tuple))
#displays the len of the my_tuple ie 6

#set datatype and data structure
#set : unorder collection of unique objects. represented within curly braces
my_set = {1, 2, 3, 4, 5, 5}
print('Length of org set is: ' + str(len(my_set)))  #prints len of original set
print(
    my_set
)  #As set is a unique collection of objects hence here n my_set we have two nos of '5' and as 5 = 5 hence it will only display one 5 in time
# we cann't add multiple same values in the set even though we are able to add 100.my_set

my_set.add(100)
my_set.add(2)  #doesn't even add 2 as there is a 2 present in the set.
print('Length of org set is: ' + str(
    len(my_set)))  #prints len of set after addition
print(my_set)

#Given a list of repeated element, print it in such a way that elemnts don't repeat.
my_list = [1, 2, 2, 3, 4, 5, 5]
print(my_list)  #prints repeated element
print(
    set(my_list)
)  #On conversion to set it discards the repeated element and pritns the list

my_set = {1, 2, 2, 3, 4, 5, 5}
#print(my_set[0])#ERROR!! Cann't access

print(list(my_set))  #covertion of set to list

#methods of set
my_set = {1, 2, 2, 3, 4, 5, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

#difference()
print(my_set.difference(your_set))
#shows the difference between two sets ie which element are same in my_set get discarded and the rest others which ain't present are diplayed.

#discard(X):discards X from the set.
print(my_set.discard(5))
print(my_set)

#difference_update(X):X is removed
print(my_set.difference_update(
    your_set))  #here 4,5 will be removed as it is present in the ypur_set
print(my_set)

#set.intersection
my_set = {1, 2, 2, 3, 4, 5, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
print(my_set.intersection(
    your_set))  #displays the common element in both the set

#set.isdisjoint()
print(my_set.isdisjoint(your_set)
      )  #displays True if the set doesn't have any common element else False

#.issubset()
print(my_set.issubset(your_set)
      )  #If my_set is the subset of your_set then it returns true else False

#.issuperset()
print(my_set.issuperset(your_set)
      )  #If my_set is the superset of your_set then it returns True else False

#.union()
print(my_set.union(your_set))  #returns the union of two sets
#Deletes duplicate and returned new txt
#Type-2
print(my_set | your_set)

#.intersection()
print(my_set & your_set)

#Boolean
is_old = False
is_license = True

#below condition checks True.
if is_old:
    print('You are old enough to drive a car.'
          )  #stmnt comes under if condition. Here indentation matters.

#else if condition
elif is_license:
    print('You are not old enough to carry a license.')

#below condition checks or outputs the False condition.
else:
    print('You can\'t drive a car and rush to RTO for your license.')

print('checked')  #independent stmt

#converting & into a statement
if is_old and is_license:
    print('You can\'t drive')  #because is_old is False and is_licence is True

#THE ABOVE INDENTATION IS FOR THE COMPILER/INTERPRETER TO UNDERSTAND THAT THE CONTENT IS WITHIN THE PARTICAL CONDITON

#Thruthy and Falsy
#Thruthy value
is_cond1 = bool(True)
is_cond2 = bool('abc')
is_cond3 = bool(5)
is_cond4 = bool(False)
is_cond5 = bool(0)
is_cond6 = bool(-5)
is_cond7 = bool(None)

print(is_cond1)
print(is_cond2)
print(is_cond3)
print(is_cond4)
print(is_cond5)
print(is_cond6)
print(is_cond7)

#Ternary operator
#cond_if_true if cond else cond_if_else
is_friend = True  #condition is true
can_message = 'message allowed' if is_friend else 'message not allowed'

print(can_message)  #as the condition is true hence it prints message allowed

#Short Circuiting
is_friend2 = True
is_user2 = False
#and operator
print('Result: ' + str(is_friend2 and is_user2)
      )  #boolean value has also to be converted into string before printing.
#or operator
print(is_friend2 or is_user2)

#logical operator
print(str(4 == 5))
print('a' > 'A')
print(1 < 2 > 3 < 4)

#using not : prints opposite to the input given
print(not (True))

#Some test case-
print('Test cases-\n')
print(True == 1)
print('1' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

#Module 4.9 --- IMPORTANT
print('\n')
#print(True is 1)  #replace 1 with True for dsplaying result as True
#print('1' is 1)  #replace 1 with '1' the value will go true
#print([] is 1)  #replace 1 with [] as both are same ie empty list and same m/m locataion
print(10 is 10.0)  #
print([] is [])

# '=' checks for the equality in value
# 'is' checks whether the location in m/m where the value is stored is same or not'

#Loops
for item in 'Welcome to BBSR.':
    print(item)
    #remember to align properly.

#iterable - list, tuples, set, string, dictionary.
#for list
for item in [1, 2, 3, 4, 5]:
    print(item)
print('\n')
#for set
for item in {1, 2, 3, 4, 5}:
    print(item)
print('\n')
#for tuple
for item in (1, 2, 3, 4, 5):
    print(item)
print('\n')

#multiline loops
for item in (1, 2, 3, 4, 5):
    print('\n')
    for ch in ['a', 'b', 'c']:
        print(item, ch)

print('\n')

#items(), values(), keys() iterate over dictonary. Below are examples.

user = {'name': 'Sudeep', 'age': 20, 'is_undergraduate': True}

for item in user.items():
    print(item)

print('\n')

for item in user.values():
    print(item)

print('\n')

for item in user.keys():
    print(item)

print('\n')

#Type-1 of printing the key and value
for item in user.items():
    key, value = item
    print(key, value)

print('\n')

#Type-2
for key, value in user.items():
    print(key, value)

print('\n')

#iterating a list using counter variable
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0
for item in my_list:
    counter = counter + item
print('Sum: ', str(counter))  #printing the sum of element in the array
print('\n')
#range(x,y,z):creates a special kind of object to iterate over. x =starting string, y=end string, z=stepover
#printing from foreward ie 0-10
for number in range(0, 10, 1):
    print('Person: ', str(number))
#The last index is not included ie 10.
print('\n')
#printing from backwward ie 10 - 0
for number in range(10, 0, -1):
    print('Person: ', str(number))
#The last index is not included ie 0.

#enumerate: is usefull if we need index count alongisde printing the output
for i, char in enumerate('Hello!!'):
    print(i, char)

for i, char in enumerate(list(range(100))):
    print(i, char)
    if char == 50:
        print(f'index of 50 is:', i)

#while Loop
i = 0
while i < 50:
    print(i)
    i = i + 1

else:
    print('done with all the work'
          )  #This case pops in console when condition is 50.

my_list = [1, 2, 3, 4]
for item in my_list:
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i = i + 1

#break, continue and pass are even included in python

#GUI - Caution: not!! Working
picture = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0]]
#iterate over picture
#if 0-> print empty space
#else if 1 -> print *

for image in picture:
    for pixel in image:
        if (pixel == 1):
            print('*', end='')
        else:
            print(' ', end='')
    print('')

#check for duplicates
a_list = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'd',
    'a',
]

duplicate = []
for value in a_list:
    if a_list.count(value) > 1:
        #this will print all the duplicate even the multiple repeated value will be displayed but...
        if value not in duplicate:
            #this displayes the only values which are duplicated.
            duplicate.append(value)

print(duplicate)

#Function


def say_hello():
    #function defined
    print('Function called: hello')  #function operation performed


say_hello()  #function call


def func1(a, b):  #parameter passed
    print('Sum: ', str(a + b))  #operation performed


func1(30, 40)  #arguements passed

a = 10
b = 20
func1(a, b)

#EEEEEEEEEEEEEERRRRRRRRRRROOOOOOOOORRRRRRRRRR!!
#4.22


def func2(f_name, l_name):
    print(f'Hello!! {f_name} {l_name}')


func2('Hello', ' World')


def sum(num1, num2):
    print(f'Sum: {num1} + {num2}')


sum(10, 20)


#return statement
def sum(num1, num2):
    return (num1 + num2)


print(f'Function returns: {sum(40,15)}')

#if not returned in the above case then it would have return none.


def sum(num1, num2):
    def another_func(num1, num2):
        return (num1 + num2)

    return another_func(
        num1, num2)  #without this statement the value return will be none
    return 5  #doesn't print this because this line exceeds the function
    print('hello'
          )  # doesn't print because this line is excedded out of the function


total = sum(29, 20)
print(f'Total: {total}')

#Methods vs Funcions
#list()
#print()
#max()
#min()
#input()


#Docstring
def test(a):
    '''
  Info: This function tests and prints param a
  '''
    print(a)


test('!!!!')  #prints output
help(test)  #whatever is printed within tripple quote it is printed
print(test.__doc__)  #same thing as above.


#clean code
def is_odd_or_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(f'is_odd_or_even: {is_odd_or_even(25)}')

def highest_even(li):
  evens = []
  for items in li:
    if items % 2 == 0:
      evens.append(item)
  return max(evens)
print(f'Ans: {highest_even([10,2,3,1,8,11])}')

#OOP
class BigObj:
  pass
  
obj1 = BigObj()
print(type(obj1))

