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


from shortestpaths import bellmanford

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