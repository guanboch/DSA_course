'''
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree
'''


from binary_search_tree_class import BinarySearchTree
from binary_search_tree_class import treeNode


class Solution:
  def insertIntoBST(self, root: treeNode, val):
    if not root:
      return treeNode(val)

    if val < root.val:
      if root.left:
        self.insertIntoBST(root.left, val)
      else:
        root.left = treeNode(val)
    else:
      if root.right:
        self.insertIntoBST(root.right, val)
      else:
        root.right = treeNode(val)

    return root

  


if __name__ == "__main__":
  root = [4,2,7,1,3]
  inval = 5
  build_binary_tree = BinarySearchTree()

  for val in root:
    build_binary_tree.insert_node(val)

  bst_tree = build_binary_tree.get_node()

  solution = Solution()
  result = solution.insertIntoBST(bst_tree, inval)
  print(result)


      