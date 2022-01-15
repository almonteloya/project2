import networkx as nx

class Graph:
    """
    Class to contain a graph perform BFS search

    Atributtes:

    graph: a graph read by networkx

    Methods:

    bfs: a method to perform breath first search or traversal

    """
    def __init__(self, filename: str):
        """
        Initialization of graph object which serves as a container for 
        methods to load data
        
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node, just return a list with the order of traversal
        * If there is an end node and a path exists, return a list of the shortest path
        * If there is an end node and a path does not exist, return None

         """

         ##check if starting node exists 
        if start not in self.graph.nodes():
            return ("The start node is not in the graph")
        #Check if end node exists 
        if end and end not in self.graph.nodes():
            return ("The end node is not in the graph")
        # Check if start node is the end node
        if start==end:
            return ("Start node is end node: " +start )
        ## Check if node has neigbors
        if len(list(self.graph.neighbors(start)))==0:
            return print ("Node doesn't have neighbor: "+ start)
        ## If end node is not defined then do traversal
        if end==None:
            return self.BFS_Traversal(start)
        ## If end node defined then do bfs traversal and shortest path
        else:
            return self.ShortestPath_BFS(start, end)

    def ShortestPath_BFS(self, start:str, goal:str) -> list:
        """
        Find the shortest path between two nodes using Breath first search

        Parameters:
        start: string specifying the starting node
        goal: string specifying ending node

        """

        # Keeping the nodes that were already visited
        exploredNodes = []
        ## initiliazing queue with starting node
        queue = [[start]]   
        
        while queue:  #while queue not empty   

            path = queue.pop(0) ## selecting furst element of path
            currentNode = path[-1] ## selecting the last element from path
            exploredNodes.append(currentNode) ##add node to visited nodes  

            #For each neighbor of the current node
            for neighbor in self.graph.neighbors(currentNode):
                if neighbor == goal:
                    return (path + [neighbor])
                    #if we reach end node then return the path and the last node 
                else:
                    if neighbor not in exploredNodes: ##if we haven't explore it then we append it to visited and to path
                        exploredNodes.append(neighbor)
                        queue.append(path + [neighbor])

        return None ##If we iterate over the whole network and not meet our goal there's no path

    def BFS_Traversal(self, start:str):
        """
        Traverse using BFS from a specific node
        Parameters
        start: string specifying starting point
        """
        # keep a record of visited nodes and queue
        explored = []
        queue = [start] 
        # while our queue not empty 
        while queue:
            node = queue.pop(0) ## take the first node in the queueu and explore its neightbors
            if node not in explored:
                explored.append(node) # added to explore neighbors so we don't visit it again
                for neighbor in self.graph.neighbors(node):
                    queue.append(neighbor)  ## add neighbr to queue

        return explored



