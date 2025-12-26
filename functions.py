## a function is a block of a code that perform a specific task. 
# functuions help in organizing code, reusing code and improving 
# readability
## syntax
def function_name(parameters):
    # code block 
    return expression

## why functions are used 
## to find odd or even number 
#num=24 
#if num%2==0:
 #   print("the number is even:",num)
#else:
#    print("the number is odd:",num) 
## we cannot reuse the above code for multiple numbers
# by using functions code can be reused rather not writing the same 
# code again and again
#def check_odd_even(number):
#    """this function checks a number is odd or even""" # docsting 
    #if number%2==0:
   #     print("the number is even:",number)
  #  else:
 #       print("the number is odd:",number)
#a=int(input("eneter the number:"))
#check_odd_even(a)
#check_odd_even(19)
#First, define the function
#Then, take input from the user
#Finally, call the function using that input
## function with multiple parameters
#def sum(a,b):
#    """ this function gives sum of two number"""# docstring
#    return a+b
#result=sum(5,10)
#print(result)    
# default parameters
#def greet(name):
#    """ this function greets the user by name"""# docstring
#    print(f"HELLO,{name} welcome to the programming world!")
#a=input("enter your name:")
#greet(a)

#def greet(name="Guest"):# default parameter
#    print(f"HELLO,{name} welcome to the programming world!")
#a=input("enter your name:")
#greet() #will use default parameter
#greet("ADHYAN")# will use provided argument

## variable length arguments
# POSTIONAL ARGUMENTS AND KEYWORD ARGUMENTS
#def print_numbers(*args):
#    """ this function prints alll the data provided as an argument"""
#    for num in args:
#        print(num)
#print_numbers(11,3,4,5,5,6,4,"mfkn")

## keyword arguments
#def print_detail(**kwargs):##keyword postional arguments 
#    """ this function prints all the key value pairs provided as arguments"""
#    for key,value in kwargs.items():
#        print(f"{key}:{value}")
#print_detail(name="adhyan",age=18,course="bca")        

#def print_detail(*args,**kwargs):# both postional and keyword argument
#    for val in args:
#        print(f"This is a Positonal argument: {val}")
     
#    for key,value in kwargs.items():
#        print(f"{key}:{value}")
#print_detail(1,2,3,4,name="adhyan",age=18,course="bca",)

## return statement
#def multiply(a,b):
#    return a*b
#result=multiply(5,11)    
#print(result)    

## return multiple parameters
#def multiply(a,b):
#    return a*b,a   

#print(multiply(5,11))    

#### LECTURE-2
## function examples 
## conversion of temperature
#def convert_temp(temp,unit):
#    """ this function converts the temp B/W Celcius and fahrenheit """
#    if unit=='C':
#        return (temp*9/5)+32# converting yo fahrenhiet
#    elif unit=='F':
#        return(temp-32)*5/9 # converting to celcius
#    else:
#        return None
#a=int(input("enter the tempereature:"))
#b=input("enter the unit (C/F):").upper()
#print(convert_temp(a,b))            

## password strength checker
def check_password_strength(password):
    """ this function checks the strength of a password"""
    if len(password)<8:
        return "WEAK PASSWORD"
    if not any(char.isdigit() for char in password):
        return "WEAK PASSWORD"
    if not any(char.isupper() for char in password):
        return "WEAK PASSWORD"
    if not any(char.islower() for char in password):
        return "WEAK PASSWORD"
    if not any(char in "!@#$%^&*()_+-=~`" for char in password):
        return "WEAK PASSWORD"
    else:
        return "STRONG PASSWORD"
#password=input("enter the password:")
#print(check_password_strength(password))   
print(check_password_strength("Adhayan@123"))             