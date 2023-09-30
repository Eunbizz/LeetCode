# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if not root:
                return (0, True)

            l_height, l_balance = height(root.left)
            r_height, r_balance = height(root.right)

            return (max(l_height, r_height)+1), l_balance and r_balance and abs(l_height-r_height)<2
        
        return height(root)[1]