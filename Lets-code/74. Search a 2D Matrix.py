class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = 0
        column = len(matrix[0])-1

        while row<len(matrix) and column>=0:
            if matrix[row][column] == target:
                return True
            else:
                if matrix[row][column] < target:
                    row+=1
                else:
                    column-=1

        return False

print Solution().searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
],51)