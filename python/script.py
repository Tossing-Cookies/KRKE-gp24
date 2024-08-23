import pandas as pd

# Define comprehensive associations for each youth subculture
associations = {
    "Goths": {
        "FashionStyle": "Dark, Victorian",
        "MusicGenre": "Gothic Rock, Darkwave",
        "Slang": "Goth",
        "Ritual": "Goth Night, Poetry Readings",
        "Activity": "Listening to Music, Visiting Cemeteries",
        "Event": "Wave-Gotik-Treffen, Goth Festival",
        "Value": "Individualism, Romanticism",
        "ExpressionMedia": "Goth Magazines, Fanzines",
        "MainstreamMedia": "Documentaries, TV Specials",
        "Location": "London, Berlin",
        "HistoricalPeriod": "1980s-present",
        "HistoricalPeriodContext": "Post-punk era with a focus on dark aesthetics and existentialism",
        "ExternalPerspective": "Seen as dark and mysterious, often misunderstood",
        "InternalPerspective": "Emphasize individual expression, aesthetics, and connection with the macabre",
        "PerspectiveInfluence": "Media portrayals of dark aesthetics, post-punk music",
        "PerspectiveChange": "Shift from misunderstood to celebrated for its style",
        "Stereotype": "Depressed and brooding",
        "SubGroups": "Romantic Goths, Cyber Goths",
        "DominantCulture": "Western mainstream culture of the 1980s",
        "StereotypeTrigger": "Media portrayal of Gothic fashion and lifestyle, association with dark themes"
    },
    "Punks": {
        "FashionStyle": "Ripped, Leather, DIY Aesthetic",
        "MusicGenre": "Punk Rock, Hardcore Punk",
        "Slang": "Punk, Anarchy",
        "Ritual": "Punk Concerts, Protests",
        "Activity": "Attending Concerts, Zine Creation",
        "Event": "Punk Weekender, Anti-Nazi Rallies",
        "Value": "Rebellion, Anti-Establishment",
        "ExpressionMedia": "Punk Zines, DIY Record Labels",
        "MainstreamMedia": "News Reports, Documentaries",
        "Location": "New York, London",
        "HistoricalPeriod": "1970s-1980s",
        "HistoricalPeriodContext": "Rise of anti-establishment sentiments, economic hardships",
        "ExternalPerspective": "Seen as rebellious, anti-social, and dangerous",
        "InternalPerspective": "Pride in challenging norms, DIY ethics, community solidarity",
        "PerspectiveInfluence": "Cultural rebellion, anti-authoritarianism, Thatcher-era policies",
        "PerspectiveChange": "From fringe to influential in mainstream fashion and music",
        "Stereotype": "Troublemakers and anti-social",
        "SubGroups": "Riot grrrl, Skinheads",
        "DominantCulture": "Conservative post-war Western society",
        "StereotypeTrigger": "News reports on punk-related violence, clashes with authorities"
    },
    "Skaters": {
        "FashionStyle": "Casual, Baggy, Streetwear",
        "MusicGenre": "Punk Rock, Hip-Hop",
        "Slang": "Skate, Shred",
        "Ritual": "Skate Sessions, Trick Jams",
        "Activity": "Skateboarding, Filming Skate Videos",
        "Event": "X Games, Local Skate Competitions",
        "Value": "Freedom, Creativity, Risk-taking",
        "ExpressionMedia": "Skateboarding Magazines, DIY Skate Videos",
        "MainstreamMedia": "TV Shows, Skateboarding Movies",
        "Location": "California, Barcelona",
        "HistoricalPeriod": "1980s-present",
        "HistoricalPeriodContext": "Emergence of extreme sports culture, urban expansion",
        "ExternalPerspective": "Seen as laid-back, rebellious, and risk-taking",
        "InternalPerspective": "Focus on skill, personal style, and community",
        "PerspectiveInfluence": "Influence of extreme sports culture, urban environments",
        "PerspectiveChange": "From niche hobby to mainstream sport and culture",
        "Stereotype": "Risk-taking, anti-establishment",
        "SubGroups": "Street Skaters, Vert Skaters",
        "DominantCulture": "Suburban and urban American culture of the 1990s",
        "StereotypeTrigger": "Media portrayal of skateboarding as rebellious, property damage concerns"
    },
    "Emo": {
        "FashionStyle": "Dark, Skinny Jeans, Band T-Shirts",
        "MusicGenre": "Emo, Post-Hardcore",
        "Slang": "Emo, Screamo",
        "Ritual": "Emo Nights, Blogging",
        "Activity": "Listening to Emo Music, Writing Poetry",
        "Event": "Emo Concerts, Warped Tour",
        "Value": "Emotional expression, Individualism",
        "ExpressionMedia": "Emo Blogs, MySpace Pages",
        "MainstreamMedia": "Music Videos, Teen Magazines",
        "Location": "Chicago, New Jersey",
        "HistoricalPeriod": "2000s",
        "HistoricalPeriodContext": "Post-9/11 era with a focus on emotional depth and alternative culture",
        "ExternalPerspective": "Seen as overly emotional, introverted, and self-destructive",
        "InternalPerspective": "Focus on expressing deep emotions, connection with music and peers",
        "PerspectiveInfluence": "Music, personal experiences, youth culture",
        "PerspectiveChange": "Evolving from niche to influential in alternative music scenes",
        "Stereotype": "Melancholic, introverted, self-harming",
        "SubGroups": "Scene Kids, Screamo Fans",
        "DominantCulture": "American youth culture in the digital age",
        "StereotypeTrigger": "Media focus on self-harm and dark lyrics, parental concerns"
    },
    "Ravers": {
        "FashionStyle": "Bright, Neon, Kandi Bracelets",
        "MusicGenre": "Electronic Dance Music, Trance",
        "Slang": "Rave, PLUR",
        "Ritual": "Rave Parties, DJ Worship",
        "Activity": "Dancing, Mixing Music",
        "Event": "Rave Festivals, Underground Parties",
        "Value": "Euphoria, Community, PLUR (Peace, Love, Unity, Respect)",
        "ExpressionMedia": "Rave Videos, DJ Mix Tapes",
        "MainstreamMedia": "News Reports, Music Festivals",
        "Location": "Berlin, Bologna",
        "HistoricalPeriod": "1990s-present",
        "HistoricalPeriodContext": "Rise of electronic music, counterculture movements",
        "ExternalPerspective": "Seen as hedonistic, wild, and drug-influenced",
        "InternalPerspective": "Emphasis on music, dance, and collective euphoria",
        "PerspectiveInfluence": "Electronic music, drug culture, urban nightlife",
        "PerspectiveChange": "From underground to mainstream popularity, EDM explosion",
        "Stereotype": "Party-goers, drug users, hedonistic",
        "SubGroups": "Candy Ravers, Techno Heads",
        "DominantCulture": "European and American nightlife culture",
        "StereotypeTrigger": "Media coverage of drug overdoses at raves, police crackdowns"
    },
    "Hipsters": {
        "FashionStyle": "Vintage, Indie, Retro Glasses",
        "MusicGenre": "Indie Rock, Alternative",
        "Slang": "Hipster, Indie",
        "Ritual": "Coffee Shop Hangs, Vinyl Collecting",
        "Activity": "Exploring New Trends, Attending Art Shows",
        "Event": "Art Exhibitions, Indie Film Festivals",
        "Value": "Authenticity, Uniqueness, Irony",
        "ExpressionMedia": "Hipster Blogs, Indie Zines",
        "MainstreamMedia": "Lifestyle Magazines, Fashion Shows",
        "Location": "Brooklyn, Portland",
        "HistoricalPeriod": "2000s-present",
        "HistoricalPeriodContext": "Post-modern reaction to mainstream consumerism, gentrification",
        "ExternalPerspective": "Seen as trend-followers, elitist, and pretentious",
        "InternalPerspective": "Focus on being unique, non-mainstream, and culturally aware",
        "PerspectiveInfluence": "Urban culture, social media, indie movements",
        "PerspectiveChange": "From niche to influential in fashion, culture, and lifestyle",
        "Stereotype": "Pretentious, overly concerned with trends, gentrifiers",
        "SubGroups": "Normcore, Lumbersexuals",
        "DominantCulture": "Urban, gentrified neighborhoods in major cities",
        "StereotypeTrigger": "Media depiction of gentrification, trend commodification"
    },
    "Rockers": {
        "FashionStyle": "Leather, Denim, Band Patches",
        "MusicGenre": "Classic Rock, Heavy Metal",
        "Slang": "Rocker, Headbanger",
        "Ritual": "Rock Concerts, Air Guitar Competitions",
        "Activity": "Playing Guitar, Collecting Vinyl",
        "Event": "Rock Festivals, Battle of the Bands",
        "Value": "Passion, Rebellion, Musical Talent",
        "ExpressionMedia": "Rock Magazines, Music Documentaries",
        "MainstreamMedia": "Music Channels, Biopics",
        "Location": "Los Angeles, London",
        "HistoricalPeriod": "1950s-present",
        "HistoricalPeriodContext": "Post-war era with a focus on rebellion and rock 'n' roll",
        "ExternalPerspective": "Seen as loud, rebellious, and wild",
        "InternalPerspective": "Deep connection to music, culture of rebellion and expression",
        "PerspectiveInfluence": "Rock music, counterculture, anti-establishment sentiments",
        "PerspectiveChange": "From fringe to the defining sound of youth rebellion",
        "Stereotype": "Loud, rebellious, party-goers",
        "SubGroups": "Metalheads, Classic Rock Enthusiasts",
        "DominantCulture": "Post-war Western youth culture",
        "StereotypeTrigger": "Media portrayal of rock concerts as chaotic, drug-fueled"
    },
    "Gamers": {
        "FashionStyle": "Casual, Graphic Tees, Hoodies",
        "MusicGenre": "Chiptune, Video Game Soundtracks",
        "Slang": "Gamer, Noob, Pwned",
        "Ritual": "Gaming Marathons, Streaming",
        "Activity": "Playing Video Games, Modding",
        "Event": "E3, Gaming Conventions, LAN Parties",
        "Value": "Competition, Strategy, Community",
        "ExpressionMedia": "Game Reviews, Twitch Streams",
        "MainstreamMedia": "Gaming Magazines, YouTube Channels",
        "Location": "Online Communities, Silicon Valley",
        "HistoricalPeriod": "1980s-present",
        "HistoricalPeriodContext": "Digital revolution, rise of personal computing",
        "ExternalPerspective": "Seen as socially awkward, overly competitive, and obsessed",
        "InternalPerspective": "Focus on skill, community, and innovation in gaming",
        "PerspectiveInfluence": "Digital culture, tech innovation, online communities",
        "PerspectiveChange": "From niche hobby to global, multi-billion dollar industry",
        "Stereotype": "Socially awkward, obsessed, isolated",
        "SubGroups": "PC Gamers, Console Gamers, eSports Players",
        "DominantCulture": "Digital and tech-savvy culture",
        "StereotypeTrigger": "Media reports on gaming addiction, violence in video games"
    },
    "Mods": {
        "FashionStyle": "Tailored Suits, Parkas, Vespa Scooters",
        "MusicGenre": "Mod Rock, Northern Soul",
        "Slang": "Mod, Ace Face",
        "Ritual": "Scooter Rallies, Club Nights",
        "Activity": "Dancing, Vespa Riding",
        "Event": "Mod Weekender, Soul All-Nighters",
        "Value": "Style, Sophistication, Music",
        "ExpressionMedia": "Mod Magazines, Fanzines",
        "MainstreamMedia": "Films, Documentaries",
        "Location": "London, Brighton",
        "HistoricalPeriod": "1960s-1980s",
        "HistoricalPeriodContext": "Post-war Britain with a focus on consumerism and youth culture",
        "ExternalPerspective": "Seen as stylish, rebellious, and elitist",
        "InternalPerspective": "Emphasis on fashion, music, and modernist lifestyle",
        "PerspectiveInfluence": "British working-class culture, consumerism, American soul music",
        "PerspectiveChange": "From youth rebellion to nostalgic revival",
        "Stereotype": "Elitist, fashion-obsessed, violent clashes with Rockers",
        "SubGroups": "Modernists, Scooter Boys",
        "DominantCulture": "Post-war British youth culture",
        "StereotypeTrigger": "Media coverage of violent clashes with Rockers, focus on fashion obsession"
    },
    "Hip-Hop": {
        "FashionStyle": "Streetwear, Baggy Pants, Gold Chains",
        "MusicGenre": "Hip-Hop, Rap",
        "Slang": "Hip-Hop, MC, DJ",
        "Ritual": "Rap Battles, DJing",
        "Activity": "Breakdancing, Graffiti Art",
        "Event": "Hip-Hop Shows, Block Parties",
        "Value": "Expression, Street Credibility, Resistance",
        "ExpressionMedia": "Mixtapes, Rap Videos",
        "MainstreamMedia": "Music Channels, Urban Radio Stations",
        "Location": "New York, Los Angeles",
        "HistoricalPeriod": "1970s-present",
        "HistoricalPeriodContext": "Urban decay, civil rights movements, cultural expression",
        "ExternalPerspective": "Seen as rebellious, dangerous, and influential",
        "InternalPerspective": "Focus on creativity, cultural expression, and social commentary",
        "PerspectiveInfluence": "Urban culture, racial tensions, media representation",
        "PerspectiveChange": "From underground to dominant force in global pop culture",
        "Stereotype": "Violent, materialistic, misogynistic",
        "SubGroups": "Old School, Gangsta Rap, Conscious Rap",
        "DominantCulture": "Urban American culture, African-American communities",
        "StereotypeTrigger": "Media portrayal of gang violence, controversial lyrics"
    }
}

