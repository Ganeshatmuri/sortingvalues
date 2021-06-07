def binary_search(arr,x):
    low=0
    high=len(arr)-1
    mid=0

    while low<=high:
        mid=(low+high)//2
        if arr[mid]>x:
            high=mid-1
        elif arr[mid]<x:
            low=mid+1
        else:
            return mid
    return "Not Found"

list1 = [12, 24, 32, 39, 45, 50, 54]  
n = 145  
print(binary_search(list1, n))