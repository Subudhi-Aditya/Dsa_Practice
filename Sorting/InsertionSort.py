def InsertionSort(arr):
    for i in range(1,len(arr)):
        j=i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j=j-1
    return arr
    
print(InsertionSort([5,4,7,8,2,1,3,4]))
