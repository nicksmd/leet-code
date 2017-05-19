from random import randrange
class Solution(object):
    def partition(self, X, pivot_index = 0):
        i = 0
        X[0], X[pivot_index] = X[pivot_index], X[0]
        for j in range(len(X)-1):
            if X[j+1] < X[0]:
                X[i+1], X[j+1] = X[j+1], X[i+1]
                i+=1

        X[0], X[i] = X[i], X[0]
        return X,i

    def qselect(self, nums, k):
        n = len(nums)
        if n == 1:
            return nums[0]
        else:
            X, pivot_index = self.partition(nums, randrange(n))
            if pivot_index+1 == k:
                return nums[pivot_index]
            elif k < pivot_index+1:
                return self.qselect(X[:pivot_index], k)
            else:
                k = k - (pivot_index + 1)
                return self.qselect(X[(pivot_index+1):], k)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.qselect(nums, len(nums)+1-k)


print Solution().findKthLargest([3,2,1,5,6,4],2)