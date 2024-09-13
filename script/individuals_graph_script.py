import pandas as pd
from rdflib import Graph, Namespace, Literal, RDF, URIRef, RDFS
import os

# Define namespaces
YOUTH = Namespace("http://www.semanticweb.org/ontologies/2024/YOUTH/")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
FRAME = Namespace("http://etna.istc.cnr.it/framester2/data/framestercore/")

# Create a new RDF graph
g = Graph()

# Bind namespaces for easier usage
g.bind("YOUTH", YOUTH)
g.bind("OWL", OWL)
g.bind("FRAME", FRAME)

# Define properties
g.add((YOUTH.participatesIn, RDF.type, OWL.ObjectProperty))
g.add((YOUTH.hasParticipant, RDF.type, OWL.ObjectProperty))
g.add((YOUTH.locatedIn, RDF.type, OWL.ObjectProperty))
g.add((YOUTH.determines, RDF.type, OWL.ObjectProperty))
g.add((YOUTH.influencedBy, RDF.type, OWL.ObjectProperty))
g.add((YOUTH.expressedVia, RDF.type, OWL.ObjectProperty))
g.add((YOUTH.isExpressedVia, RDF.type, OWL.ObjectProperty))
g.add((YOUTH.isCharacterisedBy, RDF.type, OWL.ObjectProperty))
g.add((YOUTH.influences, RDF.type, OWL.ObjectProperty))
g.add((YOUTH.isViewpointOf, RDF.type, OWL.ObjectProperty))
g.add((YOUTH.hasPerceptionOf, RDF.type, OWL.ObjectProperty))
g.add((YOUTH.hasFashionStyle, RDF.type, OWL.ObjectProperty))
g.add((YOUTH.hasMusicGenre, RDF.type, OWL.ObjectProperty))
g.add((YOUTH.hasRitual, RDF.type, OWL.ObjectProperty))
g.add((YOUTH.hasName, RDF.type, OWL.DatatypeProperty))
g.add((YOUTH.hasContent, RDF.type, OWL.DatatypeProperty))
g.add((YOUTH.belongsToGeneration, RDF.type, OWL.DatatypeProperty))
g.add((YOUTH.originatedIn, RDF.type, OWL.ObjectProperty))
g.add((YOUTH.triggersStereotype, RDF.type, OWL.ObjectProperty))
g.add((YOUTH.hasMoralValue, RDF.type, OWL.ObjectProperty))
g.add((YOUTH.hasViewpoint, RDF.type, OWL.ObjectProperty))


def normalize_text(value):
    """Normalize the text by converting it to lowercase and removing unnecessary characters."""
    return value.strip().lower().replace(",", "").replace("and", "").replace(" and", "").replace("and ", "").replace(" and ", "").replace(" ", "_")

def create_uri(value):
    """Create a URI from the string of a cell-value, ensuring it is a valid RDF URI."""
    return URIRef(YOUTH[normalize_text(value)])

def get_or_create_uri(value, rdf_type):
    """Get or create a URI for a given value and RDF type, caching URIs to avoid duplicates."""
    if value:
        normalized_value = normalize_text(value)
        uri = URIRef(YOUTH[normalized_value])
        if (uri, RDF.type, rdf_type) not in g:
            g.add((uri, RDF.type, rdf_type))
        return uri
    return None

