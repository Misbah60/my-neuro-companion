import random
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# This variable stays outside the function so the AI "remembers" 
# even if you run the cell multiple times.
last_suggested_url = None

def smart_memory_companion():
    global last_suggested_url
    
    print("\n" + "═"*45)
    print("🧠 NEURO-COMPANION: ANTI-REPETITION SYSTEM")
    print("═"*45)
    
    user_text = input("I'm listening. How are you feeling? ")
    score = SentimentIntensityAnalyzer().polarity_scores(user_text)['compound']
    
    library = [
        {"vibe": "Rain & Thunderstorm", "url": "https://www.youtube.com/watch?v=lFcSrYw-ARY"},
        {"vibe": "Peaceful Forest Ambience", "url": "https://www.youtube.com/watch?v=5qap5aO4i9A"},
        {"vibe": "Deep Healing Meditation", "url": "https://www.youtube.com/watch?v=DWcLMWal874"},
        {"vibe": "Calming Piano Music", "url": "https://www.youtube.com/watch?v=W-fFHeTX70Q"},
        {"vibe": "Ocean Waves for Anxiety", "url": "https://www.youtube.com/watch?v=mXzstU76f0U"},
        {"vibe": "Lo-fi Jazz Beats", "url": "https://www.youtube.com/watch?v=4xDzrJKXOOY"},
        {"vibe": "Zen Garden Sounds", "url": "https://www.youtube.com/watch?v=662S4h6O-s8"},
        {"vibe": "Binaural Beats for Focus", "url": "https://www.youtube.com/watch?v=AImuCtIokl0"},
        {"vibe": "Soft Guitar Relaxation", "url": "https://www.youtube.com/watch?v=tck7E11SdR8"},
        {"vibe": "528Hz Miracle Tone", "url": "https://www.youtube.com/watch?v=cyEdZ23Cp1E"},
        {"vibe": "Gentle Nature Streams", "url": "https://www.youtube.com/watch?v=RnRZ_DXipgo"},
        {"vibe": "Nighttime Crickets", "url": "https://www.youtube.com/watch?v=aIIEI33EUqI"}
    ]

    if score < -0.1:
        # THE LOGIC: Keep picking until the new choice != the last choice
        choice = random.choice(library)
        while choice['url'] == last_suggested_url:
            choice = random.choice(library)
        
        # Update memory for the next time the script runs
        last_suggested_url = choice['url']
        
        print(f"\n[AI]: I've detected a low mood. I've selected some '{choice['vibe']}' for you.")
        print(f"👉 CLICK TO OPEN (Unique Link): {choice['url']}")
    else:
        print("\n[AI]: Your mood seems stable! I'm here if you need a reset later.")

# Run the model
smart_memory_companion()
