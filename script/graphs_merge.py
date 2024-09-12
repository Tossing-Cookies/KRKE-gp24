import os
from rdflib import Graph

# Determine the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the paths to the input files
ontology_file = os.path.join(script_dir, "..", "YOUTH.ttl")  # Root directory
populated_file = os.path.join(script_dir, "individuals_graph.ttl") 

# Load the ontology graph
ontology_graph = Graph()
ontology_graph.parse(ontology_file, format="turtle")

# Load the populated ontology graph
populated_graph = Graph()
populated_graph.parse(populated_file, format="turtle")

# Merge the populated graph into the ontology graph
ontology_graph += populated_graph

# Define the path for the output file
merged_file = os.path.join(script_dir, "knowledge_graph.ttl")

# Serialize the merged graph to the output file
with open(merged_file, "w", encoding="utf-8") as f:
    f.write(ontology_graph.serialize(format="turtle"))
