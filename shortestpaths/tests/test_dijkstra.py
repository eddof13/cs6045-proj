import shortestpaths
import math

def test_dijkstra():
    graph = {
        "edges": {
            "A->B": 3,
            "B->C": 2,
            "A->C": 5
        },
        "vertices": ["A", "B", "C"]
    }
    source = "A"
    dist, prev = shortestpaths.dijkstra(graph, source)
    assert dist == {'A': 0, 'B': 3, 'C': 5}

def test_dijkstra_profiled():
    graph = {
        "edges": {
            "A->B": 3,
            "B->C": 2,
            "A->C": 5
        },
        "vertices": ["A", "B", "C"]
    }
    source = "A"
    dist, prev, prof = shortestpaths.dijkstra(graph, source, True)
    assert dist == {'A': 0, 'B': 3, 'C': 5}


from shortestpaths import dijkstra

def test_dijkstra_simple_graph():
    graph = {
        "vertices": ["A", "B", "C", "D"],
        "edges": {
            "A->B": 2,
            "A->C": 4,
            "B->C": 1,
            "B->D": 5,
            "C->D": 3
        }
    }
    source = "A"
    dist, prev = dijkstra(graph, source)
    assert dist == {'A': 0, 'B': 2, 'C': 3, 'D': 6}

def test_dijkstra_disconnected_graph():
    graph = {
        "vertices": ["A", "B", "C", "D", "E"],
        "edges": {
            "A->B": 2,
            "A->C": 4,
            "B->C": 1,
            "B->D": 5,
            "C->D": 3
        }
    }
    source = "A"
    dist, prev = dijkstra(graph, source)
    assert dist == {'A': 0, 'B': 2, 'C': 3, 'D': 6, 'E': math.inf}