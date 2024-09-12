"""
Each query corresponds to one of the competency questions. 
The queries are structured using SPARQL and executed against the RDF graph. 
The results are printed for each question.


NB. CHECK THE PREDICATES !!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
"""

FIRST LEVEL OF YOUTH SUBCULTURES ONTOLOGY

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

# General Understanding
# 1. What are the main youth subcultures and their characteristics represented in the ontology?
query1 = """
SELECT ?subculture ?fashionStyle ?musicGenre ?ritual ?location ?historicalPeriod ?stereotype
WHERE {
  ?subculture a youth:YouthSubculture .
  OPTIONAL { ?subculture youth:hasFashionStyle ?fashionStyle . }
  OPTIONAL { ?subculture youth:hasMusicGenre ?musicGenre . }
  OPTIONAL { ?subculture youth:hasRitual ?ritual . }
  OPTIONAL { ?subculture youth:locatedIn ?location . }
  OPTIONAL { ?subculture youth:originatedIn ?historicalPeriod . }
  OPTIONAL { ?subculture youth:triggersStereotype ?stereotype . }
"""
print("Main youth subcultures:")
execute_query(query1)

# 2. What are the core values associated with each youth subculture?
query2 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?subculture ?coreValue
WHERE {
    ?subculture a ex:YouthSubculture ;
                ex:hasCoreValue ?coreValue .
}
"""
print("\nCore values of each youth subculture:")
execute_query(query2)

# 3. What are the typical activities or behaviors of individuals within each subculture?
query3 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?subculture ?activity
WHERE {
    ?subculture a ex:YouthSubculture ;
                ex:hasActivity ?activity .
}
"""
print("\nTypical activities or behaviors:")
execute_query(query3)

# Membership and Participation
# 1. Who are the members associated with a particular youth subculture?
query4 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?subculture ?member
WHERE {
    ?subculture a ex:YouthSubculture ;
                ex:hasMember ?member .
}
"""
print("\nMembers of each youth subculture:")
execute_query(query4)

# 2. What activities or events do individuals attend within a specific subculture?
query5 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?subculture ?event
WHERE {
    ?subculture a ex:YouthSubculture ;
                ex:attendsEvent ?event .
}
"""
print("\nActivities or events attended by subculture members:")
execute_query(query5)

# 3. What groups or communities do individuals participate in within a subculture?
query6 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?subculture ?group
WHERE {
    ?subculture a ex:YouthSubculture ;
                ex:participatesInGroup ?group .
}
"""
print("\nGroups or communities within each subculture:")
execute_query(query6)

# Cultural Aspects
# 1. What music genres are associated with a particular youth subculture?
query7 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?subculture ?musicGenre
WHERE {
    ?subculture a ex:YouthSubculture ;
                ex:associatedMusicGenre ?musicGenre .
}
"""
print("\nMusic genres associated with each subculture:")
execute_query(query7)

# 2. What fashion styles are characteristic of each youth subculture?
query8 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?subculture ?fashionStyle
WHERE {
    ?subculture a ex:YouthSubculture ;
                ex:characteristicFashionStyle ?fashionStyle .
}
"""
print("\nFashion styles characteristic of each subculture:")
execute_query(query8)

# 3. What symbols or artifacts are significant within a specific subculture?
query9 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?subculture ?symbol
WHERE {
    ?subculture a ex:YouthSubculture ;
                ex:significantSymbol ?symbol .
}
"""
print("\nSymbols or artifacts significant within each subculture:")
execute_query(query9)

# Geographic Context
# 1. Where are the main locations or geographic regions associated with each subculture?
query10 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?subculture ?location
WHERE {
    ?subculture a ex:YouthSubculture ;
                ex:associatedLocation ?location .
}
"""
print("\nLocations or geographic regions associated with each subculture:")
execute_query(query10)

# 2. What events or activities take place in a specific location within a subculture?
query11 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?location ?event
WHERE {
    ?location a ex:Location ;
              ex:hostsEvent ?event .
}
"""
print("\nEvents or activities in specific locations:")
execute_query(query11)

