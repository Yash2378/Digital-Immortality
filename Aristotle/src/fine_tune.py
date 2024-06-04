import requests
import json
import os

# Retrieve the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")

# Define the endpoint URL
url = 'https://api.openai.com/v1/fine_tuning/jobs'

# Define the payload data
payload = {
    "training_file": "file-wcPUgMZYvQ3r4R3qLecPOezH",  # Update with actual training file ID
    "model": "gpt-3.5-turbo"
}

# Define headers with authorization
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Send the POST request to start fine-tuning
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Print the response
print(response.json())
