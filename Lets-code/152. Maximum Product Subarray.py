class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        fx = [0]*n
        fx[0] = nums[0]
        res = fx[0]
        for i in range(1,n):
            fx[i] = max(nums[i],fx[i-1]*nums[i])
            res= max(res, fx[i])

        return res


print Solution().maxProduct([2,-3,-2,4])