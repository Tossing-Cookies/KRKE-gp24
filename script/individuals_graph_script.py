import pandas as pd
from rdflib import Graph, Namespace, Literal, RDF
import os  

# Determine the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path for the CSV file
csv_path = os.path.join(script_dir, "youthsubcult_dataset.csv")

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(csv_path)

# Define namespaces
YOUTH = Namespace("http://www.semanticweb.org/ontologies/2024/YOUTH/")
OWL = Namespace("http://www.w3.org/2002/07/owl#")

# Create a new RDF graph
g = Graph()

# Bind namespaces for easier usage
g.bind("YOUTH", YOUTH)
g.bind("OWL", OWL)

def normalize_text(value):
    """Normalize the text by converting it to lowercase and removing unnecessary characters."""
    return value.strip().lower().replace(",", "").replace("and", "").replace(" and", "").replace("and ", "").replace(" and ", "").replace(" ", "_")

def create_uri(value):
    """Create a URI from the string of a cell-value, ensuring it is a valid RDF URI."""
    return YOUTH[normalize_text(value)]

def split_and_create_uris(value, rdf_type):
    """Split a comma-separated value into individual URIs and assign the correct type."""
    uris = []
    if value:
        items = [normalize_text(item) for item in value.split(",") if item.strip()]
        for item in items:
            uri = create_uri(f"{item}")
            # Assign the RDF type to the URI
            g.add((uri, RDF.type, rdf_type))
            uris.append(uri)
    return uris

