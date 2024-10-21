# speech_to_text.py

import io
from google.cloud import speech_v1p1beta1 as speech
from google.oauth2 import service_account

def audio_to_text_with_timestamps(audio_file):
    # Path to your service account key file
    client_file = 'audio_text_api.json'   # give jason path to your own api json file

    # Initialize credentials and client
    credentials = service_account.Credentials.from_service_account_file(client_file)
    client = speech.SpeechClient(credentials=credentials)

    # Read the audio file content
    with io.open(audio_file, "rb") as f:
        content = f.read()

    # Create RecognitionAudio object
    audio = speech.RecognitionAudio(content=content)

    # Configure recognition settings
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,  # Ensure this matches the audio's sample rate
        language_code='en-US',
        enable_automatic_punctuation=True,
        enable_word_time_offsets=True,  # Enable word-level timestamps
        model='video'
    )

    try:
        # Perform asynchronous speech recognition
        operation = client.long_running_recognize(config=config, audio=audio)
        print("Waiting for operation to complete...")
        response = operation.result(timeout=3600)  # Wait up to 1 hour for completion

        # Extract transcript and word timestamps from the response
        transcript = ""
        words_info = []

        for result in response.results:
            alternative = result.alternatives[0]
            transcript += alternative.transcript + " "
            for word_info in alternative.words:
                word = word_info.word
                start_time = word_info.start_time.total_seconds()
                end_time = word_info.end_time.total_seconds()
                words_info.append({
                    'word': word,
                    'start_time': start_time,
                    'end_time': end_time
                })

        return transcript.strip(), words_info

    except Exception as e:
        print(f"An error occurred during transcription: {e}")
        return "Transcription failed. Please try again.", []
