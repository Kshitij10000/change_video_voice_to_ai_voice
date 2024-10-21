# synchronize_audio.py

from pydub import AudioSegment
import tempfile
import os

def synchronize_speech_segments(words_info, corrected_transcript, text_to_speech_segment_func):
    """
    Generates synchronized audio by placing each corrected word at its original timestamp.
    
    :param words_info: List of dictionaries containing word and its start_time and end_time.
    :param corrected_transcript: The corrected transcript text.
    :param text_to_speech_segment_func: Function to generate speech for a text segment.
    :return: Path to the final synchronized audio file.
    """
    # Split the corrected transcript into words
    corrected_words = corrected_transcript.split()

    if len(corrected_words) != len(words_info):
        print("Warning: The number of corrected words does not match the original words. Synchronization may be inaccurate.")
    
    # Initialize a silent audio segment with the duration of the original audio
    if words_info:
        total_duration_ms = int(words_info[-1]['end_time'] * 1000)
    else:
        total_duration_ms = 0
    final_audio = AudioSegment.silent(duration=total_duration_ms + 100)  # Extra second to ensure coverage

    # Iterate over each word and place the generated speech segment at the correct timestamp
    for idx, word_info in enumerate(words_info):
        if idx >= len(corrected_words):
            break  # Prevent index out of range if corrected words are fewer

        word = corrected_words[idx]
        start_time_ms = int(word_info['start_time'] * 1000)
        end_time_ms = int(word_info['end_time'] * 1000)

        # Generate speech for the word
        speech_audio_path = text_to_speech_segment_func(word)
        speech_audio = AudioSegment.from_file(speech_audio_path)

        # Calculate where to place the speech audio
        placement_time_ms = start_time_ms

        # Overlay the speech audio onto the final audio at the correct timestamp
        final_audio = final_audio.overlay(speech_audio, position=placement_time_ms)

        # Optionally, delete the temporary speech audio segment
        os.remove(speech_audio_path)

    # Export the final synchronized audio to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_final_audio:
        final_audio.export(tmp_final_audio.name, format="mp3")
        final_audio_path = tmp_final_audio.name
        print(f'Final synchronized audio written to "{final_audio_path}"')

    return final_audio_path
