from build_binary_tree import buildTreeFromList

class Solution:
    def max_diff_node_ancester(self, root):
        def dfs(node):
            if not node:
                # sentinels: -inf/+inf so they never pollute max/min at the parent
                return float('-inf'), float('inf'), 0

            lmax, lmin, ldiff = dfs(node.left)
            rmax, rmin, rdiff = dfs(node.right)

            cur_max = max(node.val, lmax, rmax)
            cur_min = min(node.val, lmin, rmin)

            # max diff with current node as the ancestor
            cur_diff = max(
                node.val - min(lmin, rmin),   # node is larger than some descendant
                max(lmax, rmax) - node.val,   # node is smaller than some descendant
                0                             # clamps -inf results when a child is None
            )

            return cur_max, cur_min, max(ldiff, rdiff, cur_diff)

        return dfs(root)[2]
    
    

# %%
root = [8,3,10,1,6,None,14,None,None,4,7,13]
newroot = buildTreeFromList(root)

solution= Solution()
print(solution.max_diff_node_ancester(newroot))
# %%
