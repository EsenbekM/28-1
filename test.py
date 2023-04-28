import openai
from decouple import config


openai.api_key = config("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Когда началась вторая мировая?",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)

print(response["choices"][0]['text'])
