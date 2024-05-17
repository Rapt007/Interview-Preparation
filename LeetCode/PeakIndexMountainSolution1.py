# o(n) Time complexity
def peakIndexInMountainArray(arr):
    maximum = -99999999
    for i in range(0, len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]

    for i in range(0, len(arr)):
        if arr[i] == maximum:
            return i



arr = [0, 1, 0]
print(peakIndexInMountainArray(arr))
