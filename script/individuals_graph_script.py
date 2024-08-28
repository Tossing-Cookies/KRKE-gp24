import pandas as pd
from rdflib import Graph, Namespace, URIRef, Literal, RDF, RDFS

# Define namespaces
YOUTH = Namespace("http://www.semanticweb.org/ontologies/2024/YOUTH/")
FOAF = Namespace("http://xmlns.com/foaf/0.1/")

# Create a new RDF graph
g = Graph()

# Bind namespaces for easier usage
g.bind("youth", YOUTH)
g.bind("foaf", FOAF)

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("./script/youthsubcult_dataset.csv")

# Define a function to add a person to the ontology
def add_person(row):
    person_uri = YOUTH[row['Person']]
    
    g.add((person_uri, RDF.type, YOUTH.Person))
    g.add((person_uri, FOAF.name, Literal(row['Person'])))
    g.add((person_uri, YOUTH.youthSubculture, Literal(row['YouthSubculture'])))
    g.add((person_uri, YOUTH.fashionStyle, Literal(row['FashionStyle'].strip('"'))))
    g.add((person_uri, YOUTH.musicGenre, Literal(row['MusicGenre'])))
    g.add((person_uri, YOUTH.ritual, Literal(row['Ritual'])))
    g.add((person_uri, YOUTH.value, Literal(row['Value'])))
    g.add((person_uri, YOUTH.location, Literal(row['Location'])))
    g.add((person_uri, YOUTH.historicalPeriod, Literal(row['HistoricalPeriod'])))
    g.add((person_uri, YOUTH.externalPerspective, Literal(row['ExternalPerspective'])))
    g.add((person_uri, YOUTH.internalPerspective, Literal(row['InternalPerspective'])))
    g.add((person_uri, YOUTH.perspectiveInfluence, Literal(row['PerspectiveInfluence'])))
    g.add((person_uri, YOUTH.stereotype, Literal(row['Stereotype'])))
    g.add((person_uri, YOUTH.perspectiveChange, Literal(row['PerspectiveChange'])))

# Iterate over DataFrame rows and add each person to the graph
for _, row in df.iterrows():
    add_person(row)

# Serialize the graph to a Turtle file
with open("individuals_ontology.ttl", "w", encoding="utf-8") as f:
    f.write(g.serialize(format="turtle"))
