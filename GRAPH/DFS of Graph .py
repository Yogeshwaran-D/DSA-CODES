class Solution:
    
    def dfs(self,node,visited,adj,res):
        res.append(node)
        for edge in adj[node]:
            if not visited[edge]:
                visited[edge]=1
                self.dfs(edge,visited,adj,res)
                
    def dfsOfGraph(self, V, adj):
        visited=[0]*V
        visited[0]=1
        res=[]
        self.dfs(0,visited,adj,res)
        return res