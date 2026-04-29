# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        res = []
        q = deque()
        q.append(root)
        
        level = 0
        while q:
            level += 1

            for i in range(len(q)):
                curr = q.popleft()
                
                if len(res) < level:
                    res.append(curr.val)

                q.append(curr.right) if curr.right else None
                q.append(curr.left) if curr.left else None
            
        return res
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     res = []

    #     def dfs(node, level=1):
    #         if not node:
    #             return
            
    #         if len(res) < level+1:
    #             res.append(node.val)
            
    #         dfs(node.right, level=level+1)
    #         dfs(node.left, level=level+1)
        
    #     dfs(root, level=0)
    #     return res

