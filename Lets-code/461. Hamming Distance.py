class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x^y
        binary_string = '{0:b}'.format(z)
        return binary_string.count('1')

