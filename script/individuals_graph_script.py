import pandas as pd
from rdflib import Graph, Namespace, Literal, RDF, URIRef
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
    return URIRef(YOUTH[normalize_text(value)])  # Use URIRef to create a valid RDF term

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

    # Dictionaries to keep track of created URIs
    uri_cache = {}

    def get_or_create_uri(value, rdf_type=None):
        """Get the URI from the cache or create a new one if not exists."""
        normalized_value = normalize_text(value)
        if normalized_value not in uri_cache:
            new_uri = create_uri(value)
            if rdf_type:
                g.add((new_uri, RDF.type, rdf_type))
            uri_cache[normalized_value] = new_uri
        return uri_cache[normalized_value]

    for index, row in df.iterrows():
        subculture_name = normalize_text(str(row['YouthSubculture']).replace(" ", "_"))

        # Create URIs for Location, HistoricalPeriod, Stereotype, and MoralValue
        location_uri = get_or_create_uri(row['Location'])
        historical_period_uri = get_or_create_uri(row['HistoricalPeriod'])
        stereotype_uris = split_and_create_uris(row['Stereotype'], YOUTH.Stereotype)
        moral_value_uris = split_and_create_uris(row['MoralValue'], YOUTH.MoralValue)

        for col_name, value in row.items():
            if col_name in ["Participant", "NotParticipant"]:
                rdf_type = YOUTH.Participant if col_name == "Participant" else YOUTH.NotParticipant
                dir_uri = get_or_create_uri(value, rdf_type)
                if col_name == "Participant":
                    g.add((dir_uri, YOUTH.belongsToGeneration, Literal(row['Generation'])))
                    g.add((dir_uri, YOUTH.participatesIn, URIRef(YOUTH[subculture_name])))
                else:
                    g.add((dir_uri, YOUTH.belongsToGeneration, Literal(row['Generation'])))
                    g.add((dir_uri, YOUTH.hasname, Literal("Giovannina")))  # Replace this as needed
                    g.add((dir_uri, YOUTH.hasPerceptionOf, URIRef(YOUTH[subculture_name])))

            elif col_name == "YouthSubculture":
                subculture_uri = get_or_create_uri(value, YOUTH.YouthSubculture)
                g.add((subculture_uri, YOUTH.locatedIn, location_uri))
                g.add((subculture_uri, YOUTH.originatedIn, historical_period_uri))
                for st_uri in stereotype_uris:
                    g.add((subculture_uri, YOUTH.triggersStereotype, st_uri))
                for mv_uri in moral_value_uris:
                    g.add((subculture_uri, YOUTH.hasMoralValue, mv_uri))

            elif col_name == "Viewpoint":
                viewpoint_uri = None
                if row["Viewpoint"] == "InternalViewpoint":
                    viewpoint_uri = URIRef(YOUTH.InternalViewpoint)
                elif row["Viewpoint"] == "ExternalViewpoint":
                    viewpoint_uri = URIRef(YOUTH.ExternalViewpoint)
                
                if viewpoint_uri:
                    g.add((get_or_create_uri(value), YOUTH.isCharacterisedBy, get_or_create_uri(f"PerspectiveShift_{index+1}", YOUTH.PerspectiveShift)))
                    g.add((get_or_create_uri(value), YOUTH.determines, get_or_create_uri(row['Attitude'])))

            elif col_name == "Attitude":
                attitude_type = {
                    "Positive": YOUTH.PositiveAttitude,
                    "Negative": YOUTH.NegativeAttitude,
                    "Neutral": YOUTH.NeutralAttitude
                }.get(value, None)
                if attitude_type:
                    attitude_uri = get_or_create_uri(value, attitude_type)
                    if col_name == "Participant":
                        g.add((get_or_create_uri(row['Participant']), YOUTH.isAttitudeOf, attitude_uri))
                    else:
                        g.add((get_or_create_uri(row['NotParticipant']), YOUTH.isAttitudeOf, attitude_uri))
                    for st_uri in stereotype_uris:
                        g.add((attitude_uri, YOUTH.expressedVia, st_uri))
                    for mv_uri in moral_value_uris:
                        g.add((attitude_uri, YOUTH.expressedVia, mv_uri))
                    g.add((get_or_create_uri(f"Influence_{index+1}"), YOUTH.influencedBy, attitude_uri))

            elif col_name in ["FashionStyle", "MusicGenre", "Ritual", "PerspectiveShift", "Influence"]:
                rdf_type = getattr(YOUTH, col_name)
                content_uri = URIRef(YOUTH[f"{col_name}_{index + 1}"])
                g.add((content_uri, RDF.type, rdf_type))
                g.add((content_uri, YOUTH.hasContent, Literal(value)))

    return g

add_triple(df)

output_path = os.path.join(script_dir, "individuals_graph.ttl")
# Serialize the graph to a Turtle file
with open(output_path, "w", encoding="utf-8") as f:
    f.write(g.serialize(format="turtle"))
