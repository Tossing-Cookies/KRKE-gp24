import random
import csv

# Define the subcultures with specific characteristics
youth_subcultures = [
    {
        "name": "Goths",
        "valid_perspectives": ["Dark and mysterious"],
        "location": "Bologna",
        "valid_stereotypes": ["Morbid", "Mysterious"]
    },
    {
        "name": "Hipsters",
        "valid_perspectives": ["Elitist"],
        "location": "New York",
        "valid_stereotypes": ["Elitist", "Trendy"]
    },
    {
        "name": "Emos",
        "valid_perspectives": ["Emotional and expressive"],
        "location": "Los Angeles",
        "valid_stereotypes": ["Emotional", "Expressive"]
    }
]

external_perspectives = [
    "Dark and mysterious",
    "Elitist",
    "Emotional and expressive"
]

internal_perspectives = [
    "Introspective and aesthetic",
    "Trendy and innovative",
    "Expressive and emotional"
]

persons = [
    "Alice Smith",
    "Bob Johnson",
    "Caterina Rossi"
]

activities = [
    "Listening to music",
    "Attending concerts",
    "Creating art"
]

media_types = [
    "Social media",
    "TV shows",
    "Online articles"
]

stereotypes = [
    "Morbid",
    "Elitist",
    "Overly emotional",
    "Mysterious",
    "Trendy",
    "Expressive"
]

def generate_data(num_records):
    data = []
    for _ in range(num_records):
        subculture = random.choice(youth_subcultures)
        person = random.choice(persons)
        external_perspective = random.choice(subculture["valid_perspectives"])
        internal_perspective = random.choice(internal_perspectives)
        activity = random.choice(activities)
        media = random.choice(media_types)
        stereotype = random.choice(subculture["valid_stereotypes"])

        # Validate external perspective
        if subculture["name"] == "Goths" and external_perspective != "Dark and mysterious":
            continue
        if subculture["name"] == "Hipsters" and external_perspective != "Elitist":
            continue
        if subculture["name"] == "Emos" and external_perspective != "Emotional and expressive":
            continue
        
        # Validate stereotype
        if stereotype not in subculture["valid_stereotypes"]:
            continue
        
        # Collect valid data entry
        data.append({
            "YouthSubculture": subculture["name"],
            "ExternalPerspective": external_perspective,
            "InternalPerspective": internal_perspective,
            "Person": person,
            "Activity": activity,
            "Location": subculture["location"],  # Ensure location matches subculture
            "Media": media,
            "Stereotype": stereotype,
        })
    
    return data

# Generate a sample dataset of 100 records
synthetic_data = generate_data(100)

# Write to CSV
with open("dataset.csv", "w", newline='') as csvfile:
    fieldnames = ["YouthSubculture", "ExternalPerspective", "InternalPerspective", "Person", "Activity", "Location", "Media", "Stereotype"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for record in synthetic_data:
        writer.writerow(record)
