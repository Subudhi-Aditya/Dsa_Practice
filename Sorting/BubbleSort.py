def BubbleSort(ar):
    for i in range(0,len(ar)-1):
        for j in range(0, len(ar)-1-i):
            if(ar[j]<ar[j+1]):
                ar[j+1],ar[j]=ar[j],ar[j+1]
    return ar

print(BubbleSort([2,4,1,3,6,3,7]))