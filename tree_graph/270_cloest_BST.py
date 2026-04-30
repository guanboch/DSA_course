'''
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.'''


from binary_search_tree_class import BinarySearchTree
from binary_search_tree_class import treeNode


class Solution:   #BST greedy N(logN)
  def __init__(self):
    self.cur_diff = float('inf')
    self.cur_val = 0
  def closestValue(self, root: treeNode, target):
    if not root:
      return None
    if abs(root.val - target) < self.cur_diff:
      self.cur_diff = abs(root.val - target)
      self.cur_val = root.val
    elif abs(root.val - target) == self.cur_diff and self.cur_val > root.val:
      self.cur_val = root.val
      
    if target < root.val:
      self.closestValue(root.left, target)
    
    if target > root.val:
      self.closestValue(root.right, target)

    return self.cur_val


# Solution2 is BST in order traversal with early stop, worst case is O(N)


  


if __name__ == "__main__":
  root = [4,2,7,1,3]
  inval = 5
  build_binary_tree = BinarySearchTree()

  for val in root:
    build_binary_tree.insert_node(val)

  bst_tree = build_binary_tree.get_node()

  solution = Solution()
  result = solution.closestValue(bst_tree, inval)
  print(result)


      