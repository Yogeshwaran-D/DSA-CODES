from queue import deque
class Solution:
    def bfsOfGraph(self, V, adj) :
        queue=deque([0])
        visited=[0]*len(adj)
        visited[0]=1
        res=[]
        while queue:
            node=queue.popleft()
            res.append(node)
            for edge in adj[node]:
                if not visited[edge]:
                    visited[edge]=1
                    queue.append(edge)
        return res  