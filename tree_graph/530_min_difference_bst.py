'''
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree
'''


from binary_search_tree_class import BinarySearchTree
from binary_search_tree_class import treeNode


class Solution:
  def getMinimumDifference(self, root: treeNode):
    if not root:
      return 0
    else:
      self.cur_min_diff = float('inf')
      self.pre_val = None

    def dfs(root):
      if not root:
        return

      dfs(root.left)
      if self.pre_val is not None:
        self.cur_min_diff = min(self.cur_min_diff, abs(self.pre_val - root.val))
      self.pre_val = root.val
      dfs(root.right)

    dfs(root)
    return self.cur_min_diff
  


if __name__ == "__main__":
  root = [4,2,6,1,3]

  build_binary_tree = BinarySearchTree()

  for val in root:
    build_binary_tree.insert_node(val)

  bst_tree = build_binary_tree.get_node()

  solution = Solution()
  result = solution.getMinimumDifference(bst_tree)
  print(result)


      