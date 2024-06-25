class Solution:
    sum=0
    def convertBST(self, root):
        if root:
            root.right=self.convertBST(root.right)
            self.sum+=root.val
            root.val=self.sum
            root.left=self.convertBST(root.left)
        return root