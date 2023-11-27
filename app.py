import streamlit as st
from helper_functions import get_youtube_transcript

st.title("Video Notes")
st.divider()

col1, col2 = st.columns([0.3, 0.6])

with col1:
    st.subheader("Paste in URL to YouTube Video:")
    url = st.text_area("URL:")
    #url = st.text_input('YouTube URL')
    transcript = get_youtube_transcript(url)

with col2:
    video_container = st.container()
    try:
        video_container.video(url)
    except:
        video_container.write('No URL Entered! Enter URL to display video here.')
    with st.expander("Transcript Stats:"):
        tr = f"""{transcript}"""
        #st.write(tr)
        st.write(f"Length: {len(transcript)} words")