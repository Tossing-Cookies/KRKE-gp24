#Lucrezia

import pandas as pd
import random

# Define the associations between different attributes
associations = {
    "Goths": {
        "FashionStyle": "Dark, Victorian",
        "MusicGenre": "Gothic Rock",
        "Slang": "Goth",
        "Ritual": "Goth Night",
        "Activity": "Listening to Music",
        "Event": "Goth Festival",
        "Value": "Individualism",
        "Media": "Goth Magazine",
        "Location": "London",
        "HistoricalPeriod": "1980s"
    },
    "Punks": {
        "FashionStyle": "Ripped, Leather",
        "MusicGenre": "Punk Rock",
        "Slang": "Punk",
        "Ritual": "Punk Concert",
        "Activity": "Attending Concerts",
        "Event": "Punk Weekender",
        "Value": "Rebellion",
        "Media": "Punk Zine",
        "Location": "New York",
        "HistoricalPeriod": "1970s"
    },
    "Skaters": {
        "FashionStyle": "Casual, Streetwear",
        "MusicGenre": "Skate Punk",
        "Slang": "Skater",
        "Ritual": "Skateboarding",
        "Activity": "Skateboarding",
        "Event": "Skate Park Opening",
        "Value": "Freedom",
        "Media": "Skater Blog",
        "Location": "Los Angeles",
        "HistoricalPeriod": "1990s"
    },
    "Hip-Hop Culture": {
        "FashionStyle": "Baggy, Urban",
        "MusicGenre": "Hip-Hop",
        "Slang": "Dope",
        "Ritual": "Hip-Hop Battle",
        "Activity": "Socializing",
        "Event": "Hip-Hop Summit",
        "Value": "Creativity",
        "Media": "Hip-Hop Documentaries",
        "Location": "Berlin",
        "HistoricalPeriod": "1980s"
    },
    "Emo": {
        "FashionStyle": "Black, Minimalist",
        "MusicGenre": "Emo Rock",
        "Slang": "Emo",
        "Ritual": "Emo Night",
        "Activity": "Listening to Music",
        "Event": "Emo Festival",
        "Value": "Emotion",
        "Media": "Emo Vlogs",
        "Location": "Tokyo",
        "HistoricalPeriod": "2000s"
    },
    "Ravers": {
        "FashionStyle": "Bright, Neon",
        "MusicGenre": "Electronic",
        "Slang": "Rave On",
        "Ritual": "Rave Party",
        "Activity": "Dancing",
        "Event": "Rave Extravaganza",
        "Value": "Eclecticism",
        "Media": "Rave Radio",
        "Location": "Paris",
        "HistoricalPeriod": "1990s"
    },
    "Hipsters": {
        "FashionStyle": "Vintage, Indie",
        "MusicGenre": "Indie Rock",
        "Slang": "Hipster",
        "Ritual": "Vintage Fair",
        "Activity": "Fashion Shows",
        "Event": "Hipster Art Walk",
        "Value": "Authenticity",
        "Media": "Hipster Podcasts",
        "Location": "San Francisco",
        "HistoricalPeriod": "2010s"
    },
    "Rockers": {
        "FashionStyle": "Classic Rock",
        "MusicGenre": "Classic Rock",
        "Slang": "Rock On",
        "Ritual": "Participating in Rallies",
        "Activity": "Attending Concerts",
        "Event": "Rock Parade",
        "Value": "Self-Expression",
        "Media": "Rock Biographies",
        "Location": "Austin",
        "HistoricalPeriod": "1970s"
    },
    "Gamers": {
        "FashionStyle": "Graphic Tees",
        "MusicGenre": "Electronic",
        "Slang": "GG",
        "Ritual": "Gaming Marathon",
        "Activity": "Gaming",
        "Event": "Gaming Convention",
        "Value": "Innovation",
        "Media": "Gaming Streams",
        "Location": "Chicago",
        "HistoricalPeriod": "2000s"
    },
    "Mods": {
        "FashionStyle": "Mod Suits",
        "MusicGenre": "Mod Revival",
        "Slang": "Mods",
        "Ritual": "Mod Rally",
        "Activity": "Participating in Rallies",
        "Event": "Mod Week",
        "Value": "Tradition",
        "Media": "Mod TV Shows",
        "Location": "Manchester",
        "HistoricalPeriod": "1960s"
    }
}

# Generate sample data
def generate_data(num_entries):
    data = []
    for i in range(num_entries):
        person_id = f"Person_{i + 1}"
        subculture = random.choice(list(associations.keys()))
        attributes = associations[subculture]
        
        data.append({
            "Person": person_id,
            "YouthSubculture": subculture,
            "FashionStyle": attributes["FashionStyle"],
            "MusicGenre": attributes["MusicGenre"],
            "Slang": attributes["Slang"],
            "Ritual": attributes["Ritual"],
            "Activity": attributes["Activity"],
            "Event": attributes["Event"],
            "Value": attributes["Value"],
            "Media": attributes["Media"],
            "Location": attributes["Location"],
            "HistoricalPeriod": attributes["HistoricalPeriod"]
        })
    
    df = pd.DataFrame(data)
    # Ensure 'Person' is the first column
    df = df[['Person', 'YouthSubculture', 'FashionStyle', 'MusicGenre', 'Slang', 'Ritual', 'Activity', 'Event', 'Value', 'Media', 'Location', 'HistoricalPeriod']]
    return df

# Generate the dataset with at least 100 entries
df = generate_data(100)

# Save the dataset to a CSV file
df.to_csv('dataset_lu.csv', index=False)
