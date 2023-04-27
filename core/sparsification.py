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
        degrees = {node: graph.get_node_size(node) for node in graph.nodes}

        
        return sparsified_graph