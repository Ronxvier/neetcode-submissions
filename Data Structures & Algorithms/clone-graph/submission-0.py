"""
# definition for a node.
class node:
    def __init__(self, val = 0, neighbors = none):
        self.val = val
        self.neighbors = neighbors if neighbors is not none else []
"""

class Solution:
    def cloneGraph(self, node: optional['node']) -> optional['node']:
        copymap = {}
        def recurse(parent):
            if parent not in copymap:
                if parent is None:
                    return
                copy = Node(parent.val)
                copymap[parent] = copy
                for neighbor in parent.neighbors:
                    copy.neighbors.append(recurse(neighbor))
            else:
                copy = copymap[parent]
            return copy
        return recurse(node)