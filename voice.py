from pathlib import Path
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

text_file_path = Path(__file__).parent / "text.txt"
with open(text_file_path, "r") as file:
    text = file.read()

speech_file_path = Path(__file__).parent / "audio.mp3"

response = client.audio.speech.create(
    model="tts-1-hd",
    voice="echo",
    speed= 1,
    input=text
)

response.stream_to_file(speech_file_path)

# alloy, echo, fable, onyx, nova, shimmer
# tts-1-hd