import os
import openai

# Retrieve the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")

# Set the OpenAI API key
openai.api_key = api_key

try:
    # Upload the dataset
    response = openai.File.create(
        file=open("aristotle_prompt_completion.json", "rb"),
        purpose='fine-tune'
    )

    file_id = response['id']  # Save this ID for the fine-tuning step
    print("File uploaded successfully. File ID:", file_id)

except Exception as e:
    print("An error occurred:", e)
