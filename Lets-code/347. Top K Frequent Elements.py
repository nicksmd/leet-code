"""
    Algorithm: Counting Sort
    Complexity: O(n)
"""
import collections
class Solution(object):
    def counting_sort(self, a):
        n = len(a)
        output = [0 for i in range(0, n)]
        max_n = max(a)+1
        count = [0 for i in range(0, max_n+1)]
        for i in a:
            count[i] += 1

        for i in range(1, max_n + 1):
            count[i] += count[i - 1]

        for i in range(n):
            output[count[a[i]] - 1] = i
            count[a[i]] -= 1

        return output

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        c = collections.defaultdict(int)
        for i in nums:
            c[i]+=1

        reverse_list = []
        list_of_c = []
        for key, value in c.iteritems():
            list_of_c.append(value)
            reverse_list.append(key)

        list_of_c = self.counting_sort(list_of_c)

        res = []
        for i in range(len(list_of_c)-1,len(list_of_c)-k-1,-1):
            res.append(reverse_list[list_of_c[i]])
        return res


s = Solution().topKFrequent([1,4,1,1,2,7,5,2,4],3)
print s
