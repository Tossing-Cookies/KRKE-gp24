import csv
from rdflib import Graph, URIRef, Literal, RDF, RDFS, Namespace
from rdflib.namespace import XSD

# Define namespaces (modify as needed)
EX = Namespace("http://example.org/")

# Load the existing ontology
g = Graph()
g.parse("YOUTH.ttl", format="ttl")

# Read data from the CSV file
csv_file = 'youthsubcult_dataset.csv'
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Create a new individual URI based on data (modify as needed)
        individual_uri = URIRef(f"http://example.org/{row['id']}")
        
        # Add the individual to the graph with specific types and properties
        g.add((individual_uri, RDF.type, EX.SomeClass))  # Example class, adjust accordingly
        
        for key, value in row.items():
            if key != 'id':  # Skip the ID column
                # Add properties (modify according to your ontology)
                g.add((individual_uri, EX[key], Literal(value, datatype=XSD.string)))

# Serialize the updated graph to TTL format
g.serialize(destination="populated_ontology.ttl", format="ttl")
