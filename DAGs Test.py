import networkx as nx
import matplotlib.pyplot as plt
import random

def generate_graph(num_nodes, num_edges,weight_scale):
    # Generate a random directed graph with negative weights
    G = nx.DiGraph()
    edges = []

    # Add nodes to the graph
    for node in range(num_nodes):
        G.add_node(node)

    # Add random edges with random weights (can be negative)
    attempts = 0
    while len(edges) < num_edges and attempts < num_edges * 10:  # Maximum attempts to prevent infinite loop
        source = random.randint(0, num_nodes - 1)
        target = random.randint(0, num_nodes - 1)
        weight = random.randint(-weight_scale, weight_scale)  # Allowing negative weights
        if source != target:  # Ensure source and target are not the same
            G.add_edge(source, target, weight=weight)
            if has_negative_cycle(G):
                G.remove_edge(source, target)  # Remove edge if it forms a negative cycle
            else:
                edges.append((source, target, weight))
        attempts += 1

    # Remove self-loops
    G.remove_edges_from(nx.selfloop_edges(G))

    # Convert edge list to string format
    edges_str = [f"{source} -> {target}, {weight}" for source, target, weight in edges]

    return G, edges_str  # Return a tuple of values

def has_negative_cycle(G):
    visited = set()
    stack = set()


    def dfs(node, accumulated_weight):
        if node in stack:
            return accumulated_weight < 0  # Check if the current path weight is negative
        if node in visited:
            return False

        visited.add(node)
        stack.add(node)
        for neighbor, edge_data in G[node].items():
            weight = edge_data['weight']
            if dfs(neighbor, accumulated_weight + weight):
                return True
        stack.remove(node)
        return False

    for node in G.nodes():
        if node not in visited:
            if dfs(node, 0):
                return True

    return False


def visualize_graph(G):
    pos = nx.spring_layout(G)
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title('Directed Graph with Edges Displayed')
    plt.show()

# Parameters
num_nodes = 20  # Number of nodes
num_edges = 40  # Number of edges
scale = 100     #scaling of the weights for each edge
# Generate the graph
G, edges = generate_graph(num_nodes, num_edges,scale)

# Print the list of edges
for edge in edges:
    print(edge)
print(nx.number_of_edges(G))
# Visualize the graph
visualize_graph(G)
