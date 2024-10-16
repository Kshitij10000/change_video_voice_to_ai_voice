from moviepy.editor import VideoFileClip 
import os
import tempfile

def extract_audio(video_path):
    audio_path = os.path.join(tempfile.gettempdir(), "extracted_audio_mono.wav")
    with VideoFileClip(video_path) as video:
        # Convert audio to mono by setting channels to 1 using ffmpeg_params
        video.audio.write_audiofile(
            audio_path,
            codec='pcm_s16le',
            fps=44100,
            ffmpeg_params=["-ac", "1"]  # Set audio channels to mono
            )
    return audio_path