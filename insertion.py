def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        j=i-1
        key=arr[i]
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    print(arr)
insertion_sort([6,5,3,1,8,7,2,4])