def add_triple(df):
    df = df.fillna("")

    # Add subclass relationships
    g.add((YOUTH.Participant, RDFS.subClassOf, FRAME.People))
    g.add((YOUTH.NotParticipant, RDFS.subClassOf, FRAME.People))

    for index, row in df.iterrows():
        subculture_name = normalize_text(str(row['YouthSubculture']).replace(" ", "_"))

        # Create URIs for Location, HistoricalPeriod, Stereotype, and MoralValue
        location_uri = get_or_create_uri(row['Location'], YOUTH.Location)
        historical_period_uri = get_or_create_uri(row['HistoricalPeriod'], YOUTH.HistoricalPeriod)
        stereotype_uris = [get_or_create_uri(item, YOUTH.Stereotype) for item in row['Stereotype'].split(',') if item.strip()]
        moral_value_uris = [get_or_create_uri(item, YOUTH.MoralValue) for item in row['MoralValue'].split(',') if item.strip()]

        for col_name, value in row.items():
            if col_name in ["Participant", "NotParticipant"]:
                # Determine the RDF type and create the URI for the person
                rdf_type = YOUTH.Participant if col_name == "Participant" else YOUTH.NotParticipant
                if value:
                    person_uri = get_or_create_uri(value, rdf_type)
                    if person_uri:
                        # Add triples related to the person's attitude and viewpoint
                        if row["Viewpoint"]:
                            viewpoint_uri = URIRef(YOUTH[row["Viewpoint"]])
                            g.add((person_uri, YOUTH.hasViewpoint, viewpoint_uri))
                            # Add inverse relationship
                            g.add((viewpoint_uri, YOUTH.isViewpointOf, person_uri))
                            # Add triple to link viewpoint with PerspectiveShift
                            perspective_shift_uri = get_or_create_uri(f"PerspectiveShift_{index + 1}", YOUTH.PerspectiveShift)
                            g.add((viewpoint_uri, YOUTH.isCharacterisedBy, perspective_shift_uri))
                        if row["Attitude"]:
                            attitude_uri = URIRef(YOUTH[row["Attitude"]])
                            g.add((person_uri, YOUTH.hasAttitude, attitude_uri))
                            # Add triple to link attitude with its influence
                            influence_uri = URIRef(YOUTH[f"Influence_{index + 1}"])
                            g.add((attitude_uri, YOUTH.influencedBy, influence_uri))
                            g.add((influence_uri, RDF.type, YOUTH.Influence))
                            g.add((influence_uri, YOUTH.hasContent, Literal(value)))
                            # Add triple to link influence with attitude
                            g.add((influence_uri, YOUTH.influences, attitude_uri))
                            # Link attitude to stereotype or moral value
                            for st_uri in stereotype_uris:
                                g.add((attitude_uri, YOUTH.expressedVia, st_uri))
                                g.add((st_uri, YOUTH.isExpressedVia, attitude_uri))
                            for mv_uri in moral_value_uris:
                                g.add((attitude_uri, YOUTH.expressedVia, mv_uri))
                                g.add((mv_uri, YOUTH.isExpressedVia, attitude_uri))
                        g.add((person_uri, YOUTH.belongsToGeneration, Literal(row['Generation'])))

                        # Handle YouthSubculture only if NotParticipant column is empty
                        if row["NotParticipant"]:
                            g.add((person_uri, YOUTH.hasName, Literal("John Doe")))
                            continue  # Skip further processing for this row if NotParticipant has value

                        if row["YouthSubculture"]:
                            subculture_uri = get_or_create_uri(row["YouthSubculture"], YOUTH.YouthSubculture)
                            g.add((subculture_uri, YOUTH.hasParticipant, person_uri))
                            g.add((subculture_uri, YOUTH.locatedIn, location_uri))
                            g.add((subculture_uri, YOUTH.originatedIn, historical_period_uri))
                            for st_uri in stereotype_uris:
                                g.add((subculture_uri, YOUTH.triggersStereotype, st_uri))
                            for mv_uri in moral_value_uris:
                                g.add((subculture_uri, YOUTH.hasMoralValue, mv_uri))

                                # Add triple to link Participant to YouthSubculture
                            if rdf_type == YOUTH.Participant:
                                g.add((person_uri, YOUTH.participatesIn, subculture_uri))

            elif col_name in ["FashionStyle", "MusicGenre", "Ritual", "PerspectiveShift"]:
                rdf_type = getattr(YOUTH, col_name)
                content_uri = get_or_create_uri(f"{col_name}_{index + 1}", rdf_type)
                if value:
                    g.add((content_uri, RDF.type, rdf_type))
                    g.add((content_uri, YOUTH.hasContent, Literal(value)))
                    if row["YouthSubculture"]:
                        subculture_uri = get_or_create_uri(row["YouthSubculture"], YOUTH.YouthSubculture)
                        if col_name == "FashionStyle":
                            g.add((subculture_uri, YOUTH.hasFashionStyle, content_uri))
                        elif col_name == "MusicGenre":
                            g.add((subculture_uri, YOUTH.hasMusicGenre, content_uri))
                        elif col_name == "Ritual":
                            g.add((subculture_uri, YOUTH.hasRitual, content_uri))
                    if row["YouthSubculture"] and not row["NotParticipant"]:
                        subculture_uri = get_or_create_uri(row["YouthSubculture"], YOUTH.YouthSubculture)
                        g.add((subculture_uri, getattr(YOUTH, f"has{col_name}"), content_uri))

        # Add the determines triple between Viewpoint and Attitude
        if row["Viewpoint"] and row["Attitude"]:
            viewpoint_uri = URIRef(YOUTH[row["Viewpoint"]])
            attitude_uri = URIRef(YOUTH[row["Attitude"]])
            g.add((viewpoint_uri, YOUTH.determines, attitude_uri))

        # Add the hasPerceptionOf triple if NotParticipant exists
        if row["NotParticipant"] and row["YouthSubculture"]:
            person_uri = get_or_create_uri(row["NotParticipant"], YOUTH.NotParticipant)
            g.add((person_uri, YOUTH.hasPerceptionOf, get_or_create_uri(row["YouthSubculture"], YOUTH.YouthSubculture)))

    return g

# Determine the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path for the CSV file
csv_path = os.path.join(script_dir, "youthsubcult_dataset.csv")

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(csv_path)

# Add triples to the RDF graph
add_triple(df)

# Define the output path for the RDF graph
output_path = os.path.join(script_dir, "individuals_graph.ttl")

# Serialize the graph to a Turtle file
with open(output_path, "w", encoding="utf-8") as f:
    f.write(g.serialize(format="turtle"))
