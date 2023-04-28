from .base import BaseGraph, if_node_not_exist
from .score_func import *

class Graph(BaseGraph):
    
    def add_edge(self, node1: nodeId, node2: nodeId):
        """_summary_

        Create an edge between two nodes.

        Parameters
        ----------
        node1 : nodeId
            A node id of the first node.
        node2 : nodeId
            A node id of the second node.
        """
        
        if node1 not in self.edges:
            self.edges[node1] = []
        
        self.edges[node1].append(node2)
    
    def get_edges(self, node: nodeId):
        """_summary_

        Get all edges of a node.

        Parameters
        ----------
        node : nodeId
            A node id of the node.

        Returns
        -------
        list
            A list of node ids of the edges.
        """
        
        return self.edges[node]
    
    @if_node_not_exist
    def get_neighbor_size(self, node: nodeId) -> int:
        """_summary_

        Get the size of a node.

        Parameters
        ----------
        node : nodeId
            A node id of the node.

        Returns
        -------
        int
            The size of the node.
        """
        
        return len(self.edges[node])

    @if_node_not_exist
    def common_neighbors(self, node1: nodeId, node2: nodeId) -> int:
        """_summary_

        Calculate the common neighbors score between two nodes.

        Parameters
        ----------
        node1 : nodeId
            A node id of the first node.
        node2 : nodeId
            A node id of the second node.

        Returns
        -------
        int
            The common neighbors score between two nodes.
        """
        
        return CommonNeighbors.func(self, node1, node2)

    @if_node_not_exist
    def jaccard_coefficient(self, node1: nodeId, node2: nodeId) -> float:
        """_summary_

        Calculate the Jaccard coefficient score between two nodes.

        Parameters
        ----------
        node1 : nodeId
            A node id of the first node.
        node2 : nodeId
            A node id of the second node.

        Returns
        -------
        float
            The Jaccard coefficient score between two nodes.
        """
        
        return JaccardCoefficient.func(self, node1, node2)

    @if_node_not_exist
    def adamic_adar(self, node1: nodeId, node2: nodeId) -> float:
        """_summary_

        Calculate the Adamic-Adar score between two nodes.

        Parameters
        ----------
        node1 : nodeId
            A node id of the first node.
        node2 : nodeId
            A node id of the second node.

        Returns
        -------
        float
            The Adamic-Adar score between two nodes.
        """
        
        return AdamicAdar.func(self, node1, node2)

    def shortest_path(self, node1: nodeId, node2: nodeId) -> int:
        """_summary_

        Calculate the shortest path score between two nodes.

        Parameters
        ----------
        node1 : nodeId
            A node id of the first node.
        node2 : nodeId
            A node id of the second node.

        Returns
        -------
        int
            The shortest path score between two nodes.
        """
        
        return ShortestPath.func(self, node1, node2)

    @if_node_not_exist
    def katz_score(self, node1: nodeId, node2: nodeId, alpha: float=1.0, beta: float=1.0, max_length: int=100) -> float:
        """_summary_

        Calculate the Katz score between two nodes.

        Parameters
        ----------
        node1 : nodeId
            A node id of the first node.
        node2 : nodeId
            A node id of the second node.

        Returns
        -------
        float
            The Katz score between two nodes.
        """
        
        return KatzScore.func(self, node1, node2, alpha, beta, max_length)
    
    @if_node_not_exist
    def preferential_attachment(self, node1: nodeId, node2: nodeId) -> int:
        """_summary_

        Calculate the preferential attachment score between two nodes.

        Parameters
        ----------
        node1 : nodeId
            A node id of the first node.
        node2 : nodeId
            A node id of the second node.

        Returns
        -------
        int
            The preferential attachment score between two nodes.
        """
        
        return self.get_neighbor_size(node1) * self.get_neighbor_size(node2)





