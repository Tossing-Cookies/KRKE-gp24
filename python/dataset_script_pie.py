# Pietro

import csv
import json
import random

# Define the structure of your ontology
youth_subcultures = [
    {
        "name": "Goths",
        "description": "Dark, mysterious subculture",
        "valid_perspectives": ["Dark and mysterious"],
        "location": "Bologna"
    },
    {
        "name": "Hipsters",
        "description": "Trendy, alternative style",
        "valid_perspectives": ["Elitist"],
        "location": "New York"
    },
    {
        "name": "Emos",
        "description": "Emotional, expressive",
        "valid_perspectives": ["Emotional and expressive"],
        "location": "Los Angeles"
    }
]

external_perspectives = [
    "Dark and mysterious",
    "Elitist",
    "Emotional and expressive",
]

internal_perspectives = [
    "Introspective and aesthetic",
    "Trendsetter",
    "Expressive and emotional",
]

activities = [
    "Attending concerts",
    "Art exhibitions",
    "Poetry reading",
]

media_types = [
    "Social media",
    "TV shows",
    "Online articles"
]

stereotypes = [
    "Morbid",
    "Elitist",
    "Overly emotional"
]

# Generate synthetic data
persons = ["Alice Smith", "Bob Johnson", "Caterina Rossi", "David Brown"]
stereotypes = ["morbid", "elitist", "emotional"]
subcultures = ["Goths", "Hipsters", "Emos"]
locations = ["Bologna", "New York", "Los Angeles"]

# Function to generate data (with validation rules)
def generate_data(num_records):
    data = []
    for _ in range(num_records):
        subculture = random.choice(subcultures)
        person = random.choice(persons)
        external_perspective = random.choice(external_perspectives)
        internal_perspective = random.choice(internal_perspectives)
        activity = random.choice(activities)
        media = random.choice(media_types)
        location = random.choice(locations)
        stereotype = random.choice(stereotypes)

            # Validating perspectives
        if subculture["name"] == "Goths" and external_perspective != "Dark and mysterious":
            continue
        if subculture["name"] == "Hipsters" and external_perspective != "Elitist":
            continue
        if subculture["name"] == "Emos" and external_perspective != "Emotional and expressive":
            continue
        
        data.append({
            "YouthSubculture": subculture["name"],
            "Description": subculture["description"],
            "ExternalPerspective": external_perspective,
            "InternalPerspective": internal_perspective,
            "Person": person,
            "Activity": activity,
            "Location": subculture["location"],  # Ensure location matches subculture
            "Media": media,
            "Stereotype": stereotype,
        })
    
    return data

# Generate 100 records
synthetic_data = generate_data(100)

# Write to CSV
with open("synthetic_data.csv", "w", newline='') as csvfile:
    fieldnames = ["YouthSubculture", "ExternalPerspective", "InternalPerspective", "Person", "Activity", "Location", "Media", "Stereotype"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for record in synthetic_data:
        writer.writerow(record)
