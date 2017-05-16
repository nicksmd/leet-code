class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        track_index = 1
        result = [0]
        power = 0
        for i in range(1,num+1):
            if i == (1<<power):
                power+=1
                result.append(1)
                track_index = 1
            else:
                result.append(1 + result[track_index])
                track_index+=1
        return result

s = Solution().countBits(16)
print s