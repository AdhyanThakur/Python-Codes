def selection_sort(arr):

    n=len(arr)
    for i in range(n):#n se vhi output aarha hai aur n-1 se bhi
         min_index=i  

         for j in range(i+1,n):
            if(arr[j] < arr[ min_index]):
                min_index = j
         arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr


un_sorted_arr=[34,213,654,21,21,554,64,876]
sorted_arr=selection_sort(un_sorted_arr)
print(sorted_arr)     

## selction_sort mei sabse pehele stating element ko saare 
# element se compare se kiya jata hai aur ismei smallest element
# ko frezze kar diya jata hai phir hum j loop use krte hai 
# (i+1,n) ye i ki value inc krega har ek paas k baad mtlb ki 
# ek let's say i=5(0-5) to mtlb 5 pass honge phir j loop mei ek 
# paas chalega phir dubara i loop mei aayega aur iss baaar pehla 
# element freeze kr denge aur aage vale element se chlega loop