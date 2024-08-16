import pandas as pd

# Define the associations between different attributes, including perspectives and stereotypes
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
        "HistoricalPeriod": "1980s",
        "ExternalPerspective": "Seen as dark and mysterious",
        "InternalPerspective": "Emphasize individual expression and aesthetics",
        "PerspectiveInfluence": "Media portrayals of dark aesthetics",
        "PerspectiveChange": "Shift from misunderstood to celebrated for its style",
        "Stereotype": "Depressed and brooding"
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
        "HistoricalPeriod": "1970s",
        "ExternalPerspective": "Seen as rebellious and anti-establishment",
        "InternalPerspective": "Pride in challenging norms",
        "PerspectiveInfluence": "Cultural rebellion and anti-authoritarianism",
        "PerspectiveChange": "From fringe to influential in mainstream fashion",
        "Stereotype": "Troublemakers and anti-social"
    },
    "Skaters": {
        "FashionStyle": "Casual, Baggy",
        "MusicGenre": "Punk Rock, Hip-Hop",
        "Slang": "Skate",
        "Ritual": "Skate Sessions",
        "Activity": "Skateboarding",
        "Event": "Skate Competitions",
        "Value": "Freedom and creativity",
        "Media": "Skateboarding Magazines",
        "Location": "California",
        "HistoricalPeriod": "1990s",
        "ExternalPerspective": "Seen as laid-back and rebellious",
        "InternalPerspective": "Focus on skill and personal style",
        "PerspectiveInfluence": "Influence of extreme sports culture",
        "PerspectiveChange": "From niche hobby to mainstream sport",
        "Stereotype": "Risk-taking and anti-establishment"
    },
    "Emo": {
        "FashionStyle": "Dark, Skinny Jeans",
        "MusicGenre": "Emo",
        "Slang": "Emo",
        "Ritual": "Emo Nights",
        "Activity": "Listening to Emo Music",
        "Event": "Emo Concerts",
        "Value": "Emotional expression",
        "Media": "Emo Blogs",
        "Location": "Chicago",
        "HistoricalPeriod": "2000s",
        "ExternalPerspective": "Seen as overly emotional and introverted",
        "InternalPerspective": "Focus on expressing deep emotions",
        "PerspectiveInfluence": "Music and personal experiences",
        "PerspectiveChange": "Evolving from niche to influential in alternative music",
        "Stereotype": "Melancholic and introverted"
    },
    "Ravers": {
        "FashionStyle": "Bright, Neon",
        "MusicGenre": "Electronic Dance Music",
        "Slang": "Rave",
        "Ritual": "Rave Parties",
        "Activity": "Dancing",
        "Event": "Rave Festivals",
        "Value": "Euphoria and community",
        "Media": "Rave Videos",
        "Location": "Berlin",
        "HistoricalPeriod": "1990s",
        "ExternalPerspective": "Seen as hedonistic and wild",
        "InternalPerspective": "Emphasis on music and dance experience",
        "PerspectiveInfluence": "Electronic music and drug culture",
        "PerspectiveChange": "From underground to mainstream popularity",
        "Stereotype": "Party-goers and drug users"
    },
    "Hipsters": {
        "FashionStyle": "Vintage, Indie",
        "MusicGenre": "Indie Rock",
        "Slang": "Hipster",
        "Ritual": "Coffee Shop Hangs",
        "Activity": "Exploring New Trends",
        "Event": "Art Exhibitions",
        "Value": "Authenticity and uniqueness",
        "Media": "Hipster Blogs",
        "Location": "Brooklyn",
        "HistoricalPeriod": "2000s",
        "ExternalPerspective": "Seen as trend-followers and elitist",
        "InternalPerspective": "Focus on being unique and non-mainstream",
        "PerspectiveInfluence": "Urban culture and social media",
        "PerspectiveChange": "From niche to influential in fashion and culture",
        "Stereotype": "Pretentious and overly concerned with trends"
    },
    "Rockers": {
        "FashionStyle": "Leather, Denim",
        "MusicGenre": "Rock",
        "Slang": "Rocker",
        "Ritual": "Rock Concerts",
        "Activity": "Playing Guitar",
        "Event": "Rock Festivals",
        "Value": "Passion and rebellion",
        "Media": "Rock Magazines",
        "Location": "Los Angeles",
        "HistoricalPeriod": "1960s-1980s",
        "ExternalPerspective": "Seen as rebellious and energetic",
        "InternalPerspective": "Emphasis on musical talent and passion",
        "PerspectiveInfluence": "Rock music history and legends",
        "PerspectiveChange": "From rebellious youth culture to mainstream icons",
        "Stereotype": "Loud and rebellious"
    },
    "Gamers": {
        "FashionStyle": "Casual, Gaming Merchandise",
        "MusicGenre": "Varies",
        "Slang": "Gamer",
        "Ritual": "Gaming Sessions",
        "Activity": "Playing Video Games",
        "Event": "Gaming Conventions",
        "Value": "Skill and immersion",
        "Media": "Gaming Magazines",
        "Location": "Global",
        "HistoricalPeriod": "2000s-present",
        "ExternalPerspective": "Seen as socially isolated",
        "InternalPerspective": "Focus on skill and game strategy",
        "PerspectiveInfluence": "Gaming culture and technology",
        "PerspectiveChange": "From niche hobby to mainstream entertainment",
        "Stereotype": "Introverted and obsessive"
    },
    "Mods": {
        "FashionStyle": "Sharp Suits, Scooter Culture",
        "MusicGenre": "Soul, R&B",
        "Slang": "Mod",
        "Ritual": "Scooter Rallies",
        "Activity": "Riding Scooters",
        "Event": "Mod Rallies",
        "Value": "Style and sophistication",
        "Media": "Mod Magazines",
        "Location": "London",
        "HistoricalPeriod": "1960s",
        "ExternalPerspective": "Seen as stylish and sophisticated",
        "InternalPerspective": "Focus on appearance and music taste",
        "PerspectiveInfluence": "British pop culture and music",
        "PerspectiveChange": "From youth subculture to retro revival",
        "Stereotype": "Stylish but elitist"
    },
    "Hip-Hop Culture": {
        "FashionStyle": "Streetwear, Baggy Clothes",
        "MusicGenre": "Hip-Hop",
        "Slang": "Hip-Hop",
        "Ritual": "Freestyle Battles",
        "Activity": "Breakdancing, Rapping",
        "Event": "Hip-Hop Festivals",
        "Value": "Creativity and self-expression",
        "Media": "Hip-Hop Videos",
        "Location": "New York",
        "HistoricalPeriod": "1970s-present",
        "ExternalPerspective": "Seen as urban and expressive",
        "InternalPerspective": "Focus on lyrical skill and dance",
        "PerspectiveInfluence": "Urban environment and social issues",
        "PerspectiveChange": "From street culture to global influence",
        "Stereotype": "Street-smart and aggressive"
    }
}

# Generate sample data
def generate_data(num_entries):
    data = []
    subcultures = list(associations.keys())
    for i in range(num_entries):
        person_id = f"Person_{i + 1}"
        subculture = subcultures[i]  # Ensure each subculture is included
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
            "HistoricalPeriod": attributes["HistoricalPeriod"],
            "ExternalPerspective": attributes["ExternalPerspective"],
            "InternalPerspective": attributes["InternalPerspective"],
            "PerspectiveInfluence": attributes["PerspectiveInfluence"],
            "PerspectiveChange": attributes["PerspectiveChange"],
            "Stereotype": attributes["Stereotype"]
        })
    
    return pd.DataFrame(data)

# Generate the dataset with the exact number of entries as subcultures
df = generate_data(len(associations))  # Generate exactly 10 entries

# Save the dataset to a CSV file
df.to_csv('youthsubcult_dataset.csv', index=False)

print("Dataset created and saved as 'youthsubcult_dataset.csv'")
