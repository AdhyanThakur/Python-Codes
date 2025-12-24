## tuples are ordered and immutable collections of items. they are similar to list but their immutability makes them different from the list
## creating a tuple
tuple1=(1,2,3,4,5,6,7,)
#print(tuple1)
#print(type(tuple1))
## another way to create a tuple
tup=tuple()
#print(tup)
 ## conversion of a list t a tuple
lst=[1,2,3,4,5]
#print(tuple(lst))
#conversion of tuple to list
tup1=(1,2,3,4,5)
#print(list(tup1))
## mixed tuple
tup2=(1,"ADHYAN",3.14,True)
#print(tup2)
# accessing elements of a tuple
#print(tuple1)
#print(tuple1[0])
#tuple1[0]=10 # this will give an error because tupels are immutable
#print(tuple1)
#tuple operations
concate=tup1+tup2
#print(concate)
#print(len(concate))
#print(concate*3)
# immutable nature of tuple
# tuples are immutables which means we cannot change the elements of a tuple once it is created
## tuple methods
tup3=(5,2,1,3,6,7,4,2,1,3,2,2,2)
#print(tup3.index(6))# it will return the index of the first occurance of the element
#print(tup3.count(2))# it will count the number of times an element is occured
## tuple are separated by comma 
## packing and unpacking of tuples
#packing 
tup4="ADHYAN",18,3.14,True
#print(tup4)
#unpacking 
a,b,c,d=tup4# if we have 4 elements in tup then we have to provide 4 variables 
#print(a)
#print(b)
#print(c)
#print(d)
## unpacking with * operator
tup5=(1,2,3,4,5,6,7,8,9)
first,*middle,last=tup5# unpacks but the middle elements are stored in a list
#print(first)
#print(middle)
#print(last)
## nested tuples
nest_tup=((1,2,3),(4,5,6),(7,8,9))
#print(nest_tup[1][2])
#print(nest_tup[1][0:2])
#print(nest_tup[2][:])
## iterating over a tuple
for sub_tuple in nest_tup:
    for item in sub_tuple:
        print(item,end="")
    print()    