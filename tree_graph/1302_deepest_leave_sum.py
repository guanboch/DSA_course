'''
Given the root of a binary tree, return the sum of values of its deepest leaves.
'''
from build_binary_tree import buildTreeFromList
from collections import deque

class Solution:
    def deepestLeavesSum(self, root):
        if not root:
            return 0
        queue = deque([root])
        while queue:
            cur_lvl_nodeNum = len(queue)
            cur_sum = 0
            nextLvlNode = False
            for i in range(cur_lvl_nodeNum):
                node = queue.popleft()
                cur_sum = cur_sum + node.val
                if node.left:
                    queue.append(node.left)
                    nextLvlNode = True
                if node.right:
                    queue.append(node.right)
                    nextLvlNode = True
                
            if nextLvlNode == False:
                return cur_sum      
        return cur_sum

if __name__ == '__main__':
    arr = [1,2,3,4,5,None,6,7,None,None,None,None,8]

    
    root = buildTreeFromList(arr)
    solution = Solution()
    result = solution.deepestLeavesSum(root)
    print(result)
