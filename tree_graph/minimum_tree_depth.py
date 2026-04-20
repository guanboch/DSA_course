from collections import deque
class binaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
# %%

def build_tree_list(arr):
    if not arr:
        return None
    root = binaryTreeNode(arr[0])
    queue = deque([root])
    i = 1
    while queue and i < len(arr):
        node = queue.popleft()
        
        if arr[i] != None:
            node.left = binaryTreeNode(arr[i])
            queue.append(node.left)
        i = i + 1

        if i < len(arr) and arr[i]!= None:  
            node.right = binaryTreeNode(arr[i])
            queue.append(node.right)
        i = i + 1

    return root 

        

# %%
def min_depth_tree(root):
    if root == None:
        return
    queue = deque([root])

    i = 1
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if not node:
                continue
            if node.left == None and node.right == None:
                return i
            queue.append(node.left)
            queue.append(node.right)

        i = i + 1
           
                
    return i



# %%
a = [1,2,3,4,5]
root = build_tree_list(a)
min_depth = min_depth_tree(root)
print(min_depth)
# %%