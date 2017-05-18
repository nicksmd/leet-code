class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1]*n
        L = 1
        R = 1
        for i in range(n):
            res[i]=res[i]*L
            L=L*nums[i]
            res[n-1-i] = res[n-1-i] * R
            R=R*nums[n-1-i]

        return res

print Solution().productExceptSelf([1,2,3,4])

