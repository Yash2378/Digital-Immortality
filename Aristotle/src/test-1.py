import os
import openai

# Retrieve the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")

# Set the OpenAI API key
openai.api_key = api_key

# Define a function to generate a completion
def generate_completion(prompt):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # Update with the correct model if needed
            prompt=prompt,
            max_tokens=50
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        print("An error occurred:", e)
        return None

# Test the function
if __name__ == "__main__":
    prompt = "What is virtue?"
    completion = generate_completion(prompt)
    if completion:
        print("Generated text:", completion)
