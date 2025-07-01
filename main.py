from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
import os
import openai


load_dotenv();

api_key = os.getenv("OPENAI_API_KEY")

def get_transcript(video_id):
    try:
        transcript=YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([entry["text"] for entry in transcript])
        return text
    except Exception as e:
        print("Transcript not available:", e)
        return None

text = get_transcript("kqaMIFEz15s")

def summarize_text(text):
    openai.api_key = api_key

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages= [
               {"role": "system", "content": "You summarize YouTube transcripts."},
            {"role": "user", "content": f"Please summarize this video transcript in Markdown format:\n{text}"}
        ],
        max_tokens=300
    )

    return response.choices[0].message.content



summary = summarize_text(text);

print(summary)