# Generate sample data
def generate_data(num_entries):
    data = []
    subcultures = list(associations.keys())
    
    # Generate 10 entries without subgroups
    for i in range(10):
        person_id = f"Person_{i + 1}"
        subculture = subcultures[i]
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
            "ExpressionMedia": attributes["ExpressionMedia"],
            "MainstreamMedia": attributes["MainstreamMedia"],
            "Location": attributes["Location"],
            "HistoricalPeriod": attributes["HistoricalPeriod"],
            "HistoricalPeriodContext": attributes["HistoricalPeriodContext"],
            "ExternalPerspective": attributes["ExternalPerspective"],
            "InternalPerspective": attributes["InternalPerspective"],
            "PerspectiveInfluence": attributes["PerspectiveInfluence"],
            "PerspectiveChange": attributes["PerspectiveChange"],
            "Stereotype": attributes["Stereotype"],
            "SubGroups": "",  # Empty for basic entries
            "DominantCulture": attributes["DominantCulture"],
            "StereotypeTrigger": attributes["StereotypeTrigger"]
        })
    
    # Generate 10 entries with subgroups
    for i in range(10):
        person_id = f"Person_{i + 11}"
        subculture = subcultures[i]
        attributes = associations[subculture]
        
        # Randomly select a subgroup if available
        subgroups = attributes["SubGroups"].split(", ")
        subgroup = subgroups[i % len(subgroups)] if subgroups else ""
        
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
            "ExpressionMedia": attributes["ExpressionMedia"],
            "MainstreamMedia": attributes["MainstreamMedia"],
            "Location": attributes["Location"],
            "HistoricalPeriod": attributes["HistoricalPeriod"],
            "HistoricalPeriodContext": attributes["HistoricalPeriodContext"],
            "ExternalPerspective": attributes["ExternalPerspective"],
            "InternalPerspective": attributes["InternalPerspective"],
            "PerspectiveInfluence": attributes["PerspectiveInfluence"],
            "PerspectiveChange": attributes["PerspectiveChange"],
            "Stereotype": attributes["Stereotype"],
            "SubGroups": subgroup,
            "DominantCulture": attributes["DominantCulture"],
            "StereotypeTrigger": attributes["StereotypeTrigger"]
        })
    
    return pd.DataFrame(data)

# Generate the dataset
df = generate_data(20)  # Generate a dataset with 20 entries

# Save the dataset to a CSV file
df.to_csv('1youthsubcult_dataset_20_entries.csv', index=False)

print("Dataset created and saved as 'youthsubcult_dataset_20_entries.csv'")
