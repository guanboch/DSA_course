'''
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.
A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
'''


from build_binary_tree import buildTreeFromList

class Solution:    # bottom up approach
    def max_diff_node_ancester(self, root):
        def dfs(node):
            if not node:
                # sentinels: -inf/+inf so they never pollute max/min at the parent
                return float('-inf'), float('inf'), 0

            lmax, lmin, ldiff = dfs(node.left)
            rmax, rmin, rdiff = dfs(node.right)

            cur_max = max(node.val, lmax, rmax)
            cur_min = min(node.val, lmin, rmin)

            # cur_max/cur_min already include node.val, so both terms are >= 0
            cur_diff = max(cur_max - node.val, node.val - cur_min)

            return cur_max, cur_min, max(ldiff, rdiff, cur_diff)

        return dfs(root)[2]
    
class Solution_top_down:
    # hybrid: top-down state passing + bottom-up result aggregation
    # top-down (pre-order): cur_min/cur_max are updated before recursing,
    #   so each call receives the running min/max of all its ancestors
    # bottom-up (post-order): return value max(left, right) propagates upward
    #   after both children return, collecting the best diff across all paths
    def max_diff_node_ancester(self, root):
        def dfs(node, cur_min, cur_max):
            if not node:
                return cur_max - cur_min
            cur_min = min(cur_min, node.val)
            cur_max = max(cur_max, node.val)
            return max(dfs(node.left, cur_min, cur_max),
                       dfs(node.right, cur_min, cur_max))


        return dfs(root, root.val, root.val)


# %%
root = [8,3,10,1,6,None,14,None,None,4,7,13]
newroot = buildTreeFromList(root)

solution= Solution()
print(solution.max_diff_node_ancester(newroot))
# %%
