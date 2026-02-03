# %%
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"

def build_tree_from_list(arr):
    """
    Builds a binary tree from a list in level-order.
    None values mean no child at that position.
    """
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        node = queue.popleft()

        # left child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        # right child
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root


tree1 = build_tree_from_list([1, 2, 3, None, 4, 5, 6])
def preorder(root):
    return [] if not root else [root.val] + preorder(root.left) + preorder(root.right)

print("Pre-order:", preorder(tree1))
# %%