# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class CustomError(Exception):
    def __init__(self, msg="Error raised manually!"):
        self.message = msg
    
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return
            
            if node.val == subRoot.val and self.isSameTree(node, subRoot):
                raise CustomError()
            
            dfs(node.left)
            dfs(node.right)

        try:
            dfs(root)
            return False
        except CustomError:
            return True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if not node1 and not node2:
                return

            if not node1 and node2:
                raise Exception()
                
            if node1 and not node2:
                raise Exception()

            if node1.val != node2.val:
                raise Exception()
            
            dfs(node1.left, node2.left)
            dfs(node1.right, node2.right)
        
        try:
            dfs(p, q)
        except:
            return False
        return True
        