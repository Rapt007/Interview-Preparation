def findduplicate(nums):
    i = 0
    while i < len(nums):
        temp1 = nums[i]
        if nums[i] == i + 1 or nums[i] == nums[temp1 - 1]:
            i = i + 1
        else:
            temp = nums[i]
            nums[i] = nums[temp - 1]
            nums[temp - 1] = temp

    print(nums)
    for i in range(0, len(nums)):
        if nums[i] != i + 1:
            return nums[i]

nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findduplicate(nums))

