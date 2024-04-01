from shortestpaths import floydwarshall
import math

def test_floydwarshall():
    graph = {
        "edges": {
            "A->B": 3,
            "B->C": 2,
            "A->C": 5
        },
        "vertices": ["A", "B", "C"]
    }
    source = "A"
    dist, prev = floydwarshall(graph, source)
    assert dist == {'A': 0, 'B': 3, 'C': 5}

def test_floydwarshall_profiled():
    graph = {
        "edges": {
            "A->B": 3,
            "B->C": 2,
            "A->C": 5
        },
        "vertices": ["A", "B", "C"]
    }
    source = "A"
    dist, prev, prof = floydwarshall(graph, source, True)
    assert dist == {'A': 0, 'B': 3, 'C': 5}
