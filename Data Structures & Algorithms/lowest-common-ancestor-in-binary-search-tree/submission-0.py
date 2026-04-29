# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = None
        maxi = max(q.val,p.val)
        mini = min(q.val,p.val)

        def dfs(node):
            nonlocal res

            if not node:
                return
            
            if mini <= node.val <= maxi:
                res = node
                raise Exception()
            
            if node.val > maxi:
                dfs(node.left)
            elif node.val < mini:
                dfs(node.right)
                
        try:
            dfs(root)
        except:
            return res