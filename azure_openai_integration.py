# transcript = """Welcome to English in a minute. If you've ever gardened, you know, weeds grow super fast. They can take over a garden overnight, but what does grow like a weed mean in other situations?
#  Hey Dan. Do you want to see pictures from my trip home? Oh, jeez. I would love to but great. This is me with my little cousin Arlo little. He's taller than you. I know he is growing like a weed. He's only ten.
#  Does he have a beard to grow like a weed? Just means to grow very quickly. We mostly use this expression when talking about how fast children grow
#  and that's English in a minute."""
 
azure_endpoint = "https://internshala.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview`"
deployment_name = "gpt-4o"

import os
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()
  
client = AzureOpenAI(
    api_version="2024-08-01-preview",
    azure_endpoint=azure_endpoint,
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  # Retrieve the API key from the environment
)

def Azure_openai_service(transcript):
  prompt = f"Please correct the following transcription by fixing grammatical mistakes and removing filler words like 'um', 'uh', 'hmm', etc:\n\n{transcript}"
      
  completion = client.chat.completions.create(
      model="gpt-4o",  # Ensure this matches your deployment name
      messages=[
                  {"role": "system", "content": "You are a helpful assistant that corrects transcriptions."},
                  {"role": "user", "content": prompt}
              ],
  )

  # Extract and print only the message content
  message_content = completion.choices[0].message.content
  
  return message_content
