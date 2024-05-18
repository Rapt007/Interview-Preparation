def findPeakElement( nums):
    start = 0
    end = len(nums) - 1
    if len(nums) <= 1:
        return 0

    while start < end:
        mid = start + (end - start) // 2

        if nums[mid] > nums[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return end

arr = [1,2,1,3,5,6,4]
print(findPeakElement(arr))
