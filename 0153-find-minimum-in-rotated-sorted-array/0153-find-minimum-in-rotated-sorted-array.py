class Solution:
    def findMin(self, nums: List[int]) -> int:
         res = min(nums)
         return res
#         l = 0
#         r = len(nums) - 1

#         while l < r:
#            m = (l + r) // 2
#            if nums[m] < nums[r]:
#               r = m
#            else:
#              l = m + 1

#         return nums[l]
    

   