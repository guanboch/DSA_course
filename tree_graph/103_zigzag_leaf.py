'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
'''
from build_binary_tree import buildTreeFromList
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        start_left = True
        queue = deque([root])
        final_result = []
        
        
        while queue:
            lvl_result = []
            lvl_node_num = len(queue)
            for i in range(lvl_node_num):
                if start_left:
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    node = queue.pop()
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
                lvl_result.append(node.val)
                

            start_left = not start_left    
            final_result.append(lvl_result)

        return final_result



  
if __name__ == '__main__':
    arr = root = [3,9,20,None,None,15,7]

    
    root = buildTreeFromList(arr)
    solution = Solution()
    result = solution.zigzagLevelOrder(root)
    print(result)
