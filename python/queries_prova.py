import rdflib

# Load the RDF graph
g = rdflib.Graph()
g.parse("knowledge_graph.ttl", format="ttl")

# Define a SPARQL query
query = """
SELECT ?person ?subculture ?activity
WHERE {
    ?person <http://example.org/ontology/participatesIn> ?subculture .
    ?subculture <http://example.org/ontology/hasRitual> ?ritual .
    ?ritual <http://example.org/ontology/engagesIn> ?activity .
}
"""

# Execute the query
results = g.query(query)

# Print the results
for row in results:
    print(f"Person: {row.person}, Subculture: {row.subculture}, Activity: {row.activity}")