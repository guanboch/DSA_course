'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST: left subtree values < node < right subtree values, and all subtrees must also be valid BSTs.
'''


from binary_search_tree_class import BinarySearchTree
from binary_search_tree_class import treeNode


class Solution:
  def isValidBST(self, root: treeNode) -> bool:
    def dfs(node, min_val, max_val):
      if not node:
        return True
      if not (min_val < node.val < max_val):
        return False
      return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

    return dfs(root, float('-inf'), float('inf'))


if __name__ == "__main__":
  solution = Solution()

  # Valid BST: [4,2,6,1,3]
  bst = BinarySearchTree()
  for val in [4, 2, 6, 1, 3]:
    bst.insert_node(val)
  print(solution.isValidBST(bst.get_node()))  # True

  # Invalid BST: manually construct a tree where right child < root
  root = treeNode(5)
  root.left = treeNode(1)
  root.right = treeNode(4)
  root.right.left = treeNode(3)
  root.right.right = treeNode(6)
  print(solution.isValidBST(root))  # False
