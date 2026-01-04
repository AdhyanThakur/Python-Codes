##### Lambda Functions in Python
#Lambda functions are small anonymous functions defined 
#using the **lambda** keyword. They can have any number of 
#arguments but only one expression. They are commonly used 
#for short operations or as arguments to higher-order functions.

### NOTE- MAP BASICALLY REQUIRES- map(func,*iterables)

## syntax
#lambda arguments: expression

## addition function
#def addition(a,b):
#    return a+b
#print(addition(32,23))    
## by lambda func
#add=lambda a,b:a+b
#print(add(5,5))
## even function
def even(num):
    if num%2==0:
        return True
print(even(24))
## or
even1= lambda num:num%2==0
print(even(27))

## addition of three numbers
def add_three_num(a,b,c):
    return a+b+c
print(add_three_num(12,13,14))
# or
addition1=lambda x,y,z:x+y+z
print(addition1(12,13,12))

## map()- applies a function to all items in a list
numbers=[1,2,3,4,5,6]
def square(number):
    return number**2

square(2)
#or 
list(map(lambda x:x**2,numbers))