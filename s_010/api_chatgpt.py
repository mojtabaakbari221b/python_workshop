import openai
from .configs import API_KEY

openai.api_key = API_KEY

my_question = "tell me about history of iran"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
        "role": "user",
        "content": my_question,
    }
  ],
)

print(completion.choices[0].message.get("content"))