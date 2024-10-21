# text_to_speech.py

from google.cloud import texttospeech
import os
import tempfile

# Ensure the path to your Google Cloud service account key is correct
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'text_audio_api.json' # give jason path to your own api json file 

client = texttospeech.TextToSpeechClient()

def text_to_speech_segment(text_segment):
    synthesis_input = texttospeech.SynthesisInput(text=text_segment)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name='en-US-Journey-D'  # Ensure this is a valid and supported voice
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        # Optionally, adjust speaking rate and pitch if needed
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    # Create a temporary file to store the generated audio segment
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_audio:
        tmp_audio.write(response.audio_content)
        tmp_audio_path = tmp_audio.name
        print(f'Audio segment written to "{tmp_audio_path}"')

    return tmp_audio_path
