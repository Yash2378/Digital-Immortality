import time
import os
import openai

# Retrieve the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")

# Set the OpenAI API key
openai.api_key = api_key

# Define the fine-tune job ID
fine_tune_job_id = 'your_fine_tune_job_id'  # Update with the actual job ID

try:
    while True:
        # Retrieve fine-tuning job status
        job_status = openai.FineTune.retrieve(fine_tune_job_id)
        print("Fine-tune status:", job_status['status'])

        if job_status['status'] not in ['succeeded', 'failed']:
            time.sleep(10)  # Wait for 10 seconds before checking again
        else:
            break

except Exception as e:
    print("An error occurred:", e)
