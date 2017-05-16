class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        m = len(nums[0])
        if n*m != r*c:
            return nums
        else:
            one_d_array = [item  for row in nums for item in row]
            new_array = []
            print one_d_array
            count = 0
            for i in range(0,r):
                new_array.append([])
                for j in range(0,c):
                    new_array[len(new_array)-1].append(one_d_array[count])
                    count+=1
            return new_array


s = Solution().matrixReshape([[1,2],[3,4]],1,4)
print s
s = Solution().matrixReshape([[4,3,0],[0,2,1]],3,4)
print s
s = Solution().matrixReshape([[4,3,1,2]],2,2)
print s
s = Solution().matrixReshape([[4,3,1,2]],4,1)
print s
s = Solution().matrixReshape([[4,3],[1,2]],1,4)
print s
