class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        res = self.findMountain(mountain_arr)
        ans = -1
        if target == mountain_arr.get(res):
            return res
        elif target < mountain_arr.get(res):
            ans = self.BinarySearch(mountain_arr, 0, res, target, True)
            print('Hi' + str(ans))
            if ans == -1:
                print('Hi')
                return self.BinarySearch(mountain_arr, res + 1, mountain_arr.length() - 1, target, False)
        return ans

    def BinarySearch(self, nums, start, end, target, isleft):
        start = start
        end = end
        while start <= end:
            mid = start + int((end - start) / 2)
            if target == nums.get(mid):
                return mid
            elif target > nums.get(mid):
                if isleft:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if isleft:
                    end = mid - 1
                else:
                    start = mid + 1


        else:
            return -1

    def findMountain(self, arr):
        start = 0
        end = arr.length() - 1

        while start < end:
            mid = start + (end - start) // 2

            if arr.get(mid) > arr.get(mid + 1):
                end = mid
            else:
                start = mid + 1
        print(end)
        return end
