import openai
from UserCredentials import openai_api_key
import PIL

openai.api_key = openai_api_key
models_list = openai.Model.list()


response = openai.Completion.create(
  model="text-davinci-003",
  prompt="who is barrack obama",
  max_tokens=50,
  temperature=0.2
)


print(response)

description = "cat shooting laser"

image_resp = openai.Image.create(prompt=description, n=4, size="512x512")
image_url = image_resp['data'][0]['url']

print(image_url)