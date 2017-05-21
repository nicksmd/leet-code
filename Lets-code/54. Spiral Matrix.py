class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        min_r = 0
        max_r = len(matrix)-1
        min_c = 0
        max_c = len(matrix[0])-1
        res = []
        while min_r<= max_r and min_c <= max_c:
            for col in range(min_c, max_c+1):
                res.append(matrix[min_r][col])

            for row in range(min_r+1, max_r+1):
                res.append(matrix[row][max_c])

            if max_r != min_r:
                for col in range(max_c-1, min_c-1, -1):
                    res.append(matrix[max_r][col])

            if max_c != min_c:
                for row in range(max_r-1, min_r, -1):
                    res.append(matrix[row][min_c])

            min_r+=1
            min_c+=1
            max_c-=1
            max_r-=1


        return res

print Solution().spiralOrder([
 [1],[2],[3],[4],[5]
])

