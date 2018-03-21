class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix
        n = len(matrix)
        m = len(matrix[0])
        res = [[n*m for _ in xrange(m)] for _ in xrange(n)]
        q = collections.deque([])
        for i in xrange(n):
            for j in xrange(m):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                    q.append((i, j))

        dx = [1,0,-1,0]
        dy = [0,1,0,-1]

        while q:
            x, y = q.popleft()
            for k in range(4):
                newx = x + dx[k]
                newy = y + dy[k]
                if 0 <= newx < n and 0 <= newy < m:
                    if res[newx][newy] > res[x][y] + 1:
                        res[newx][newy] = res[x][y] + 1
                        q.append((newx, newy))

        return res
