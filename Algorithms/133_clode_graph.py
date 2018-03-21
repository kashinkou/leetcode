# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return
        root = node
        queue = collections.deque([node])
        node_set = set([node])

        while queue:
            n = queue.popleft()
            for nb in n.neighbors:
                if nb not in node_set:
                    node_set.add(nb)
                    queue.append(nb)

        mapping = {}
        # copy nodes
        for node in node_set:
            mapping[node] = UndirectedGraphNode(node.label)

        # copy neighbors
        for node in node_set:
            for nb in node.neighbors:
                mapping[node].neighbors.append(mapping[nb])

        return mapping[root]
