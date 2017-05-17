import collections
import heapq

class Solution(object):

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
        heap = []

        for key, value in c.iteritems():
            heapq.heappush(heap, (-value,key))

        res = []
        while k>0:
            res.append(heapq.heappop(heap)[1])
            k-=1

        return res




#s = Solution().topKFrequent([1,4,1,1,2,7,5,2,4],3)
s = Solution().topKFrequent([1,2],2)
print s
