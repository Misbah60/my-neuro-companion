import streamlit as st
import random
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# 1. SETUP PAGE
st.set_page_config(page_title="Neuro-Companion", page_icon="🧠")
st.title("🧠 NEURO-COMPANION: ANTI-REPETITION SYSTEM")

# 2. SMART MEMORY (Replaces the 'global' variable from Kaggle)
if 'last_suggested_url' not in st.session_state:
    st.session_state.last_suggested_url = None

# 3. USER INTERFACE
user_text = st.text_input("I'm listening. How are you feeling?")

# 4. DATA LIBRARY (Exact same 12 videos from your Kaggle code)
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

# 5. EXECUTE LOGIC
if user_text:
    score = SentimentIntensityAnalyzer().polarity_scores(user_text)['compound']
    
    if score < -0.1:
        # THE LOGIC: Anti-Repetition choice
        choice = random.choice(library)
        while choice['url'] == st.session_state.last_suggested_url:
            choice = random.choice(library)
        
        # Update memory
        st.session_state.last_suggested_url = choice['url']
        
        st.warning(f"I've detected a low mood. I've selected some '{choice['vibe']}' for you.")
        st.video(choice['url']) # This embeds the YouTube video directly!
    else:
        st.success("Your mood seems stable! I'm here if you need a reset later.")
