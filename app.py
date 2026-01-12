import streamlit as st
import random
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize Memory
if 'last_link' not in st.session_state:
    st.session_state.last_link = None

st.title("🧠 AI Neuro-Companion")
st.write("Real-time sentiment intervention based on simulated EEG logic.")

user_input = st.text_input("How are you feeling right now?")

if user_input:
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(user_input)['compound']
    
    # Library of 10+ Videos
    links = [
        "https://www.youtube.com/watch?v=lFcSrYw-ARY", "https://www.youtube.com/watch?v=5qap5aO4i9A",
        "https://www.youtube.com/watch?v=DWcLMWal874", "https://www.youtube.com/watch?v=W-fFHeTX70Q",
        "https://www.youtube.com/watch?v=mXzstU76f0U", "https://www.youtube.com/watch?v=4xDzrJKXOOY",
        "https://www.youtube.com/watch?v=662S4h6O-s8", "https://www.youtube.com/watch?v=AImuCtIokl0",
        "https://www.youtube.com/watch?v=tck7E11SdR8", "https://www.youtube.com/watch?v=cyEdZ23Cp1E"
    ]
    
    if score < -0.1:
        # Prevent repetition
        choice = random.choice(links)
        while choice == st.session_state.last_link:
            choice = random.choice(links)
        st.session_state.last_link = choice
        
        st.warning("Low mood detected. Try this unique relaxation track:")
        st.video(choice)
    else:
        st.success("Your mood seems stable. Keep it up!")
