import os
from openai import OpenAI
client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')

# completion = client.chat.completions.create( # Change the method name
#   model = 'gpt-3.5-turbo',
#   messages = [ # Change the prompt parameter to messages parameter
#     {'role': 'user', 'content': 'Hello!'}
#   ],
#   temperature = 0  
# )

# print(completion.choices[0].message.content) # Change message content extraction


from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)

print(response.choices[0].message.content)