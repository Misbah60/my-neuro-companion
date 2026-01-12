import streamlit as st
import random
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Set up page title
st.set_page_config(page_title="AI Neuro-Companion", page_icon="🧠")
st.title("🧠 AI Neuro-Companion")
st.write("Real-time sentiment intervention based on simulated EEG logic.")

# Initialize a 'memory' so the same video doesn't show twice
if 'previous_video' not in st.session_state:
    st.session_state.previous_video = ""

# User input box
user_input = st.text_input("How are you feeling right now?")

if user_input:
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(user_input)['compound']
    
    # UPDATED LIBRARY: Verified working links
    links = [
        "https://www.youtube.com/watch?v=cyEdZ23Cp1E", # How to relax tips
        "https://www.youtube.com/watch?v=W-fFHeTX70Q", # Best of Beethoven
        "https://www.youtube.com/watch?v=AImuCtIokl0", # 15 Min Meditation
        "https://www.youtube.com/watch?v=4xDzrJKXOOY", # Synthwave/Lofi Radio
        "https://www.youtube.com/watch?v=inpok4MKVLM", # 528Hz DNA Healing
        "https://www.youtube.com/watch?v=lTRiuFIWV54", # Deep Sleep Music
        "https://www.youtube.com/watch?v=2OEL4P1Rz04", # Nature Sounds
        "https://www.youtube.com/watch?v=6v9u8n_mX3o", # Guided Anxiety Relief
        "https://www.youtube.com/watch?v=DXU3o8YwS8E", # Rain Sounds
        "https://www.youtube.com/watch?v=8p_S9YfU54g"  # Calming Piano
    ]
    
    # LOGIC: If mood is low (score < -0.1)
    if score < -0.1:
        # Pick a video that isn't the same as the last one
        choice = random.choice(links)
        while choice == st.session_state.previous_video:
            choice = random.choice(links)
        
        st.session_state.previous_video = choice # Save to memory
        
        st.warning("Low mood detected. Try this unique relaxation track:")
        
        # Display the video player
        st.video(choice)
        
        # PROVIDE THE DIRECT LINK AS REQUESTED
        st.markdown(f"🔗 [Click here to open the video directly on YouTube]({choice})")
        
    else:
        st.success("Your mood seems stable. Keep up the positive energy!")

# Bottom Section: Explanation of EEG Logic
st.divider()
st.info("Note: This app simulates an EEG intervention. In a clinical setting, a detected 'outlier' in brainwaves would trigger this same video suggestion.")
