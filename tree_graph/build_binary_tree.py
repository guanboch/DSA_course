# %%
from collections import deque

class treeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def get_val(self):
    return self.val
  


def buildTreeFromList(arr):
  if not arr:
    return None
  root = treeNode(arr[0])
  queue = deque([root])

  i = 1
  while queue and i < len(arr):
    node = queue.popleft()

    if arr[i] != None:
      node.left = treeNode(arr[i])
      queue.append(node.left)
    i = i + 1 

    if arr[i] != None and i < len(arr):
      node.right = treeNode(arr[i])
      queue.append(node.right)
    i = i + 1

  return root


arr=[1,2,3,None,4,5,6,7,None]

tree = buildTreeFromList(arr)

def depth_first(node):
  if node == None:
    return
  
  depth_first(node.left)
  print(node.val)
  depth_first(node.right)
  return


depth_first(tree)

def max_depth(node) -> int:
  if node == None:
    return 0
  
  left = max_depth(node.left)
  right = max_depth(node.right)

  return max(left, right) + 1 

max_depth(tree)

def target_sum(node, cur, target) -> bool:
  if node == None:
    return 0
  
  if node.left != None:
    cur = cur + node.value
    if cur == target:
      return True
    target_sum(node.left)
  


# %%
 

    







