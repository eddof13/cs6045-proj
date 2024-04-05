import math
from collections import defaultdict

def bellmanford(graph, source):
    dist = {}
    prev = {}
    for v in graph["vertices"]:
        dist[v] = math.inf
        prev[v] = None

    dist[source] = 0
    for i in range(len(graph["vertices"]) - 1):
        for key, w in graph["edges"].items():
            u, v = key.split("->")
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
    # Negative-weight cycle check
    for key, w in graph["edges"].items():
        u, v = key.split("->")
        if dist[u] + w < dist[v]:
            raise Exception("Negative-weight cycle detected")
    return dist, prev

def floydwarshall(graph, source):
    dist = defaultdict(lambda: math.inf)
    prev = {}
    for key, value in graph["edges"].items():
        dist[key] = value
        prev[key] = key.split("->")[0]
    for v in graph["vertices"]:
        dist[f"{v}->{v}"] = 0
        prev[f"{v}->{v}"] = v
    for k in graph["vertices"]:
        for i in graph["vertices"]:
            for j in graph["vertices"]:
                if dist[f"{i}->{j}"] > dist[f"{i}->{k}"] + dist[f"{k}->{j}"]:
                    dist[f"{i}->{j}"] = dist[f"{i}->{k}"] + dist[f"{k}->{j}"]
                    prev[f"{i}->{j}"] = prev[f"{k}->{j}"]
    # filtering dist for to only return for source for our purposes
    filtered_dist = {k.split("->")[1]: dist[k] for k in dist.keys() if k.startswith(source)}
    return filtered_dist, prev

def dijkstra(graph, source):
    dist = {}
    prev = {}
    Q = []
    for v in graph["vertices"]:
        dist[v] = math.inf
        prev[v] = None
        Q.append(v)
    dist[source] = 0
    
    while len(Q) > 0:
        u = min_dist(Q, dist)
        Q.remove(u)
        for v in neighbors(Q, u, graph):
            alt = dist[u] + edge(u, v, graph)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return dist, prev

def edge(u, v, graph):
    length = graph["edges"][f"{u}->{v}"]
    if length != None:
        return length
    else:
        return math.inf

def min_dist(Q, dist):
    filtered_dist = {key: dist[key] for key in Q}
    return min(filtered_dist, key=filtered_dist.get)

def neighbors(Q, u, graph):
    neighbors = []
    for v in Q:
        if f"{u}->{v}" in graph["edges"]:
            neighbors.append(v)
    return neighbors    
