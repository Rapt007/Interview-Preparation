
def peakIndexInMountainArray(arr):
    start = 1
    end = len(arr) - 2
    while start <= end:
        mid = start + (end - start) // 2
        left = mid - 1
        right = mid + 1

        if arr[mid] > arr[left] and arr[mid] > arr[right]:
            return mid
        elif arr[mid] > arr[left]:
            start = mid + 1
        else:
            end = mid - 1

arr = [0, 0, 1, 0, 0]
print(peakIndexInMountainArray(arr))


