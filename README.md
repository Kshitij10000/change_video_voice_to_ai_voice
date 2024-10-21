## 🎥 AI-Powered Video Audio Replacement with Synchronization
Welcome to the AI-Powered Video Audio Replacement with Synchronization project! This application allows you to upload a video file, transcribe its audio, correct the transcription (removing filler words and fixing grammar), synthesize new audio, and replace the original audio in the video with the new synchronized audio. All seamlessly and automatically! 🚀

# 📋 Table of Contents
Features
Demo
Installation
Usage
Modules
Dependencies
Configuration
Contributing
License
Acknowledgments

# ✨ Features
Upload Videos: Supports various video formats like MP4, MOV, AVI, MKV.
Audio Extraction: Extracts audio from the uploaded video and converts it to mono.
Speech-to-Text: Transcribes the audio using Google Speech-to-Text API.
Transcription Correction: Corrects grammar and removes filler words using Azure OpenAI GPT-4.
Text-to-Speech: Converts the corrected text back to speech using Google Text-to-Speech API.
Audio Synchronization: Synchronizes the new audio with the original video's timing.
Audio Replacement: Replaces the original audio in the video with the new audio.
Streamlit Web Interface: User-friendly interface to interact with the application.

🎬 Demo


Click on the link to watch the demo video.
https://drive.google.com/file/d/1cVq1MlA69IeI8yFdXnP595GbO3tOuzrB/view?usp=sharing

# 🛠️ Installation
Prerequisites
Python 3.7 or higher
Google Cloud SDK (for authentication with Google APIs)
Azure OpenAI Service

Clone the Repository

git clone https://github.com/yourusername/ai-powered-video-audio-replacement.git
cd ai-powered-video-audio-replacement

Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

Install Dependencies
pip install -r requirements.txt
Download NLTK Data
import nltk
nltk.download('punkt')

# 🚀 Usage
Running the Application
streamlit run app.py
Steps
Upload a Video: Use the sidebar to upload your video file.
Processing: The app will extract audio, transcribe, correct, synthesize, and synchronize.
Download: Once processing is complete, you can download the new video with replaced audio.

# 📁 Modules
app.py: Main Streamlit application file.
video_to_audio.py: Extracts audio from video.
speech_to_text.py: Transcribes audio to text using Google Speech-to-Text API.
azure_openai_integration.py: Corrects transcription using Azure OpenAI GPT-4.
synchronize_audio.py: Synchronizes the synthesized speech with original timings.
text_to_speech.py: Converts text to speech using Google Text-to-Speech API.
replace_audio.py: Replaces the original audio in the video with the new audio.

# 📚 Dependencies
Streamlit
MoviePy
Pydub
NLTK
Google Cloud Speech-to-Text
Google Cloud Text-to-Speech
Azure OpenAI Service
dotenv
# ⚙️ Configuration
Google Cloud Setup
Create a Google Cloud Project.
Enable Speech-to-Text and Text-to-Speech APIs.
Download Service Account Key: Save as audio_text_api.json and text_audio_api.json.
Azure OpenAI Setup
Create an Azure OpenAI Resource.
Deploy a GPT-4 Model.
Set Environment Variables:
AZURE_OPENAI_API_KEY: Your Azure OpenAI API key.
Environment Variables
Create a .env file in the project root:
env
AZURE_OPENAI_API_KEY=your-azure-openai-api-key
# 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request.

# 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

# 🙏 Acknowledgments
OpenAI for GPT-4.
Google Cloud for Speech-to-Text and Text-to-Speech APIs.
Streamlit for the awesome web app framework.
MoviePy and Pydub for multimedia processing.
NLTK for natural language processing tools.
