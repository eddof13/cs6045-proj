import networkx as nx
import matplotlib.pyplot as plt
import random

# Genereates a graph using the Python networks library, this is used to add nodes and edges
def generate_graph(num_nodes, num_edges, weight_scale):
    G = nx.DiGraph()
    edges = {}

    for node in range(num_nodes):
        G.add_node(node)

    attempts = 0
    #iterativly adds edges by checking for negative cycles and self loops
    while len(list(edges.keys())) < num_edges and attempts < num_edges * 100: 
        source = random.randint(0, num_nodes - 1)
        target = random.randint(0, num_nodes - 1)
        weight = random.randint(-weight_scale, weight_scale)
        if source != target and (source, target) not in G.edges():
            G.add_edge(source, target, weight=weight)
            if not has_negative_cycle(G):
                edges[f"{source}->{target}"] = weight
            else:
                G.remove_edge(source, target)
        attempts += 1

    return G, edges

def has_negative_cycle(G): 
    visited = set()
    stack = set()

     #uses depth first search to check if negative cycles are present
    def dfs(node, accumulated_weight):
        if node in stack:
            return accumulated_weight < 0
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

#simple code to visualize the graph that was generated, mainly used for debugging 
def visualize_graph(G): 
    pos = nx.spring_layout(G)
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title('Directed Graph with Edges Displayed')
    plt.show()

# Parameters

'''Dense and Large graphs
    A large graph here is defined to be a graph of nodes > 40
    Dense graphs are more formally difined by the density function whereby the density is #Edges/((#nodes)(#nodes-1))
    The higheest possible density is defined to be 1, so for a graph to be truly dense, the number of edges have to be around the square of the number of nodes
    '''

'''Store test cases:
Large and desnse (has negative and positive weights):
    num_nodes = 200
    num_edges=num_nodes*(num_nodes-1)

Large and Sparse:
    num_nodes = 200
    num_edges = num_nodes*2

Small and desnse:
    num_nodes = 20
    num_edges=num_nodes*(num_nodes-1)

Small and Sparse:
    num_nodes = 20
    num_edges = num_nodes*2
 '''
num_nodes = 20
num_edges=num_nodes*(num_nodes-1)
# num_edges = num_nodes*2 #this well never be dense as the value will never be close to a perfect square of the number of nodes
scale = 100

# Generate the graph
G, edges = generate_graph(num_nodes, num_edges, scale)

# Write the edges and vertices to a text file format is a dictionary thats read by the main programs 
output_file_path = 'output.txt'
with open(output_file_path, 'w') as file:
    file.write('"edges": {\n')
    edges_list = [f'    "{edge}": {weight}' for edge, weight in edges.items()]
    file.write(",\n".join(edges_list) + "\n")
    file.write('},\n')
    file.write('"vertices": ')
    file.write(str([str(node) for node in G.nodes()]) + "\n")

print("Edges and vertices written to", output_file_path)
print(nx.density(G))
# Visualize the graph
visualize_graph(G)

