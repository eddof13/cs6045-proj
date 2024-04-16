from shortestpaths import bellmanford
import math
import random

def test_bellmanford():
    graph = {
        "edges": {
            "A->B": 3,
            "B->C": 2,
            "A->C": 5
        },
        "vertices": ["A", "B", "C"]
    }
    source = "A"
    dist, prev = bellmanford(graph, source)
    assert dist == {'A': 0, 'B': 3, 'C': 5}

def test_bellmanford_simple_graph():
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
    dist, prev = bellmanford(graph, source)
    assert dist == {'A': 0, 'B': 2, 'C': 3, 'D': 6}

def test_bellmanford_negative_cycle():
    graph = {
        "vertices": ["A", "B", "C", "D"],
        "edges": {
            "A->B": 1,
            "B->C": -1,
            "C->D": -1,
            "D->B": -1
        }
    }
    source = "A"
    try:
        dist, prev = bellmanford(graph, source)
        assert False, "Expected a negative cycle exception, but none was raised"
    except Exception as e:
        assert str(e) == "Negative-weight cycle detected"

def test_bellmanford_dense_graph():
    graph = {
        "vertices": ["A", "B", "C", "D", "E"],
        "edges": {
            "A->B": 2, "A->C": 1, "A->D": 4, "A->E": 3,
            "B->C": 5, "B->D": 1, "B->E": 2,
            "C->D": 3, "C->E": 4,
            "D->E": 1
        }
    }
    source = "A"
    dist, prev = bellmanford(graph, source)
    assert dist == {'A': 0, 'B': 2, 'C': 1, 'D': 3, 'E': 3}

def test_bellmanford_large_graph():
    graph = {
        "vertices": [str(i) for i in range(1000)],
        "edges": {f"{i}->{j}": random.randint(1, 10) for i in range(1000) for j in range(i+1, 1000, 100)}
    }
    source = "0"
    dist, prev = bellmanford(graph, source)
    assert dist["999"] < math.inf