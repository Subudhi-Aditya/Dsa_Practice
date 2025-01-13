# Here the first step is to select teh first smallest element and swap it with the first index and continues the steps
def selectionSort(ar):
    for i in range(0, len(ar)-1): #the outer loop runs upto the last 2nd element 
        min_idx = i
        for j in range(i,len(ar)): # the inner loop always start from the ith position to the last element becuase the i-1 position is already sorted 
            if ar[j]<ar[min_idx]:
                min_idx = j
        ar[i],ar[min_idx] = ar[min_idx],ar[i]
    return ar
print(selectionSort([4,5,2,3,1,6,8]))