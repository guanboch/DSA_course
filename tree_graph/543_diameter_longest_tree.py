'''
diameter of longest tree
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
'''


from build_binary_tree import buildTreeFromList


class Solution:
    def __init__(self):
        self.maxLen = 0
    def diameterOfBinaryTree(self, root) -> int:
        def diameter_tree(root):
            if not root:
                return 0, 0
            
            _, left_len = diameter_tree(root.left)
            _, right_len = diameter_tree(root.right)
            cur_node_len = left_len+right_len
            left_len = left_len + 1
            right_len = right_len + 1
            max_left_right = max(left_len, right_len)
            self.maxLen = max(cur_node_len,self.maxLen)
            
            return self.maxLen, max_left_right 
        return diameter_tree(root)[0]


# %%
root = [1,2]
newroot = buildTreeFromList(root)

solution= Solution()
print(solution.diameterOfBinaryTree(newroot))
# %%
