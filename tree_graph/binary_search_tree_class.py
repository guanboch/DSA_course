class treeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def get_val(self):
    return self.val

class BinarySearhTree:
    def __init__(self):
        self.root = None

    def insert_node(self, key):
        if self.root == None:
            self.root = treeNode(key)
        else: 
            self._insert_recursive(self.root, key)


    def _insert_recursive(self,cur_node, key):
            if key <= cur_node.val:
                if cur_node.left != None:
                    self._insert_recursive(cur_node.left, key)
                else:
                    cur_node.left = treeNode(key)
            else:
                if cur_node.right != None:
                    self._insert_recursive(cur_node.right, key)
                else:
                    cur_node.right = treeNode(key)


    def inorder_traversal(self, node, result):
       
        if result == None:
            result = []

        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.val)
            self.inorder_traversal(node.right,result)

        return

# %%

        




# %%
