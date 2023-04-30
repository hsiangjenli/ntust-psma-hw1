from typing import NewType
import warnings

nodeId = NewType('nodeId', int)
graph = NewType('graph', dict)

def if_node_not_exist(func):
    
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        except Exception as e:
            warnings.warn(f"func({func.__name__}): The node {e} does not exist.")
            return -1
            
    return wrapper

class BaseGraph:

    def __init__(self):
        self.edges = {}

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
    
    @property
    def get_nodes(self) -> list:
        """_summary_

        Get all nodes of the graph.

        Returns
        -------
        list
            A list of node ids of the nodes.
        """
        return list(set(sum(self.edges.values(), [])) | set(self.edges.keys()))

    @property
    def get_average_degree(self):
        """_summary_

        Get the average degree of the graph.

        Returns
        -------
        float
            The average degree of the graph.
        """
        return sum([len(self.edges[node]) for node in self.edges]) / len(self.edges)
    
    @if_node_not_exist
    def get_neighbors_size(self, node: nodeId) -> int:
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