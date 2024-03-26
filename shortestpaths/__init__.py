import os
import psutil
import time

def bellmanford(graph, source, profile=False):
    if profile == True:
        result, prof = _bellmanford(graph, source, monitor=proc())
        write_graphs(prof)
        return result, prof
    return _bellmanford(graph, source)

def astar(graph, source, profile=False):
    if profile == True:
        result, prof = _astar(graph, source, monitor=proc())
        write_graphs(prof)
        return result, prof
    return _astar(graph, source)

def dijkstra(graph, source, profile=False):
    if profile == True:
        result, prof = _dijkstra(graph, source, monitor=proc())
        write_graphs(prof)
        return result, prof
    return _dijkstra(graph, source)

def _bellmanford(graph, source, monitor=None):
    prof = []
    if monitor:
        prof.append(tick(monitor))
        return None, prof
    return None

def _astar(graph, source, monitor=None):
    prof = []
    if monitor:
        prof.append(tick(monitor))
        return None, prof
    return None

def _dijkstra(graph, source, monitor=None):
    prof = []
    if monitor:
        prof.append(tick(monitor))
        return None, prof
    return None

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
    
