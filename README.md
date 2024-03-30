# cs6045-proj

Shortest path implementations from source to other nodes (not providing previous hop nodes)- Bellman Ford, Floyd Warshall (from source), Dijkstra

Python 3.8.18, recommended with pyenv

Install packages:

pip install -r requirements.txt

Run tests:

python setup.py pytest

Graph format:

{
  "edges": {
  "A->B": 3,
  "B->C": 2,
  "A->C": 5
  },
  "vertices": ["A", "B", "C"]
}