# Temporal Aspects
# 1. When did each youth subculture originate?
query12 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?subculture ?originDate
WHERE {
    ?subculture a ex:YouthSubculture ;
                ex:originatedOn ?originDate .
}
"""
print("\nOrigins of each youth subculture:")
execute_query(query12)

# 2. What historical influences contributed to the development of a specific subculture?
query13 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?subculture ?historicalInfluence
WHERE {
    ?subculture a ex:YouthSubculture ;
                ex:historicallyInfluencedBy ?historicalInfluence .
}
"""
print("\nHistorical influences on each subculture:")
execute_query(query13)

# 3. What current trends or developments are relevant within each subculture?
query14 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?subculture ?currentTrend
WHERE {
    ?subculture a ex:YouthSubculture ;
                ex:currentTrend ?currentTrend .
}
"""
print("\nCurrent trends or developments within each subculture:")
execute_query(query14)

# Media and Information
# 1. What media content (e.g., blogs, forums, videos) is consumed by individuals within a particular subculture?
query15 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?subculture ?mediaContent
WHERE {
    ?subculture a ex:YouthSubculture ;
                ex:consumesMediaContent ?mediaContent .
}
"""
print("\nMedia content consumed by subculture members:")
execute_query(query15)

# 2. What online communities or platforms are relevant to a specific subculture?
query16 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?subculture ?onlineCommunity
WHERE {
    ?subculture a ex:YouthSubculture ;
                ex:relevantOnlineCommunity ?onlineCommunity .
}
"""
print("\nOnline communities or platforms relevant to each subculture:")
execute_query(query16)

# 3. What artifacts or tangible items are associated with a particular subculture?
query17 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?subculture ?artifact
WHERE {
    ?subculture a ex:YouthSubculture ;
                ex:associatedArtifact ?artifact .
}
"""
print("\nArtifacts or tangible items associated with each subculture:")
execute_query(query17)

# Interactions and Influences
# 1. How do different youth subcultures influence each other?
query18 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?subculture1 ?subculture2
WHERE {
    ?subculture1 a ex:YouthSubculture ;
                 ex:influences ?subculture2 .
}
"""
print("\nInfluences between different subcultures:")
execute_query(query18)

# 2. What are the connections or relationships between individuals belonging to different subcultures?
query19 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?individual1 ?individual2
WHERE {
    ?individual1 a ex:Person ;
                 ex:connectedTo ?individual2 .
    ?individual1 ex:belongsTo ?subculture1 .
    ?individual2 ex:belongsTo ?subculture2 .
    FILTER (?subculture1 != ?subculture2)
}
"""
print("\nConnections between individuals of different subcultures:")
execute_query(query19)

# 3. How do individuals navigate between or participate in multiple subcultures?
query20 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?individual ?subculture
WHERE {
    ?individual a ex:Person ;
                ex:participatesIn ?subculture .
}
"""
print("\nIndividuals participating in multiple subcultures:")
execute_query(query20)

# Identity and Expression
# 1. How do individuals express their identity within a specific subculture?
query21 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?subculture ?expression
WHERE {
    ?subculture a ex:YouthSubculture ;
                ex:identityExpression ?expression .
}
"""
print("\nIdentity expression within each subculture:")
execute_query(query21)

# 2. What role does fashion play in the self-expression of individuals within each subculture?
query22 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?subculture ?fashionRole
WHERE {
    ?subculture a ex:YouthSubculture ;
                ex:fashionRole ?fashionRole .
}
"""
print("\nRole of fashion in self-expression:")
execute_query(query22)

# 3. How do individuals align with the core values and principles of a particular subculture?
query23 = """
PREFIX ex: <http://example.org/youth/>
SELECT ?individual ?subculture ?coreValue
WHERE {
    ?individual a ex:Person ;
                ex:alignsWith ?coreValue .
    ?subculture a ex:YouthSubculture ;
                ex:hasCoreValue ?coreValue .
}
"""
print("\nAlignment with core values and principles:")
execute_query(query23)