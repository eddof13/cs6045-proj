import math
import os
import psutil
import time
from collections import defaultdict

def bellmanford(graph, source, profile=False):
    if profile == True:
        dist, prev, prof = _bellmanford(graph, source, monitor=proc())
        write_graphs(prof)
        return dist, prev, prof
    return _bellmanford(graph, source)

def floydwarshall(graph, source, profile=False):
    if profile == True:
        dist, prev, prof = _floydwarshall(graph, source, monitor=proc())
        write_graphs(prof)
        return dist, prev, prof
    return _floydwarshall(graph, source)

def dijkstra(graph, source, profile=False):
    if profile == True:
        dist, prev, prof = _dijkstra(graph, source, monitor=proc())
        write_graphs(prof)
        return dist, prev, prof
    return _dijkstra(graph, source)

def _bellmanford(graph, source, monitor=None):
    prof, tic = init_profile(monitor)

    # TODO

    if monitor:
        return None, None, prof
    else:
        return None, None

def _floydwarshall(graph, source, monitor=None):
    prof, tic = init_profile(monitor)

    tic()
    dist = defaultdict(lambda: math.inf)
    prev = {}
    for key, value in graph["edges"].items():
        dist[key] = value
        prev[key] = key.split("->")[0]
    tic()    
    for v in graph["vertices"]:
        dist[f"{v}->{v}"] = 0
        prev[f"{v}->{v}"] = v
    tic()
    for k in graph["vertices"]:
        tic()
        for i in graph["vertices"]:
            for j in graph["vertices"]:
                if dist[f"{i}->{j}"] > dist[f"{i}->{k}"] + dist[f"{k}->{j}"]:
                    dist[f"{i}->{j}"] = dist[f"{i}->{k}"] + dist[f"{k}->{j}"]
                    prev[f"{i}->{j}"] = prev[f"{k}->{j}"]
    tic()
    if monitor:
        return dist, prev, prof
    else:
        return dist, prev

def _dijkstra(graph, source, monitor=None):
    prof, tic = init_profile(monitor)

    tic()
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
        tic()
        for v in neighbors(Q, u, graph):
            alt = dist[u] + edge(u, v, graph)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
            tic()
    tic()
    if monitor:
        return dist, prev, prof
    else:
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
        if graph["edges"][f"{u}->{v}"]:
            neighbors.append(v)
    return neighbors

def init_profile(monitor):
    prof = []
    if monitor:
        tic = lambda: prof.append(tick(monitor))
    else:
        tic = lambda: None
    return prof, tic

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
    
