from build_binary_tree import buildTreeFromList


class Solution:
    def __init__(self):
        self.leftsum = 0 
    def sumOfLeftLeaves(self, root):
        def dfs(root, left_right):
            if not root:
                return 0
            if (not root.left) and (not root.right) and left_right:
                self.leftsum = self.leftsum + root.val

            dfs(root.left, 1)
            dfs(root.right,0)
            return
        dfs(root, 0)
        return self.leftsum

class Solution2:
    def sumOfLeftLeaves(self, root):
        def dfs(node, is_left):
            if not node:
                return 0
            if (not node.left) and (not node.right):
                return node.val if is_left else 0
            return dfs(node.left, True) + dfs(node.right, False) # this is post order traversal, thus reaches leaf first, then return from the leaf

        return dfs(root, False)

