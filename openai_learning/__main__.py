import openai
from UserCredentials import openai_api_key

openai.api_key = openai_api_key
models_list = openai.Model.list()