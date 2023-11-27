import streamlit as st
from helper_functions import get_youtube_transcript

st.title("Video Notes")
st.divider()

col1, col2 = st.columns([0.3, 0.6])

with col1:
    st.subheader("Paste in URL to YouTube Video:")
    url = st.text_input('YouTube URL')

with col2:
    transcript = get_youtube_transcript(url)
    with st.expander("Retrieved Transcript:"):
        
        tr = f"""{transcript}"""
        st.write(tr)