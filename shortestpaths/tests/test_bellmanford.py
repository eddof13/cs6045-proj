from shortestpaths import bellmanford

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

def test_bellmanford_profiled():
    graph = {
        "edges": {
            "A->B": 3,
            "B->C": 2,
            "A->C": 5
        },
        "vertices": ["A", "B", "C"]
    }
    source = "A"
    dist, prev, prof = bellmanford(graph, source, True)
    assert dist == {'A': 0, 'B': 3, 'C': 5}
