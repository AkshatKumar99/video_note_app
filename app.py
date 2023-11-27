import streamlit as st
from helper_functions import get_youtube_transcript

st.title("Video Notes")
st.divider()
st.subheader("Paste in URL to YouTube Video:")

url = st.text_input('YouTube URL')

transcript = get_youtube_transcript(url)

st.write(transcript)