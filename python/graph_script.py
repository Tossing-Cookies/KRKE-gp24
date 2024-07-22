import rdflib
import pandas as pd
from rdflib import URIRef, Literal, RDF
from rdflib.namespace import RDF, RDFS, OWL

# Load the ontology
g = rdflib.Graph()
g.parse("YOUTH.ttl", format="ttl")

# Load the CSV file
df = pd.read_csv("dataset_lu.csv")

# Define RDF namespaces
EX = rdflib.Namespace("http://example.org/")

# Create RDF Triples from CSV Data
def create_uri(subject, base_uri="http://example.org/"):
    return URIRef(base_uri + subject.replace(" ", "_"))

# Iterate over rows and create triples
for index, row in df.iterrows():
    person_uri = create_uri(row["Person"])
    
    # Define triples based on the CSV columns
    triples = [
        (person_uri, EX.belongsToSubculture, create_uri(row["YouthSubculture"])),
        (person_uri, EX.hasFashionStyle, create_uri(row["FashionStyle"])),
        (person_uri, EX.hasMusicGenre, create_uri(row["MusicGenre"])),
        (person_uri, EX.usesSlang, create_uri(row["Slang"])),
        (person_uri, EX.participatesInRitual, create_uri(row["Ritual"])),
        (person_uri, EX.engagesInActivity, create_uri(row["Activity"])),
        (person_uri, EX.attendsEvent, create_uri(row["Event"])),
        (person_uri, EX.followsValue, create_uri(row["Value"])),
        (person_uri, EX.consumesMedia, create_uri(row["Media"])),
        (person_uri, EX.isLocatedIn, create_uri(row["Location"])),
        (person_uri, EX.originatedInHistoricalPeriod, create_uri(row["HistoricalPeriod"]))
    ]
    
    # Add triples to the graph
    for triple in triples:
        g.add(triple)

# Save the graph in Turtle format
g.serialize("knowledge_graph.ttl", format="ttl")

