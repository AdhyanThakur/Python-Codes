# lst=["ADHYAN","THAKUR",1,2,3,4]
# print(lst)
# fruits=["APPLE","BANANA","CHERRY","KIWI","GUAVA"]
# fruits[1]="watermelon"
# print(fruits)
# ## list methods
# fruits.append("ORANGE")
# print(fruits)
# fruits.insert(1,"PApaya")
# print(fruits)
# fruits.remove("PApaya")
# print(fruits)
# popped_fruits=fruits.pop()
# print(popped_fruits)
# index=fruits.index("APPLE")
# print(index)
# fruits.insert(2,"BANANA")
# print(fruits.count("BANANA"))
# fruits.sort()
# print(fruits)
## ITERATING WITH INDEX
# numbers=[1,2,3,4,5,6,7,8,9,10]
# for number in numbers:
#     print(number)
# for index,number in enumerate(numbers):
#     print(index,number)
## LIST COMPREHENSION
lst=[]
# for x in range(10):
#     lst.append(x**2)
# print(lst)    
[x**2 for x in range(10)]