import io
from google.cloud import speech_v1p1beta1 as speech
from google.oauth2 import service_account

def audio_to_text(audio_file):
    # Path to your service account key file
    client_file = 'audio_text_api.json'

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
        enable_automatic_punctuation=True ,# Optional: Adds punctuation to the transcript
        model = 'video' 
    )

    try:
        # Perform asynchronous speech recognition
        operation = client.long_running_recognize(config=config, audio=audio)
        print("Waiting for operation to complete...")
        response = operation.result(timeout=3600)  # Wait up to 1 hour for completion

        # Extract transcript from the response
        transcript = ""
        for result in response.results:
            transcript += result.alternatives[0].transcript + "\n"

        return transcript

    except Exception as e:
        print(f"An error occurred during transcription: {e}")
        return "Transcription failed. Please try again."
