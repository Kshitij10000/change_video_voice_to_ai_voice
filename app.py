# app.py

import streamlit as st
import tempfile
import os
from video_to_audio import extract_audio
from speech_to_text import audio_to_text_with_timestamps
from azure_openai_integration import Azure_openai_service
from text_to_speech import text_to_speech_segment
from synchronize_audio import synchronize_speech_segments
from replace_audio import replace_audio
from pydub import AudioSegment

st.title("AI-Powered Video Audio Replacement with Synchronization")

uploaded_file = st.sidebar.file_uploader("Upload a Video File", type=["mp4", "mov", "avi", "mkv"])

if uploaded_file is not None:
    try:
        with st.spinner("Extracting audio from video..."):
            # Save the uploaded video to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_video:
                tmp_video.write(uploaded_file.read())
                video_path = tmp_video.name
            st.video(video_path)

            # Extract and convert audio to mono
            audio_path = extract_audio(video_path)
        
        # Display the extracted audio
        st.sidebar.audio(audio_path, format='audio/wav')

        # Display audio file size
        audio_size = os.path.getsize(audio_path)
        st.sidebar.write(f"Audio file size: {audio_size / (1024 * 1024):.2f} MB")

        with st.spinner("Transcribing audio... This may take a while for large files."):
            # Transcribe the extracted audio with timestamps
            transcript, words_info = audio_to_text_with_timestamps(audio_path)
            st.sidebar.text_area("Original Transcription", transcript, height=300)

        with st.spinner("Correcting Transcription... This may take a while for large files."):
            # Use Azure services to correct the grammar and remove filler words
            corrected_transcript, corrected_words_info = Azure_openai_service(transcript, words_info)
            st.sidebar.text_area("Corrected Transcription", corrected_transcript, height=300)

        with st.spinner("Generating and Synchronizing Audio... This may take a while for large files."):
            # Generate synchronized speech audio
            synchronized_audio_path = synchronize_speech_segments(
                corrected_words_info,
                corrected_transcript,
                text_to_speech_segment
            )

            # Determine audio format for display
            _, gen_ext = os.path.splitext(synchronized_audio_path)
            gen_ext = gen_ext.lower()
            if gen_ext == '.wav':
                audio_format = 'audio/wav'
            elif gen_ext == '.mp3':
                audio_format = 'audio/mp3'
            else:
                audio_format = 'audio/mpeg'  # Default fallback

            # Display the synchronized audio in the sidebar
            st.sidebar.audio(synchronized_audio_path, format=audio_format)

        with st.spinner("Replacing audio in video..."):
            try:
                st.write(f"Video Path: {video_path}")
                st.write(f"Synchronized Audio Path: {synchronized_audio_path}")
                final_video_path = replace_audio(video_path, synchronized_audio_path)
                st.write(f"Final Video Path: {final_video_path}")
            except Exception as e:
                st.error(f"Error during audio replacement: {e}")
                final_video_path = None  # Explicitly set to None

        if final_video_path:
            st.success("Processing complete!")
            st.video(final_video_path)

            # Provide download link
            with open(final_video_path, "rb") as final_video:
                st.download_button(
                    label="Download Video with New Audio",
                    data=final_video,
                    file_name="final_video.mp4",
                    mime="video/mp4"
                )

            # Cleanup temporary files
            try:
                os.remove(video_path)
                os.remove(audio_path)
                os.remove(synchronized_audio_path)
                os.remove(final_video_path)
            except Exception as cleanup_error:
                st.warning(f"Could not delete temporary files: {cleanup_error}")
        else:
            st.error("Failed to process the video due to audio replacement error.")

    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please upload a video file to begin.")
