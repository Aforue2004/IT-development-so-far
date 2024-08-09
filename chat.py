import os
import openai

# Set the API key using the environment variable
openai.api_key = os.getenv('OPENAI')

# Create a chat completion
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hi ChatGPT. Say hi back!"}
    ]
)

# Extract the answer from the response
answer = response['choices'][0]['message']['content']
print(answer)
