import warnings
warnings.filterwarnings('ignore')

nums = [2, 32, 922, 82, 888]

def EvenDigits(nums):
    count = 0
    for i in range(0, len(nums)):
        if len(str(nums[i])) % 2 == 0:
            count += 1

    return count


count = EvenDigits(nums)
print('Number of Even Digit in this array are: ' + str(count))