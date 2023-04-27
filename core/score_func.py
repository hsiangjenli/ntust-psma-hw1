from .base import BaseGraph, nodeId, graph
import math
import warnings

class CommonNeighbors:
    
    @staticmethod
    def func(self, node1: nodeId, node2: nodeId) -> int:
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
        return len(list(set(self.edges[node1]) & set(self.edges[node2])))
        

class JaccardCoefficient:

    @staticmethod
    def func(self, node1: nodeId, node2: nodeId) -> float:
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
        union_size = len(set(self.edges[node1]) | set(self.edges[node2]))
        
        if union_size == 0:
            return 0
        
        return CommonNeighbors.func(self, node1, node2) / union_size

class AdamicAdar:
    
    @staticmethod
    def func(self, node1: nodeId, node2: nodeId) -> float:
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
        aa = 0
        cn = CommonNeighbors.func(self, node1, node2)
        
        if cn == 0:
            return 0
        
        neighbors = list(set(self.edges[node1]) & set(self.edges[node2]))

        for neighbor in neighbors:            
            degree = self.get_node_size(neighbor)
            
            if degree != 0:
                aa += 1 / math.log(degree)
        
        return aa

class ShortestPath:

    @staticmethod
    def func(self, node1: nodeId, node2: nodeId) -> int:
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
        if node1 == node2:
            return 0
        
        if node1 not in self.nodes or node2 not in self.nodes:
            return -1
        
        if node2 in self.edges[node1]:
            return 1
        
        """
        DFS 還沒寫完
        """
        
class KatzScore:

    @staticmethod
    def func(self, node1: nodeId, node2: nodeId, alpha: float, beta: float=1, max_length: int=4):
        """_summary_

        Calculate the Katz score between two nodes.
        
        Katz score
        ----------
        1. Measure the relative degree of influence of an actor (or node) within a social network
        1. Measures influence by taking into account the **total number of walks between a pair of actors**

        Similar
        -------
        1. PageRank
        1. Eigenvector centrality

        Parameters
        ----------
        node1 : nodeId
            A node id of the first node.
        node2 : nodeId
            A node id of the second node.
        alpha : float
            Attenuation factor. 衰減係數，用來控制遠近的影響力，通常介於 0~1 之間
            Connections made with distant neighbors are, however, penalized by an attenuation factor *alpha*. Each path or connection between a pair of nodes is assigned a weight determined by *alpha* and the distance between nodes 
        beta : float, optional
            Weight attributed to the immediate neighborhood, by default 1
        max_length : int, optional

        References
        ----------
        1. [Katz Centrality (Centrality Measure) - GeeksforGeeks](https://www.geeksforgeeks.org/katz-centrality-centrality-measure/)
        1. [katz和eigenvector 中心性](https://zhuanlan.zhihu.com/p/456679785)
        """
        pass
    
    @staticmethod
    def __get_all_possible_path(self, start: nodeId, max_length: int) -> list:
        """_summary_

        Get all possible path from start node to other nodes.

        Parameters
        ----------
        start : nodeId
            A node id of the start node.
        max_length : int
            The max length of the path.

        Returns
        -------
        list
            A list of all possible path.
        """
        
        yield None

class EigenvectorScore:
    
    @staticmethod
    def func(self, node: nodeId) -> float:
        pass