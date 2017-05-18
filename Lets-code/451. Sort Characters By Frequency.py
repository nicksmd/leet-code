"""
    Algorithm: Counting Sort
    Complexity: O(n)
"""

import collections
class Solution(object):
    def counting_sort(self, a):
        n = len(a)
        output = [0 for i in range(n)]
        max_a = max(a)+1
        count = [0 for i in range(max_a+1)]
        for i in a:
            count[i]+=1

        for i in range(1,max_a+1):
            count[i]+=count[i-1]

        for i in range(n):
            output[count[a[i]]-1] = i
            count[a[i]] -= 1

        return output


    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return ''
        a = []
        for i in s:
            a.append(ord(i))

        count = collections.defaultdict(int)
        for i in a:
            count[i]+=1

        list_of_c = []
        reverse_list = []
        for key, value in count.iteritems():
            list_of_c.append(value)
            reverse_list.append(key)

        list_of_c = self.counting_sort(list_of_c)
        res = []
        for i in list_of_c:
            res.extend([chr(reverse_list[i]) for k in range(count[reverse_list[i]])])

        res= reversed(res)
        return "".join(c for c in res)


print Solution().frequencySort('')
