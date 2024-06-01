def finderrornums(nums):
    i = 0
    while i < len(nums):
        temp = nums[i]
        if nums[i] == i + 1 or nums[i] == nums[temp - 1]:
            i = i + 1
        else:
            nums[i] = nums[temp - 1]
            nums[temp - 1] = temp

    for i in range(0, len(nums)):
        if nums[i] != i + 1:
            return [nums[i], i + 1]

