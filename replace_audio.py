from moviepy.editor import VideoFileClip, AudioFileClip
from pydub import AudioSegment
import tempfile
import os 

# Function to replace audio in video
def replace_audio(video_path, new_audio_path):
    # Verify that input files exist
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")
    if not os.path.exists(new_audio_path):
        raise FileNotFoundError(f"New audio file not found: {new_audio_path}")

    # Determine audio format based on file extension
    _, ext = os.path.splitext(new_audio_path)
    ext = ext.lower()

    if ext == '.wav':
        new_audio = AudioSegment.from_wav(new_audio_path)
    elif ext == '.mp3':
        new_audio = AudioSegment.from_mp3(new_audio_path)
    else:
        raise ValueError(f"Unsupported audio format: {ext}")

    # Export new audio to a format compatible with MoviePy (mp3)
    temp_new_audio = os.path.join(tempfile.gettempdir(), "temp_new_audio.mp3")
    new_audio.export(temp_new_audio, format="mp3")

    # Load the new audio into MoviePy
    new_audio_clip = AudioFileClip(temp_new_audio)

    # Load the video
    video = VideoFileClip(video_path)

    # Set the new audio
    final_video = video.set_audio(new_audio_clip)

    # Export the final video
    final_video_path = os.path.join(tempfile.gettempdir(), "final_video.mp4")
    final_video.write_videofile(final_video_path, codec="libx264", audio_codec="aac")

    # Close clips to release resources
    video.close()
    new_audio_clip.close()
    final_video.close()

    return final_video_path