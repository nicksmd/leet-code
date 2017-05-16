class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        result = 0
        for i in range(0,len(nums)-1,2):
            result = result+ nums[i]
        return result

s = Solution().arrayPairSum([4,3,2,1])
print s