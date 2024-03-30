import math
import os
import psutil
import time

def bellmanford(graph, source, profile=False):
    if profile == True:
        result, prof = _bellmanford(graph, source, monitor=proc())
        write_graphs(prof)
        return result, prof
    return _bellmanford(graph, source)

def floydwarshall(graph, source, profile=False):
    if profile == True:
        result, prof = _floydwarshall(graph, source, monitor=proc())
        write_graphs(prof)
        return result, prof
    return _floydwarshall(graph, source)

def dijkstra(graph, source, profile=False):
    if profile == True:
        result, prof = _dijkstra(graph, source, monitor=proc())
        write_graphs(prof)
        return result, prof
    return _dijkstra(graph, source)

def _bellmanford(graph, source, monitor=None):
    prof = []
    if monitor:
        tic = lambda: prof.append(tick(monitor))
    else:
        tic = lambda: None

    if monitor:
        return None, prof
    else:
        return None

# floyd warshall calculates all pairs, but we only care about them from source for consistency
# so we need to use path reconstruction at the end for each vertice from the source for calculation
def _floydwarshall(graph, source, monitor=None):
    prof = []
    if monitor:
        tic = lambda: prof.append(tick(monitor))
    else:
        tic = lambda: None

    if monitor:
        return None, prof
    else:
        return None

def _dijkstra(graph, source, monitor=None):
    prof = []
    if monitor:
        tic = lambda: prof.append(tick(monitor))
    else:
        tic = lambda: None

    tic
    dist = {}
    prev = {}
    Q = []
    for v in graph["vertices"]:
        dist[v] = math.inf
        prev[v] = None
        Q.append(v)
        tic
    dist[source] = 0

    while len(Q) > 0:
        u = min_dist(Q, dist)
        Q.remove(u)
        tic
        for v in neighbors(Q, u, graph):
            alt = dist[u] + edge(u, v, graph)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
            tic
    tic
    if monitor:
        return dist, prof
    else:
        return dist

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
        if graph["edges"][f"{u}->{v}"]:
            neighbors.append(v)
    return neighbors

def tick(monitor):
    return {
        "ms": round(time.time() * 1000),
        "cpu": monitor.cpu_times(),
        "cpu%": monitor.cpu_percent(interval=1.0),
        "mem%": monitor.memory_percent(),
        "mem": monitor.memory_info()
    }

def proc():
    pid = os.getpid()
    proc = psutil.Process(pid)
    return proc

def write_graphs(profile):
    # TODO: write graphs to files
    return None
    
