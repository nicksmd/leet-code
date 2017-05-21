class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        dx = [-1, 0, 1, 0]
        dy = [ 0, 1, 0, -1]

        fx = {}
        queue = []
        res = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    queue.append((row, col))
                    fx[(row, col)] = 0
                else:
                    fx[(row, col)] = -1

        while len(queue) > 0:
            now = queue.pop(0)
            for i in range(4):
                then = (now[0]+dx[i], now[1]+dy[i])
                if then in fx and fx[then] == -1:
                    fx[then] = fx[now] + 1
                    queue.append(then)

        for item in fx:
            res[item[0]][item[1]] = fx[item]
        return res

print Solution().updateMatrix([[0]])