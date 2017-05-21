class Solution(object):
    def spiralOrder(self, n):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        min_r = 0
        max_r = n-1
        min_c = 0
        max_c = n-1
        res = [[0 for i in range(n)] for j in range(n)]
        k = 0
        while min_r<= max_r and min_c <= max_c:
            for col in range(min_c, max_c+1):
                k+=1
                res[min_r][col] = k

            for row in range(min_r+1, max_r+1):
                k+=1
                res[row][max_c] = k

            if max_r != min_r:
                for col in range(max_c-1, min_c-1, -1):
                    k+=1
                    res[max_r][col] = k

            if max_c != min_c:
                for row in range(max_r-1, min_r, -1):
                    k+=1
                    res[row][min_c]=k

            min_r+=1
            min_c+=1
            max_c-=1
            max_r-=1


        return res

print Solution().spiralOrder(1)

