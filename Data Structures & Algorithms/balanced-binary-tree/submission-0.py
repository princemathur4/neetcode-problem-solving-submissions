# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0

            left_l = dfs(node.left)
            right_l = dfs(node.right)
            if abs(left_l - right_l) > 1:
                raise Exception()
            return 1 + max(left_l, right_l)

        try:
            dfs(root)
            return True
        except:
            return False
        