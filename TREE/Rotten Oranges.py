from collections import deque
class Solution:
	def orangesRotting(self, grid):
		n,m=len(grid),len(grid[0])
		visited=[[0 for _ in range(m)]for _ in range(n)]
		queue=deque()
		for i in range(n):
			for j in range(m):
				if grid[i][j] == 2:
					queue.append([[i,j],0])
					visited[i][j] = 1
		time=0
		vrow=[-1,1,0,0]
		vcol=[0,0,-1,1]
		while queue:
			node=queue.popleft()
			r=node[0][0]
			c=node[0][1]
			t=node[1]
			time=max(time,t)
			for i in range(4):
				nrow=r+vrow[i]
				ncol=c+vcol[i]
				if nrow>=0 and nrow<n and ncol>=0 and ncol<m and visited[nrow][ncol]!=1 and grid[nrow][ncol] == 1:
					queue.append([[nrow,ncol],t+1])
					visited[nrow][ncol]=1
		for i in range(n):
			for j in range(m):
				if grid[i][j] == 1 and visited[i][j] == 0 :
					return -1
		return time
	