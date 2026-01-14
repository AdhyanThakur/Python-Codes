### A filter function constructs an iterator from an elements of an 
# iterable for which a function returns True. it is used to filter 
# out the items from a list or any iterable based on condition.
# What filter(function, iterable) needs
# filter() requires:
# A function that returns True or False
# An iterable (like a list)
def even(x):
    return x%2==0
lst=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(even,lst)))
# x receives each element of the list automatically, one by one,
#  through the filter() function.
## by  filter and lambda function
print(list(filter(lambda x: x % 2 == 0, lst)))
## filter with lambda function
number=[1,2,3,4,5,6,7,8,9]
greater_than_five=list(filter(lambda x:x>5,number))
print(greater_than_five)
## filetr with lambda function and multiple conditions
## taking the same list as above number[]
even_and_greater_than_five=list(filter(lambda x:x%2==0 and x>5, number))
print(even_and_greater_than_five)
## apply filter on the dictionary (check if the age is greater 
# than 25)
people=[{"name":"adhyan","age":34},
        {"name":"ravi_teja","age":25},
        {"name":"ravia","age":15}] 
def age_greater_than_25(person):
    return person['age']>25
print(list(filter(age_greater_than_25,people)))  


##### Conclusion
#The filter() function is a powerful tool for creating iterators
# that filter items out of an iterable based on a function. 
# It is commonly used for data cleaning, filtering objects, 
# and removing unwanted elements from lists. 
# By mastering filter(), you can write more concise and 
# efficient code for processing and manipulating collections 
# in Python.