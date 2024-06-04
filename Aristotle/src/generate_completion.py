import os
import openai

# Retrieve the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")

# Set the OpenAI API key
openai.api_key = api_key

# Replace with the actual ID of your fine-tuning job
fine_tune_job_id = 'your_fine_tune_job_id'  # Update this with the actual job ID

try:
    # Retrieve the fine-tuning job details
    fine_tune_job = openai.FineTune.retrieve(fine_tune_job_id)

    # Generate a completion using the fine-tuned model ID
    completion = openai.Completion.create(
        model=fine_tune_job['fine_tuned_model_id'],
        prompt="What is virtue?",
        max_tokens=50
    )

    print("Generated text:", completion['choices'][0]['text'].strip())

except Exception as e:
    print("An error occurred:", e)
