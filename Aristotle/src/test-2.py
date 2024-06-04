import os
import openai

# Retrieve the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")

# Set the OpenAI API key
openai.api_key = api_key

# Define a function to retrieve fine-tuning job details
def retrieve_fine_tune_job(job_id):
    try:
        job_details = openai.FineTune.retrieve(job_id)
        return job_details
    except Exception as e:
        print("An error occurred:", e)
        return None

# Test the function
if __name__ == "__main__":
    fine_tune_job_id = "your_fine_tune_job_id"  # Replace with the actual fine-tune job ID
    job_details = retrieve_fine_tune_job(fine_tune_job_id)
    if job_details:
        print("Fine-tune job details:", job_details)
