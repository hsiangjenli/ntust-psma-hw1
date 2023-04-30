from .base import graph

class DegreeBased:

    @staticmethod
    def sparsify(graph: graph, threshold: float) -> graph:
        """_summary_

        Sparsify the graph based on the degree of the nodes.

        Parameters
        ----------
        graph : graph
            A graph.
        threshold : float
            The threshold of the sparsification.

        Returns
        -------
        graph
            The sparsified graph.
        """
        sparsified_graph = {}
        sparsified_nodes = {}
        
        for node in graph.get_nodes:
            if graph.get_neighbors_size(node) >= threshold:
                sparsified_nodes[node] = graph.get_neighbors(node)
        
        # 與 node1 的交集
        sparsified_node1 = list(set(graph.keys() & sparsified_nodes.keys()))

        # 所有 sparsified_nodes
        sparsified_nodes = set(sparsified_nodes.keys() | sparsified_nodes.values())
        
        for node in sparsified_node1:
            sparsified_graph[node] = 1

        
        return sparsified_graph