# # calculate the sum of first n natural  number using a while loop and for loop
# # by while loop 
# n=10
# sum=0
# count=1
# while count<=n:
#     sum=sum+count
#     count=count+1
# print(sum) 
# by for loop
# sum=0
# count=1
# n=10
# for i in range(11):
#     sum=sum+i
# print(sum) 
# dipaly the prime number from 1-100 
for num in range(1,101):
    if num>1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)          