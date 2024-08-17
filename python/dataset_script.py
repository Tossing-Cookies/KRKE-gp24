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
        "ExpressionMedia": "Goth Magazines",
        "MainstreamMedia": "Documentaries, News Coverage",
        "Location": "London",
        "HistoricalPeriod": "1980s",
        "HistoricalPeriodContext": "Rise of goth subculture in post-punk era",
        "ExternalPerspective": "Seen as dark and mysterious",
        "InternalPerspective": "Emphasize individual expression and aesthetics",
        "PerspectiveInfluence": "Media portrayals of dark aesthetics",
        "PerspectiveChange": "Shift from misunderstood to celebrated for its style",
        "Stereotype": "Depressed and brooding",
        "DominantCulture": "Post-punk and alternative fashion",
        "StereotypeTrigger": "Media portrayal of goths as morose and detached",
        "SubGroups": {}
    },
    "Punks": {
        "FashionStyle": "Ripped, Leather",
        "MusicGenre": "Punk Rock",
        "Slang": "Punk",
        "Ritual": "Punk Concert",
        "Activity": "Attending Concerts",
        "Event": "Punk Weekender",
        "Value": "Rebellion",
        "ExpressionMedia": "Punk Zines",
        "MainstreamMedia": "Music Documentaries, News Articles",
        "Location": "New York",
        "HistoricalPeriod": "1970s",
        "HistoricalPeriodContext": "Origins in political and social rebellion",
        "ExternalPerspective": "Seen as rebellious and anti-establishment",
        "InternalPerspective": "Pride in challenging norms",
        "PerspectiveInfluence": "Cultural rebellion and anti-authoritarianism",
        "PerspectiveChange": "From fringe to influential in mainstream fashion",
        "Stereotype": "Troublemakers and anti-social",
        "DominantCulture": "DIY ethic and punk music",
        "StereotypeTrigger": "Media portrayal of punk riots and anarchism",
        "SubGroups": {
            "Hardcore Punks": {
                "DominantCulture": "Aggressive punk and DIY ethos",
                "HistoricalPeriodContext": "Focus on hardcore punk's rise in the early 80s",
                "Value": "Intensity, Activism",
                "StereotypeTrigger": "Media portrayal of hardcore punk as violent"
            },
            "Pop Punks": {
                "DominantCulture": "Melodic punk and mainstream crossover",
                "HistoricalPeriodContext": "Focus on pop punk's commercial success in the 90s",
                "Value": "Catchiness, Youth Appeal",
                "StereotypeTrigger": "Media portrayal of pop punk as mainstream and commercial"
            }
        }
    },
    "Skaters": {
        "FashionStyle": "Casual, Baggy",
        "MusicGenre": "Punk Rock, Hip-Hop",
        "Slang": "Skate",
        "Ritual": "Skate Sessions",
        "Activity": "Skateboarding",
        "Event": "Skate Competitions",
        "Value": "Freedom and creativity",
        "ExpressionMedia": "Skateboarding Magazines, Videos",
        "MainstreamMedia": "Sports Channels, Lifestyle TV Shows",
        "Location": "California",
        "HistoricalPeriod": "1990s",
        "HistoricalPeriodContext": "Growth of extreme sports and skate culture",
        "ExternalPerspective": "Seen as laid-back and rebellious",
        "InternalPerspective": "Focus on skill and personal style",
        "PerspectiveInfluence": "Influence of extreme sports culture",
        "PerspectiveChange": "From niche hobby to mainstream sport",
        "Stereotype": "Risk-taking and anti-establishment",
        "DominantCulture": "Extreme sports and urban youth culture",
        "StereotypeTrigger": "Media portrayal of skater lifestyle as rebellious",
        "SubGroups": {
            "Street Skaters": {
                "DominantCulture": "Street culture and urban skateboarding",
                "HistoricalPeriodContext": "Focus on street skating's rise in the 90s",
                "Value": "Creativity, Urban Exploration",
                "StereotypeTrigger": "Media portrayal of street skaters as troublemakers"
            },
            "Vert Skaters": {
                "DominantCulture": "Vert skating and competitive sports",
                "HistoricalPeriodContext": "Focus on vert skating's prominence in the 80s",
                "Value": "Skill, Competition",
                "StereotypeTrigger": "Media portrayal of vert skaters as elite athletes"
            }
        }
    },
    "Emo": {
        "FashionStyle": "Dark, Skinny Jeans",
        "MusicGenre": "Emo",
        "Slang": "Emo",
        "Ritual": "Emo Nights",
        "Activity": "Listening to Emo Music",
        "Event": "Emo Concerts",
        "Value": "Emotional expression",
        "ExpressionMedia": "Emo Blogs, Music Videos",
        "MainstreamMedia": "Music Channels, Magazines",
        "Location": "Chicago",
        "HistoricalPeriod": "2000s",
        "HistoricalPeriodContext": "Emergence from post-hardcore and punk influences",
        "ExternalPerspective": "Seen as overly emotional and introverted",
        "InternalPerspective": "Focus on expressing deep emotions",
        "PerspectiveInfluence": "Music and personal experiences",
        "PerspectiveChange": "Evolving from niche to influential in alternative music",
        "Stereotype": "Melancholic and introverted",
        "DominantCulture": "Alternative rock and emotional music",
        "StereotypeTrigger": "Media portrayal of emo culture as melodramatic",
        "SubGroups": {
            "Screamo": {
                "DominantCulture": "Intense and aggressive emo music",
                "HistoricalPeriodContext": "Focus on screamo's rise in the early 2000s",
                "Value": "Intensity, Emotional Expression",
                "StereotypeTrigger": "Media portrayal of screamo as chaotic"
            },
            "Post-Emo": {
                "DominantCulture": "Evolution of emo into more mainstream genres",
                "HistoricalPeriodContext": "Focus on emo's transition to pop-punk",
                "Value": "Adaptability, Emotional Honesty",
                "StereotypeTrigger": "Media portrayal of post-emo as sellouts"
            }
        }
    },
    "Ravers": {
        "FashionStyle": "Bright, Neon",
        "MusicGenre": "Electronic Dance Music",
        "Slang": "Rave",
        "Ritual": "Rave Parties",
        "Activity": "Dancing",
        "Event": "Rave Festivals",
        "Value": "Euphoria and community",
        "ExpressionMedia": "Rave Videos, EDM Blogs",
        "MainstreamMedia": "Music Channels, Event Coverage",
        "Location": "Berlin",
        "HistoricalPeriod": "1990s",
        "HistoricalPeriodContext": "Rise of electronic dance music and rave culture",
        "ExternalPerspective": "Seen as hedonistic and wild",
        "InternalPerspective": "Emphasis on music and dance experience",
        "PerspectiveInfluence": "Electronic music and drug culture",
        "PerspectiveChange": "From underground to mainstream popularity",
        "Stereotype": "Party-goers and drug users",
        "DominantCulture": "Electronic dance music and festival culture",
        "StereotypeTrigger": "Media portrayal of rave culture and drug use",
        "SubGroups": {
            "Techno Enthusiasts": {
                "DominantCulture": "Techno music and dance culture",
                "HistoricalPeriodContext": "Focus on techno's growth in the 90s",
                "Value": "Musical Innovation, Dance",
                "StereotypeTrigger": "Media portrayal of techno music and festival scenes"
            },
            "Trance Fans": {
                "DominantCulture": "Trance music and its effects",
                "HistoricalPeriodContext": "Focus on trance's evolution and impact",
                "Value": "Euphoric Experience, Music",
                "StereotypeTrigger": "Media portrayal of trance music as escapist"
            }
        }
    },
    "Hipsters": {
        "FashionStyle": "Vintage, Indie, Artisan",
        "MusicGenre": "Indie Rock, Alternative",
        "Slang": "Hipster, Indie",
        "Ritual": "Coffee Shop Hangouts, Art Shows",
        "Activity": "Exploring Vintage Shops, Indie Music",
        "Event": "Art Exhibits, Indie Music Festivals",
        "Value": "Authenticity, Creativity, Individualism",
        "ExpressionMedia": "Indie Magazines, Blogs",
        "MainstreamMedia": "Lifestyle Magazines, Documentaries",
        "Location": "Brooklyn",
        "HistoricalPeriod": "2000s",
        "HistoricalPeriodContext": "Rise of indie culture and alternative lifestyle",
        "ExternalPerspective": "Seen as trend-followers and elitist",
        "InternalPerspective": "Focus on being unique and non-mainstream",
        "PerspectiveInfluence": "Urban culture and social media",
        "PerspectiveChange": "From niche to influential in fashion and culture",
        "Stereotype": "Pretentious and overly concerned with trends",
        "DominantCulture": "Indie music and alternative fashion",
        "StereotypeTrigger": "Media portrayal of hipsters as elitist trendsetters",
        "SubGroups": {
            "Urban Explorers": {
                "DominantCulture": "Urban exploration and street art",
                "HistoricalPeriodContext": "Focus on the urban exploration trend of the 2000s",
                "Value": "Adventure, Creativity",
                "StereotypeTrigger": "Media portrayal of urban explorers as pretentious"
            },
            "Vintage Enthusiasts": {
                "DominantCulture": "Vintage fashion and retro lifestyle",
                "HistoricalPeriodContext": "Focus on the rise of vintage trends in the 2000s",
                "Value": "Nostalgia, Style",
                "StereotypeTrigger": "Media portrayal of vintage enthusiasts as superficial"
            }
        }
    },
    "Rockers": {
        "FashionStyle": "Leather, Denim",
        "MusicGenre": "Rock",
        "Slang": "Rocker",
        "Ritual": "Rock Concerts",
        "Activity": "Playing Guitar",
        "Event": "Rock Festivals",
        "Value": "Passion, Rebellion",
        "ExpressionMedia": "Rock Magazines, Albums",
        "MainstreamMedia": "Music Channels, Biographies",
        "Location": "Los Angeles",
        "HistoricalPeriod": "1960s-1980s",
        "HistoricalPeriodContext": "Era of classic rock and roll and its evolution",
        "ExternalPerspective": "Seen as rebellious and energetic",
        "InternalPerspective": "Emphasis on musical talent and passion",
        "PerspectiveInfluence": "Rock music history and legends",
        "PerspectiveChange": "From rebellious youth culture to mainstream icons",
        "Stereotype": "Loud and rebellious",
        "DominantCulture": "Classic rock and roll",
        "StereotypeTrigger": "Media portrayal of rockers as wild and unruly",
        "SubGroups": {
            "Metalheads": {
                "DominantCulture": "Heavy metal music and subculture",
                "HistoricalPeriodContext": "Focus on heavy metal's rise in the 70s and 80s",
                "Value": "Intensity, Musical Complexity",
                "StereotypeTrigger": "Media portrayal of metalheads as extreme and aggressive"
            },
            "Glam Rockers": {
                "DominantCulture": "Glam rock and theatrical performance",
                "HistoricalPeriodContext": "Focus on glam rock's prominence in the 70s",
                "Value": "Theatricality, Style",
                "StereotypeTrigger": "Media portrayal of glam rockers as extravagant"
            }
        }
    },
    "Gamers": {
        "FashionStyle": "Casual, Gaming Merchandise",
        "MusicGenre": "Varies",
        "Slang": "Gamer",
        "Ritual": "Gaming Sessions",
        "Activity": "Playing Video Games",
        "Event": "Gaming Conventions",
        "Value": "Skill and immersion",
        "ExpressionMedia": "Gaming Magazines, Online Forums",
        "MainstreamMedia": "Gaming News, Reviews",
        "Location": "Global",
        "HistoricalPeriod": "2000s-present",
        "HistoricalPeriodContext": "Growth of online gaming and eSports",
        "ExternalPerspective": "Seen as socially isolated",
        "InternalPerspective": "Focus on skill and game strategy",
        "PerspectiveInfluence": "Gaming culture and technology",
        "PerspectiveChange": "From niche hobby to mainstream entertainment",
        "Stereotype": "Introverted and obsessive",
        "DominantCulture": "Video gaming and technology",
        "StereotypeTrigger": "Media portrayal of gamers as antisocial",
        "SubGroups": {
            "eSports Players": {
                "DominantCulture": "Competitive gaming and professional leagues",
                "HistoricalPeriodContext": "Focus on the rise of eSports in the 2010s",
                "Value": "Competition, Skill",
                "StereotypeTrigger": "Media portrayal of eSports players as excessively competitive"
            },
            "Casual Gamers": {
                "DominantCulture": "Casual gaming and social play",
                "HistoricalPeriodContext": "Focus on casual gaming's growth in the 2000s",
                "Value": "Relaxation, Fun",
                "StereotypeTrigger": "Media portrayal of casual gamers as unserious"
            }
        }
    },
    "Mods": {
        "FashionStyle": "Sharp Suits, Scooter Culture",
        "MusicGenre": "Soul, R&B",
        "Slang": "Mod",
        "Ritual": "Scooter Rallies",
        "Activity": "Riding Scooters",
        "Event": "Mod Rallies",
        "Value": "Style and sophistication",
        "ExpressionMedia": "Mod Magazines, Music",
        "MainstreamMedia": "Documentaries, News Features",
        "Location": "London",
        "HistoricalPeriod": "1960s",
        "HistoricalPeriodContext": "Rise of the mod culture post-WWII",
        "ExternalPerspective": "Seen as stylish and sophisticated",
        "InternalPerspective": "Focus on appearance and music taste",
        "PerspectiveInfluence": "British pop culture and music",
        "PerspectiveChange": "From youth subculture to retro revival",
        "Stereotype": "Stylish but elitist",
        "DominantCulture": "British pop culture and fashion",
        "StereotypeTrigger": "Media portrayal of mods as elitist fashionistas",
        "SubGroups": {
            "Scooterists": {
                "DominantCulture": "Scooter culture and mod lifestyle",
                "HistoricalPeriodContext": "Focus on the scooter culture of the 60s",
                "Value": "Style, Mobility",
                "StereotypeTrigger": "Media portrayal of scooterists as superficial"
            },
            "Modernists": {
                "DominantCulture": "Modernist influences in fashion",
                "HistoricalPeriodContext": "Focus on modernist fashion and design",
                "Value": "Elegance, Modernity",
                "StereotypeTrigger": "Media portrayal of modernists as detached"
            }
        }
    },
    "Hip-Hop": {
        "FashionStyle": "Streetwear, Baggy Clothes",
        "MusicGenre": "Hip-Hop",
        "Slang": "Hip-Hop",
        "Ritual": "Freestyle Battles",
        "Activity": "Breakdancing, Rapping",
        "Event": "Hip-Hop Festivals",
        "Value": "Creativity and self-expression",
        "ExpressionMedia": "Hip-Hop Videos, Blogs",
        "MainstreamMedia": "Music Channels, Reality Shows",
        "Location": "New York",
        "HistoricalPeriod": "1970s-present",
        "HistoricalPeriodContext": "Evolution from street culture to global phenomenon",
        "ExternalPerspective": "Seen as urban and expressive",
        "InternalPerspective": "Focus on lyrical skill and dance",
        "PerspectiveInfluence": "Urban environment and social issues",
        "PerspectiveChange": "From street culture to global influence",
        "Stereotype": "Street-smart and aggressive",
        "DominantCulture": "Urban culture and music",
        "StereotypeTrigger": "Media portrayal of hip-hop culture as violent and aggressive",
        "SubGroups": {
            "B-Boys/B-Girls": {
                "DominantCulture": "Breakdancing and street performance",
                "HistoricalPeriodContext": "Focus on breakdancing's origins and growth",
                "Value": "Skill, Creativity",
                "StereotypeTrigger": "Media portrayal of B-boys/B-girls as rebellious"
            },
            "Rappers": {
                "DominantCulture": "Rapping and lyrical prowess",
                "HistoricalPeriodContext": "Focus on the evolution of rap music",
                "Value": "Lyrical Skill, Expression",
                "StereotypeTrigger": "Media portrayal of rappers as aggressive"
            }
        }
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
        subgroups = attributes.get("SubGroups", {})
        if subgroups:
            subgroup_name = list(subgroups.keys())[i % len(subgroups)]
            subgroup_attributes = subgroups[subgroup_name]
            subgroup = subgroup_name
        else:
            subgroup = ""
            subgroup_attributes = {}
        
        # Combine attributes from base subculture and subgroup
        entry_attributes = {**attributes, **subgroup_attributes}
        
        data.append({
            "Person": person_id,
            "YouthSubculture": subculture,
            "FashionStyle": entry_attributes["FashionStyle"],
            "MusicGenre": entry_attributes["MusicGenre"],
            "Slang": entry_attributes["Slang"],
            "Ritual": entry_attributes["Ritual"],
            "Activity": entry_attributes["Activity"],
            "Event": entry_attributes["Event"],
            "Value": entry_attributes["Value"],
            "ExpressionMedia": entry_attributes["ExpressionMedia"],
            "MainstreamMedia": entry_attributes["MainstreamMedia"],
            "Location": entry_attributes["Location"],
            "HistoricalPeriod": entry_attributes["HistoricalPeriod"],
            "HistoricalPeriodContext": entry_attributes["HistoricalPeriodContext"],
            "ExternalPerspective": entry_attributes["ExternalPerspective"],
            "InternalPerspective": entry_attributes["InternalPerspective"],
            "PerspectiveInfluence": entry_attributes["PerspectiveInfluence"],
            "PerspectiveChange": entry_attributes["PerspectiveChange"],
            "Stereotype": entry_attributes["Stereotype"],
            "SubGroups": subgroup,
            "DominantCulture": entry_attributes["DominantCulture"],
            "StereotypeTrigger": entry_attributes["StereotypeTrigger"]
        })
    
    return pd.DataFrame(data)

# Generate the dataset
df = generate_data(20)  # Generate a dataset with 20 entries

# Save the dataset to a CSV file
df.to_csv('youthsubcult_dataset.csv', index=False)
