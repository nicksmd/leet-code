class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary_string = "{0:b}".format(n)
        return binary_string.count('1')

s = Solution().hammingWeight(11)
print s