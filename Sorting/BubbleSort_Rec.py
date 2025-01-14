def BubbleSort(arr,n):
    if n==1:
        return 
    for i in range(1,n):
        if arr[i]>arr[i-1]:
            arr[i],arr[i-1]=arr[i-1],arr[i]
    BubbleSort(arr,n-1)
    return arr
arr=[6,2,7,4,1,3,5]
print(BubbleSort(arr,len(arr)))