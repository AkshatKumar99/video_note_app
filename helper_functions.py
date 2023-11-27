from youtube_transcript_api import YouTubeTranscriptApi

def get_youtube_transcript(video_url):
    try:
        video_id = video_url.split('v=')[1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        return f"Error: {str(e)}"
        