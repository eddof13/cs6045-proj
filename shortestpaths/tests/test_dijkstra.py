import shortestpaths

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
