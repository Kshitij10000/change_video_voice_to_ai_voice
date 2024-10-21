# azure_openai_integration.py

import os
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

azure_endpoint = "https://internshala.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview"
deployment_name = "gpt-4o"

client = AzureOpenAI(
    api_version="2024-08-01-preview",
    azure_endpoint=azure_endpoint,
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  # Retrieve the API key from the environment
)

def Azure_openai_service(transcript, words_info):
    # Combine words with their timestamps
    detailed_transcript = ""
    for word_entry in words_info:
        detailed_transcript += f"{word_entry['word']} "

    prompt = (
        "Please correct the following transcription by fixing grammatical mistakes and removing filler words like 'um', 'uh', 'hmm', etc. "
        "Ensure that the corrected text maintains the original timing for each word as much as possible.\n\n"
        f"{detailed_transcript.strip()}"
    )
        
    completion = client.chat.completions.create(
        model="gpt-4o",  # Ensure this matches your deployment name
        messages=[
            {"role": "system", "content": "You are a helpful assistant that corrects transcriptions."},
            {"role": "user", "content": prompt}
        ],
    )

    # Extract and print only the message content
    message_content = completion.choices[0].message.content
    
    # Here, you may need to implement a way to map corrected text back to timestamps.
    # This can be complex and may require advanced parsing depending on the correction output.
    # For simplicity, we will assume the corrected_transcript aligns with original timestamps.
    
    return message_content, words_info
