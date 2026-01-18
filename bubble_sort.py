def bubble_sort(arr):
    n=len(arr) # len of the list
    for i in range(n):  #mo of passes
        for j in range(0,n-1-i): # compares the elements and avoids index out of range j+1 ,-i used to skip the sorted elements 
            if(arr[j] >= arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]        
    return arr







un_sorted_arr=[5,4,3,2,1]
sorted_arr=bubble_sort(un_sorted_arr)
print(sorted_arr)

####Time Complexity (Important for Exams)
# Worst case: O(n²)
# Best case: O(n²) (without optimization)
# Space: O(1) (in-place sorting)