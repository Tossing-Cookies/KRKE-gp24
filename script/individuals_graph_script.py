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

def add_triple(df):

    for index , row in df.iterrows():

        for col_name, value in row.items():
            
                dir_uri = YOUTH[value]
                con_uri = YOUTH[f"{col_name}_{index+1 }"]
                
                if col_name == "Participant" and row["Participant"]!="":
                    g.add((dir_uri, RDF.type, YOUTH.Participant))
                    g.add((dir_uri, YOUTH.participatesIn, YOUTH[row['YouthSubculture']]))
                    g.add((dir_uri, YOUTH.belongsToGeneration, Literal(row['Generation'])))
                    g.add((dir_uri, YOUTH.hasViewpoint, YOUTH[row['Viewpoint']]))
                    g.add((dir_uri, YOUTH.hasAttitude, YOUTH[row['Attitude']]))

                elif col_name == "NotParticipant"and row["NotParticipant"]!="":
                    g.add((dir_uri, RDF.type, YOUTH.NotParticipant))
                    g.add((dir_uri, YOUTH.hasname, Literal("Giovannina")))
                    g.add((dir_uri, YOUTH.belongsToGeneration, Literal(row['Generation'])))
                    g.add((dir_uri, YOUTH.hasViewpoint, YOUTH[row['Viewpoint']]))
                    g.add((dir_uri, YOUTH.hasAttitude, YOUTH[row['Attitude']]))

                elif col_name == "YouthSubculture" and row['Participant'] != "":
                    g.add((dir_uri, YOUTH.hasParticipant, YOUTH[row['Participant']]))
                    g.add((dir_uri, RDF.type, YOUTH.YouthSubculture))
                    g.add((dir_uri, YOUTH.locatedIn, YOUTH[f"Location_{index+1}"])) 
                    g.add((dir_uri, YOUTH.hasFashionStyle, YOUTH[f"FashionStyle_{index+1}"])) 
                    g.add((dir_uri, YOUTH.hasMusicGenre , YOUTH[f"MusicGenre_{index+1}"])) 
                    g.add((dir_uri, YOUTH.hasRitual, YOUTH[f"Ritual_{index+1}"])) 
                    g.add((dir_uri, YOUTH.hasMoralValue, YOUTH[f"MoralValue_{index+1}"]))
                    g.add((dir_uri, YOUTH.originatesIn, YOUTH[f"HistoricalPeriod_{index+1}"])) 
                    g.add((dir_uri, YOUTH.triggersStereotype, YOUTH[f"Stereotype_{index+1}"]))

                elif col_name == "Viewpoint": 
                    g.add((dir_uri, RDF.type, YOUTH.Viewpoint))
                    g.add((dir_uri, YOUTH.isCharacterisedBy, YOUTH[row['Attitude']]))
                    g.add((dir_uri, YOUTH.determinesShift, YOUTH[f"PerspectiveShift_{index+1}"]))

                elif col_name == "Location":
                    g.add((con_uri, RDF.type, YOUTH.Location))
                    g.add((con_uri, YOUTH.hasContent, Literal(row["Location"])))
                    
                elif col_name == "Attitude" and row['Participant'] != "": 
                    g.add((dir_uri, RDF.type, YOUTH.Attitude))
                    g.add((dir_uri, YOUTH.expressedVia, YOUTH[f"Stereotype_{index+1}"]))
                    g.add((dir_uri, YOUTH.expressedVia, YOUTH[f"MoralValue_{index+1}"]))
                    g.add((dir_uri, YOUTH.influencedBy, YOUTH[f"PerspectiveInfuece_{index+1}"]))
                    g.add((dir_uri, YOUTH.isAttitudeOf, YOUTH[row['Participant']]))

                elif col_name == "Attitude" and row['NotParticipant'] != "": 
                    g.add((dir_uri, RDF.type, YOUTH.Attitude))
                    g.add((dir_uri, YOUTH.expressedVia, YOUTH[f"Stereotype_{index+1}"]))
                    g.add((dir_uri, YOUTH.expressedVia, YOUTH[f"MoralValue_{index+1}"]))
                    g.add((dir_uri, YOUTH.influencedBy, YOUTH[f"PerspectiveInfuece_{index+1}"]))
                    g.add((dir_uri, YOUTH.isAttitudeOf, YOUTH[row['NotParticipant']]))
                    
                elif col_name == "MoralValue":
                    g.add((con_uri, RDF.type, YOUTH.MoralValue))
                    g.add((con_uri, YOUTH.hasContent, Literal(row["MoralValue"]))) 
                    g.add((con_uri, YOUTH.isExpressedVia, YOUTH[row["Attitude"]]))
                
                elif col_name == "HistoricalPeriod":
                    g.add((con_uri, RDF.type, YOUTH.HistoricalPeriod))
                    g.add((con_uri, YOUTH.hasContent, Literal(row["HistoricalPeriod"])))

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
                    g.add((con_uri, RDF.type, YOUTH.PerspectiveInfluence))
                    g.add((con_uri, YOUTH.hasContent, Literal(row["Influence"])))
                    g.add((con_uri, YOUTH.influences, YOUTH[row["Attitude"]]))

                elif col_name == "Stereotype": 
                    g.add((con_uri, RDF.type, YOUTH.Stereotype))
                    g.add((con_uri, YOUTH.hasContent, Literal(row["Stereotype"])))
                    g.add((con_uri, YOUTH.isExpressedVia, YOUTH[row["Attitude"]]))
                
                elif col_name == "PerspectiveShift": 
                    g.add((con_uri, RDF.type, YOUTH.PerspectiveShift))
                    g.add((con_uri, YOUTH.hasContent, Literal(row["PerspectiveShift"])))

        g.add((YOUTH.contrasts, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.creates, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.determines, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.expressedVia, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.extractedFrom, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.hasAttitude, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.hasFashionStyle, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.hasMusicGenre, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.hasParticipant, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.hasRitual, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.vhasMoralValue, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.hasViewpoint, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.holds, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.influencedBy, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.influences, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.isAttitudeOf, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.isCharacterisedBy, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.isExpressedVia, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.isSatisfiedBy, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.isSettingFor, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.isViewpointOf, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.locatedIn, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.ClassifiedBy, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.originatedIn, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.participatesIn, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.perspectivisedAs, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.perspectivisedThrough, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.satisfies, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.shotThrough, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.toward, RDF.type, OWL.ObjectProperty))
        g.add((YOUTH.triggersStereotype, RDF.type, OWL.ObjectProperty))
            
add_triple(df)

output_path = os.path.join(script_dir, "individuals_graph.ttl")
        # Serialize the graph to a Turtle file
with open(output_path, "w", encoding="utf-8") as f:
                    f.write(g.serialize(format="turtle"))



