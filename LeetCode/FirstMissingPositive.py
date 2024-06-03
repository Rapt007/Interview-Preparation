def firstMissingPositive( nums):
    i = 0
    while i < len(nums):
        temp = nums[i]
        if (temp == i + 1):
            i = i + 1
        elif (temp <= 0):
            i = i + 1
        elif temp > len(nums):
            i = i + 1
        elif temp == nums[temp - 1]:
            i = i + 1
        else:
            nums[i] = nums[temp - 1]
            nums[temp - 1] = temp
    print(nums)
    for i in range(0, len(nums)):
        if nums[i] != i + 1:
            return i + 1
    else:
        return len(nums) + 1


nums = [7,8,9,11,12]
print(firstMissingPositive(nums))