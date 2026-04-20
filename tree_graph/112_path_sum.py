# %%

#leetcode 112, given root, check if there is a root to leaf path such that adding up all values along the path equals targetSum
from build_binary_tree import buildTreeFromList
import importlib


a = buildTreeFromList([2,4,5,1,6,None,3, 56])
# %%


root = buildTreeFromList(a)

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if root == None:
            return False
        sum = 0 
        def path_sum1(root, sum, targetSum):
            sum = sum + root.val
            if root.left == None and root.right == None:
                if sum == targetSum:
                    return True
            left_found = False
            right_found = False
            if root.left != None:
                left_found = path_sum1(root.left, sum, targetSum)
            if root.right != None:
                right_found = path_sum1(root.right, sum, targetSum)
            return (left_found or right_found)
        return path_sum1(root, sum, targetSum)


class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return targetSum - root.val == 0
        
        targetSum -= root.val
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
