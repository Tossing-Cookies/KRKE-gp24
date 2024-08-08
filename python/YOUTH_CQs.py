"""

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
NB. CHECK THE PREDICATES 
and  replace the PREFIX URI with the actual namespace used in the RDF ontology
!!!!!!!!!!!!!!!!!!!!!!!!!!!!

"""
"""
SECOND LEVEL OF YOUTH SUBCULTURES ONTOLOGY: PERSPECTIVE CQS

This script parses the RDF data and executes the specified SPARQL queries, printing the results for each competency question. 

"""

import rdflib

# Load the RDF graph
YOUTHCqs = rdflib.Graph()
YOUTHCqs.parse("YOUTH.ttl", format="ttl")

# Function to execute and print SPARQL query results
def execute_query(query):
    results = YOUTHCqs.query(query)
    for row in results:
        print(row)

# Query: How are different youth subcultures viewed by mainstream society?
query_viewed_by_mainstream = """
PREFIX ex: <http://example.org/youth/>
SELECT ?subculture ?externalPerspective
WHERE {
    ?subculture ex:hasExternalPerspective ?externalPerspective .
}
"""
print("How are different youth subcultures viewed by mainstream society?")
execute_query(query_viewed_by_mainstream)

# Query: What factors shape the perspective of a particular youth subculture?
query_factors_shape_perspective = """
PREFIX ex: <http://example.org/youth/>
SELECT ?perspective ?influence
WHERE {
    ?perspective ex:shapedBy ?influence .
}
"""
print("\nWhat factors shape the perspective of a particular youth subculture?")
execute_query(query_factors_shape_perspective)

# Query: How do members of youth subcultures view their own identities?
query_view_own_identities = """
PREFIX ex: <http://example.org/youth/>
SELECT ?person ?internalPerspective
WHERE {
    ?person ex:hasInternalPerspective ?internalPerspective .
}
"""
print("\nHow do members of youth subcultures view their own identities?")
execute_query(query_view_own_identities)

# Query: What stereotypes are associated with each youth subculture, and how accurate are they?
query_stereotypes_associated = """
PREFIX ex: <http://example.org/youth/>
SELECT ?subculture ?stereotype
WHERE {
    ?subculture ex:reinforcesStereotype ?stereotype .
}
"""
print("\nWhat stereotypes are associated with each youth subculture, and how accurate are they?")
execute_query(query_stereotypes_associated)

# Query: How do youth subcultures challenge or reinforce societal perspectives?
query_challenge_reinforce = """
PREFIX ex: <http://example.org/youth/>
SELECT ?subculture ?stereotype
WHERE {
    ?subculture ex:challengesStereotype ?stereotype .
}
"""
print("\nHow do youth subcultures challenge or reinforce societal perspectives?")
execute_query(query_challenge_reinforce)