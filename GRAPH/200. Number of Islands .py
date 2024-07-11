from collections import deque
class Solution:
    def checkIsland(self,queue,visited,grid,n,m):
        prow=[-1,1,0,0]
        pcol=[0,0,1,-1]
        while queue:
            node=queue.popleft()
            row,col=node[0],node[1]
            for i in range(4):
                nrow=row+prow[i]
                ncol=col+pcol[i]
                if nrow>=0 and nrow<n and ncol >=0 and ncol<m and visited[nrow][ncol] == 0 and grid[nrow][ncol] == "1" :
                    visited[nrow][ncol]=1
                    queue.append([nrow,ncol])
    def numIslands(self, grid) :
        n=len(grid)
        m=len(grid[0])
        visited=[[0 for _ in range(m)] for _ in range(n)]
        island=0
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and grid[i][j] == "1":
                    island+=1
                    queue=deque([[i,j]])
                    self.checkIsland(queue,visited,grid,n,m)
        return island
    
#Time complexity: O(N*M)
#Space complexity:O(N*M)