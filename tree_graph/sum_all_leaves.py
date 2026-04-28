
'''Given the root of a binary tree, return the sum of values all leaves.
'''
from build_binary_tree import buildTreeFromList

class Solution_dfs:
    def allLeaveSum(self, root):
        if not root:
            return 0
        if (not root.left) and (not root.right):
            return root.val
        return self.allLeaveSum(root.left) + self.allLeaveSum(root.right)


if __name__ == '__main__':
    root = [1,2,3,4,5,None,6,7,None,None,None,None,8]
    root = buildTreeFromList(root)
    solution1 = Solution_dfs()
    print(solution1.allLeaveSum(root))