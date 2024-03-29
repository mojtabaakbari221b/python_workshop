import openai
from .configs import API_KEY

def chat():

  openai.api_key = API_KEY

  my_question = "tell me about covid"
  # my_question = input("what is your question: ")

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
          "role": "user",
          "content": my_question,
      }
    ],
  )

  return completion.choices[0].message.get("content")