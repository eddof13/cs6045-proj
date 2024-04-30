import os
import psutil
import time
import shortestpaths
import multiprocessing
import random
from cProfile import Profile
from pstats import SortKey, Stats
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
    
def load_func(q, f, func, graph, source, name):
    pid = os.getpid()
    p = multiprocessing.Process(target=init_ticker, args=(q, f, pid))
    p.start()
    with Profile() as profile:
        try:
            results = str(func(graph, source))
        except Exception as err:
            results = str(err)
        Stats(profile).strip_dirs().sort_stats(SortKey.CALLS).dump_stats(name.split(".")[0] + " HEATMAP.txt")
    with open(name.split(".")[0] + " RESULTS.txt", "w") as output:
        output.write(results)
    f.put("die")

def profile(func, graph, source, name):
    q = multiprocessing.Queue()
    f = multiprocessing.Queue()
    p = multiprocessing.Process(target=load_func, args=(q, f, func, graph, source, name))
    p.start()
    p.join()
    while not q.empty():
        result = str(q.get())
    with open(name.split(".")[0] + " PROFILE.txt", "a") as output:
        output.write(result)

def test_files():
    root_folder = "graph_generation"
    extensions = [".txt", ".csv", ".test"]
    test_files = []
    for subdir, dirs, files in os.walk(root_folder):
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if ext in extensions:
                test_files.append(os.path.join(subdir, file))
    return test_files

if __name__ == "__main__":
    for test_file in test_files():
        with open(test_file, "r") as file:
            data = file.read()
            graph = eval("{ " + data + " }") # this is quite dangerous, but we are only using it for profiling
            source = random.choice(graph["vertices"]) # picking a source at random

            print(f"Starting dijkstra {test_file} with source {source}")
            profile(shortestpaths.dijkstra, graph, source, test_file.replace(".", "dijkstra."))
            print(f"Finishing dijkstra {test_file} with source {source}")

            print(f"Starting bellmanford {test_file} with source {source}")
            profile(shortestpaths.bellmanford, graph, source, test_file.replace(".", "bellmanford."))
            print(f"Finishing bellmanford {test_file} with source {source}")

            print(f"Starting floydwarshall {test_file} with source {source}")
            profile(shortestpaths.floydwarshall, graph, source, test_file.replace(".", "floydwarshall."))
            print(f"Finishing floydwarshall {test_file} with source {source}")


