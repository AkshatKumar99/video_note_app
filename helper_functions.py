from youtube_transcript_api import YouTubeTranscriptApi

def get_youtube_transcript(video_url):
    try:
        video_id = video_url.split('v=')[1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return parse_transcript(transcript)
    except Exception as e:
        return f"Error: {str(e)}"
        
def parse_transcript(transcript):
    
    text = ""
    for current_section in transcript:
        text+=current_section["text"]
        text+=" "
    return text