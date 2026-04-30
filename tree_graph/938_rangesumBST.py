'''
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
'''


from binary_search_tree_class import BinarySearchTree
from binary_search_tree_class import treeNode


class Solution:
  def rangeSumBST(self, root: treeNode, low, high):
    self.result = 0
    def dfs(root, low, high):
      if not root:
        return 
      if low <= root.val <= high:
        self.result += root.val
        if root.left:
          dfs(root.left, low, high)
        if root.right:
          dfs(root.right, low, high)

      elif root.val> high:
        if root.left:
          dfs(root.left, low, high)
      elif root.val < low:
        if root.right:
          dfs(root.right, low, high)

    dfs(root, low, high)
    return self.result
      


if __name__ == "__main__":
  root = [10,5,15,3,7,None,18]

  build_binary_tree = BinarySearchTree()

  for val in root:
    build_binary_tree.insert_node(val)

  bst_tree = build_binary_tree.get_node()

  solution = Solution()
  result = solution.rangeSumBST(bst_tree, 7, 15)
  print(result)


      