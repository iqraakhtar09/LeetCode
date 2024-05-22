# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if q is None and p is not None:
            return False
        def compare(pnode,qnode):
            if not pnode and not qnode:
                return True
            if not pnode or not qnode:
                return False
            if pnode.val != qnode.val:
                return False
            return compare(pnode.left, qnode.left) and compare(pnode.right, qnode.right)
        
        return compare(p, q)
   

