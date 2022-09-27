# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traverse(self, node, output):
        if node != None:
            self.traverse(node.left, output)
            output.append(node.val)
            self.traverse(node.right, output)
    
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        self.traverse(root, output)
        return output
        
    