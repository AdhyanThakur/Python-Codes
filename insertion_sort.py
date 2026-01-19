def insertion_sort(lst):
    # Your code goes here
    for i in range(1, len(lst)):
        key = lst[i]
        
        # Move elements of lst[0..i-1] that are greater than key
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        
        # Insert key in its correct position
        lst[j + 1] = key
    
    return lst
 
#### or


def insertion_sort(arr):
    n = len(arr)

    for current in range(1,n):
        currentCard = arr[current]
        correctPosition = current-1 # It will go from i-1 to 0
        while correctPosition >=0:
            if(arr[correctPosition] < currentCard):
                break
            else:
                arr[correctPosition +1 ] = arr[correctPosition]
                correctPosition-=1
            arr[correctPosition + 1] = currentCard

    return arr


unsorted_list = [12,25,11,34,90,22]
sorted_list = insertion_sort(unsorted_list)
print("Sorted Elements :", sorted_list)