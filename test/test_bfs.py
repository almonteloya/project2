# write tests for bfs
import pytest
import sys
import networkx as nx
sys.path.append('/Users/anaalmonte/Documents/Algorithms/project2/')
from search import Graph




@pytest.fixture
def test_bfs_traversal():
    """
    Testing BFS traversal 
    Test.adjlist is a small network created manually, see graph.png for representation
    G_citation is created from the citation graph
    """
    G=Graph("./data/test.adjlist")
    
    assert G.bfs('A') == ['A', 'B', 'C', 'G', 'D', 'E', 'F']
    
    ## Z is isolated
    assert G.bfs('Z')== None

    G_citation=Graph("./data/tiny_network.adjlist")
    # my bfs search such be the same lenght as netwrok ex traversal
    assert len((G_citation.bfs('Luke Gilbert'))) == len(list(nx.bfs_tree(G_citation.graph,"Luke Gilbert")))



def test_bfs():
    """
    Testing BFS traversal 
    Test.adjlist is a small network created manually, see graph.png for representation
    """
    G=Graph("./data/test.adjlist")
    assert G.bfs('A','E') == ['A', 'G', 'E']
    
    # There's no path between A and Z
    assert G.bfs('A','Z') == None
    

