import warnings
warnings.filterwarnings('ignore')

nums = [2, 3, 9, 8]
target = 3
def searchInsert(nums, target):
    if len(nums) == 0:
        return -1

    for i in range(0, len(nums)):
        if nums[i] == target:
            return i

    else:
        return -1


index = searchInsert(nums, target)
print('Target is at index:' + str(index))