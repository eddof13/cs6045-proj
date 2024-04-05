import os
import psutil
import time
import shortestpaths
import multiprocessing
from threading import Event
from ischedule import schedule, run_loop

def tick(q, f, pid, stop_event):
    if not f.empty():
        stop_event.set()
    monitor = psutil.Process()
    q.put({
        "ms": round(time.time() * 1000),
        "cpu": monitor.cpu_times(),
        "cpu%": monitor.cpu_percent(interval=1.0),
        "mem%": monitor.memory_percent(),
        "mem": monitor.memory_info()
    })

def init_ticker(q, f, pid):
    stop_event = Event()
    def ticker():
        tick(q, f, pid, stop_event)
    schedule(ticker, interval=0.1)
    run_loop(stop_event=stop_event)
    
def load_func(q, f, func, graph, source):
    pid = os.getpid()
    p = multiprocessing.Process(target=init_ticker, args=(q, f, pid))
    p.start()
    print(func(graph, source))
    f.put("die")

def process(func, graph, source):
    q = multiprocessing.Queue()
    f = multiprocessing.Queue()
    p = multiprocessing.Process(target=load_func, args=(q, f, func, graph, source))
    p.start()
    p.join()
    while not q.empty():
        print(q.get())

if __name__ == "__main__":
    graph = {
        "edges": {
            "A->B": 3,
            "B->C": 2,
            "A->C": 5
        },
        "vertices": ["A", "B", "C"]
    }
    source = "A"

    print("Starting dijkstra 1")
    process(shortestpaths.dijkstra, graph, source)
    print("Finishing dijkstra 1")

    print("Starting bellmanford 1")
    process(shortestpaths.bellmanford, graph, source)
    print("Finishing bellmanford 1")

    print("Starting floydwarshall 1")
    process(shortestpaths.floydwarshall, graph, source)
    print("Finishing floydwarshall 1")


