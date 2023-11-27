from youtube_transcript_api import YouTubeTranscriptApi

def get_youtube_transcript(video_url, api_key):
    try:
        video_id = video_url.split('v=')[1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id, developer_key=api_key)
        return transcript
    except:
        return "Unable to obtain transcript"
        