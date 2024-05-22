class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = self.findPivot(nums)
        ans = -1
        print(idx)
        start = 0
        end = len(nums) - 1
        if target == nums[idx]:
            return idx
        else:
            ans = self.BinarySearch(nums, start, idx - 1, target)
            if ans == -1:
                ans = self.BinarySearch(nums, idx + 1, end, target)
        return ans

    def BinarySearch(self, nums, start, end, target):
        while start <= end:
            mid = start + int((end - start) / 2)
            print(mid)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1

        else:
            return -1

    def findPivot(self, nums):
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid - 1
        return start
