class Solution:
    def searchRange(self, nums, target):

        ans = [-1, -1]
        left = self.BinarySearch(nums, target, True)
        right = self.BinarySearch(nums, target, False)

        ans[0] = left
        ans[1] = right
        return ans

    def BinarySearch(self, nums, target, isleft):
        start = 0
        end = len(nums) - 1
        ans = -1
        mid = 0
        while start <= end:
            mid = start + (end - start) // 2
            if target > nums[mid]:
                start = mid + 1

            elif target < nums[mid]:
                end = mid - 1

            else:
                ans = mid
                if isleft:
                    end = mid - 1
                else:
                    start = mid + 1
        return ans


nums = [5, 7, 7, 8, 8, 10]
target = 8

print(Solution.searchRange(nums, target))

