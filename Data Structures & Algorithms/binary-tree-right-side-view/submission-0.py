# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, level=1):
            if not node:
                return
            
            if len(res) < level+1:
                res.append(node.val)
            
            dfs(node.right, level=level+1)
            dfs(node.left, level=level+1)
        
        dfs(root, level=0)
        return res