# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)
        
        res = []
        while q:
            curr_l = []
            for i in range(len(q)):
                curr = q.popleft()
                curr_l.append(curr.val)
                q.append(curr.left) if curr.left else None
                q.append(curr.right) if curr.right else None
            res.append(curr_l)
        return res
