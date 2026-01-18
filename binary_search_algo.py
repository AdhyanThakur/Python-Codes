def binary_search(lst,target):
    n=len(lst)
    for i in range(0,n):
        if lst[i]==target:
            return i
    return -1



lst=[5,3,4,2,1]
target=2
r=binary_search(lst,target)
print(r)