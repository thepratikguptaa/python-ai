import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

print('''

 ███            █████████  ██████████ ██████   ██████ █████ ██████   █████ █████
░░░███         ███░░░░░███░░███░░░░░█░░██████ ██████ ░░███ ░░██████ ░░███ ░░███
  ░░░███      ███     ░░░  ░███  █ ░  ░███░█████░███  ░███  ░███░███ ░███  ░███
    ░░░███   ░███          ░██████    ░███░░███ ░███  ░███  ░███░░███░███  ░███
     ███░    ░███    █████ ░███░░█    ░███ ░░░  ░███  ░███  ░███ ░░██████  ░███
   ███░      ░░███  ░░███  ░███ ░   █ ░███      ░███  ░███  ░███  ░░█████  ░███
 ███░         ░░█████████  ██████████ █████     █████ █████ █████  ░░█████ █████
░░░            ░░░░░░░░░  ░░░░░░░░░░ ░░░░░     ░░░░░ ░░░░░ ░░░░░    ░░░░░ ░░░░░

      ''')

# List models
print("Available text generation models:")
models = client.models.list()
model_ids = [model.id for model in models if ('gemini' in model.id or 'gemma' in model.id) and 'embedding' not in model.id]
for i, model_id in enumerate(model_ids):
    print(f"{i + 1}: {model_id}")

# Get user's choice of model
model_choice = int(input("Choose a model (enter the number): ")) - 1
selected_model = model_ids[model_choice]

# Get user's prompt
user_prompt = input("Enter your prompt: ")

# Get response from AI
response = client.chat.completions.create(
    model=selected_model,
    messages=[
        {
            "role": "user",
            "content": user_prompt
        }
    ]
)

# Print the response
print("\nAI Response:")
print(response.choices[0].message.content)