def add_triple(df):
    df = df.fillna("")
    for index, row in df.iterrows():
        subculture_name = str(row['YouthSubculture']).replace(" ", "_")
        
        # Create URIs for Location, HistoricalPeriod, Stereotype, and MoralValue
        location_uri = create_uri(row['Location'])
        historical_period_uri = create_uri(row['HistoricalPeriod'])
        stereotype_uri = split_and_create_uris(row['Stereotype'], YOUTH.Stereotype)
        moral_value_uri = split_and_create_uris(row['MoralValue'], YOUTH.MoralValue)
        
        for col_name, value in row.items():
            pie_uri = YOUTH[value.replace(" ", "_").replace(",", "").replace("and", "").strip()]
            dir_uri = create_uri(value)
            con_uri = YOUTH[f"{col_name}_{index+1 }"]
            
            if col_name == "Participant" and row["Participant"] != "":
                g.add((dir_uri, RDF.type, YOUTH.Participant))
                g.add((dir_uri, YOUTH.participatesIn, YOUTH[subculture_name]))
                g.add((dir_uri, YOUTH.belongsToGeneration, Literal(row['Generation'])))
                g.add((pie_uri, YOUTH.hasViewpoint, YOUTH[row['Viewpoint']]))
                g.add((pie_uri, YOUTH.hasAttitude, YOUTH[row['Attitude']]))

            elif col_name == "NotParticipant" and row["NotParticipant"] != "":
                g.add((dir_uri, RDF.type, YOUTH.NotParticipant))
                g.add((dir_uri, YOUTH.hasname, Literal("Giovannina")))
                g.add((dir_uri, YOUTH.belongsToGeneration, Literal(row['Generation'])))
                g.add((pie_uri, YOUTH.hasViewpoint, YOUTH[row['Viewpoint']]))
                g.add((pie_uri, YOUTH.hasAttitude, YOUTH[row['Attitude']]))
                g.add((dir_uri, YOUTH.hasPerceptionOf, YOUTH[subculture_name]))

            elif col_name == "YouthSubculture" and row['Participant'] != "":
                g.add((dir_uri, RDF.type, YOUTH.YouthSubculture))
                g.add((dir_uri, YOUTH.locatedIn, location_uri)) 
                g.add((pie_uri, YOUTH.hasFashionStyle, YOUTH[f"FashionStyle_{index+1}"])) 
                g.add((pie_uri, YOUTH.hasMusicGenre, YOUTH[f"MusicGenre_{index+1}"])) 
                g.add((pie_uri, YOUTH.hasRitual, YOUTH[f"Ritual_{index+1}"])) 
                if moral_value_uri:
                    for mv_uri in moral_value_uri:
                        g.add((dir_uri, YOUTH.hasMoralValue, mv_uri))
                g.add((dir_uri, YOUTH.originatedIn, historical_period_uri)) 
                if stereotype_uri:
                    for st_uri in stereotype_uri:
                        g.add((dir_uri, YOUTH.triggersStereotype, st_uri))

            elif col_name == "Viewpoint":
                if row["Viewpoint"] == "InternalViewpoint":
                    g.add((dir_uri, RDF.type, YOUTH.InternalViewpoint))
                elif row["Viewpoint"] == "ExternalViewpoint":
                    g.add((dir_uri, RDF.type, YOUTH.ExternalViewpoint))
                g.add((pie_uri, YOUTH.isCharacterisedBy, YOUTH[f"PerspectiveShift_{index+1}"]))
                g.add((pie_uri, YOUTH.determines, YOUTH[row['Attitude']]))

            elif col_name == "Attitude":
                if row['Participant']:
                    if row['Attitude'] == "Positive":
                        g.add((dir_uri, RDF.type, YOUTH.PositiveAttitude))
                    elif row['Attitude'] == "Negative":
                        g.add((dir_uri, RDF.type, YOUTH.NegativeAttitude))
                    elif row['Attitude'] == "Neutral":
                        g.add((dir_uri, RDF.type, YOUTH.NeutralAttitude))
                    if stereotype_uri:
                        for st_uri in stereotype_uri:
                            g.add((dir_uri, YOUTH.expressedVia, st_uri))
                    if moral_value_uri:
                        for mv_uri in moral_value_uri:
                            g.add((dir_uri, YOUTH.expressedVia, mv_uri))
                    g.add((pie_uri, YOUTH.influencedBy, YOUTH[f"Influence_{index+1}"]))
                    g.add((pie_uri, YOUTH.isAttitudeOf, YOUTH[row['Participant']]))

            elif row['NotParticipant']:
                if row['Attitude'] == "Positive":
                    g.add((dir_uri, RDF.type, YOUTH.PositiveAttitude))
                elif row['Attitude'] == "Negative":
                    g.add((dir_uri, RDF.type, YOUTH.NegativeAttitude))
                elif row['Attitude'] == "Neutral":
                    g.add((dir_uri, RDF.type, YOUTH.NeutralAttitude))
                if stereotype_uri:
                    for st_uri in stereotype_uri:
                        g.add((dir_uri, YOUTH.expressedVia, st_uri))
                if moral_value_uri:
                    for mv_uri in moral_value_uri:
                        g.add((dir_uri, YOUTH.expressedVia, mv_uri))
                g.add((pie_uri, YOUTH.influencedBy, YOUTH[f"Influence_{index+1}"]))
                g.add((pie_uri, YOUTH.isAttitudeOf, YOUTH[row['NotParticipant']]))
                
            elif col_name == "FashionStyle":
                g.add((con_uri, RDF.type, YOUTH.FashionStyle))
                g.add((con_uri, YOUTH.hasContent, Literal(row["FashionStyle"])))

            elif col_name == "MusicGenre":
                g.add((con_uri, RDF.type, YOUTH.MusicGenre))
                g.add((con_uri, YOUTH.hasContent, Literal(row["MusicGenre"])))

            elif col_name == "Ritual":
                g.add((con_uri, RDF.type, YOUTH.Ritual))
                g.add((con_uri, YOUTH.hasContent, Literal(row["Ritual"])))

            elif col_name == "Influence": 
                g.add((con_uri, RDF.type, YOUTH.Influence))
                g.add((con_uri, YOUTH.hasContent, Literal(row["Influence"])))
                g.add((con_uri, YOUTH.influences, YOUTH[row["Attitude"]]))

            elif col_name == "PerspectiveShift": 
                g.add((con_uri, RDF.type, YOUTH.PerspectiveShift))
                g.add((con_uri, YOUTH.hasContent, Literal(row["PerspectiveShift"])))

    # Add ObjectProperties
    g.add((YOUTH.determines, RDF.type, OWL.ObjectProperty))
    g.add((YOUTH.expressedVia, RDF.type, OWL.ObjectProperty))
    g.add((YOUTH.hasAttitude, RDF.type, OWL.ObjectProperty))
    g.add((YOUTH.hasFashionStyle, RDF.type, OWL.ObjectProperty))
    g.add((YOUTH.hasMusicGenre, RDF.type, OWL.ObjectProperty))
    g.add((YOUTH.hasParticipant, RDF.type, OWL.ObjectProperty))
    g.add((YOUTH.hasRitual, RDF.type, OWL.ObjectProperty))
    g.add((YOUTH.hasMoralValue, RDF.type, OWL.ObjectProperty))
    g.add((YOUTH.hasViewpoint, RDF.type, OWL.ObjectProperty))
    g.add((YOUTH.influencedBy, RDF.type, OWL.ObjectProperty))
    g.add((YOUTH.influences, RDF.type, OWL.ObjectProperty))
    g.add((YOUTH.isAttitudeOf, RDF.type, OWL.ObjectProperty))
    g.add((YOUTH.isCharacterisedBy, RDF.type, OWL.ObjectProperty))
    g.add((YOUTH.isExpressedVia, RDF.type, OWL.ObjectProperty))
    g.add((YOUTH.isViewpointOf, RDF.type, OWL.ObjectProperty))
    g.add((YOUTH.locatedIn, RDF.type, OWL.ObjectProperty))
    g.add((YOUTH.ClassifiedBy, RDF.type, OWL.ObjectProperty))
    g.add((YOUTH.originatedIn, RDF.type, OWL.ObjectProperty))
    g.add((YOUTH.participatesIn, RDF.type, OWL.ObjectProperty))
    g.add((YOUTH.triggersStereotype, RDF.type, OWL.ObjectProperty))
    g.add((YOUTH.hasPerceptionOf, RDF.type, OWL.ObjectProperty))

add_triple(df)

output_path = os.path.join(script_dir, "individuals_graph.ttl")
# Serialize the graph to a Turtle file
with open(output_path, "w", encoding="utf-8") as f:
    f.write(g.serialize(format="turtle"))
