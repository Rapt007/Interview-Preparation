## Amazon question
# class Solution:
#     def InfiniteArray(self, nums, target):
#         start = 0
#         end = 1
#         while target > nums[end]:
#             temp = end + 1
#             end = end + (end+1-start)*2
#             start = temp
#
#         return self.BinarySearch(nums, start, end, target)
#
#     def BinarySearch(self, nums, start, end, target):
#         while start <= end:
#             mid = start + (end - start) // 2
#             if target > nums[mid]:
#                 start = mid + 1
#             elif target < nums[mid]:
#                 end = mid - 1
#             else:
#                 return mid
#         return -1


nums = [2, 4, 6, 7, 8, 10, 12]
target = 12

# print(Solution.InfiniteArray( nums=nums, target=target))

def InfiniteArray( nums, target):
        start = 0
        end = 1
        while target > nums[end]:
            temp = end + 1
            end = end + (end+1-start)*2
            start = temp

        return BinarySearch(nums, start, end, target)

def BinarySearch( nums, start, end, target):
    while start <= end:
        mid = start + (end - start) // 2
        if target > nums[mid]:
            start = mid + 1
        elif target < nums[mid]:
            end = mid - 1
        else:
            return mid
    return -1

print(InfiniteArray( nums=nums, target=target))
