'''
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

'''

from build_binary_tree import buildTreeFromList

from collections import deque


class Solution:
    def largestValues(self, root):
        if not root:
            return []
        
        queue = deque([root])
        row_largest = []
        while queue:
            cur_lvl_num = len(queue)
            for i in range(cur_lvl_num):
                cur_node = queue.popleft()
                if i == 0:
                    cur_max = cur_node.val
                else:
                    cur_max = max(cur_node.val, cur_max)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            
            row_largest.append(cur_max)

        return row_largest