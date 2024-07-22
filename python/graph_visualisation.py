import rdflib
import networkx as nx
import matplotlib.pyplot as plt

# Load the RDF graph
g = rdflib.Graph()
g.parse("knowledge_graph.ttl", format="ttl")

# Create a NetworkX graph
nx_graph = nx.Graph()

# Add nodes and edges from RDF triples
for s, p, o in g:
    nx_graph.add_node(str(s))
    nx_graph.add_node(str(o))
    nx_graph.add_edge(str(s), str(o), label=str(p))

# Draw the graph
pos = nx.spring_layout(nx_graph)
nx.draw(nx_graph, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold", arrows=True)
labels = nx.get_edge_attributes(nx_graph, "label")
nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=labels)

plt.show()