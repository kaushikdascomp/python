#Sort an array of 0's, 1's and 2's
def sortArray(arr):
    length = len(arr)
    lo=0
    hi=length-1
    mid=0
    while (mid<=hi):
        if(arr[mid] == 0):
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo = lo+1
            mid = mid+1
        elif arr[mid] == 1:
            mid = mid+1
        else:
            arr[hi],arr[mid] = arr[mid], arr[hi]
            hi = hi-1
    return arr

def printarray(arr):
    for i in arr:
        print(i),
    print

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
arr = sortArray(arr)
printarray(arr)