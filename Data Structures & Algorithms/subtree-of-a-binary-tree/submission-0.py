# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        if not subRoot: return True
        def sameTree(root, subRoot):
            if root is None or subRoot is None:
                return root is subRoot
            else:
                return root.val == subRoot.val and sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)
        return sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)