
import os

api_key = os.environ.get('OPENAI_API_KEY')
if not api_key:
    raise ValueError("API-Schlüssel nicht gefunden!")

# Nun können Sie den Schlüssel mit der OpenAI-Bibliothek verwenden
import openai
import streamlit as st

# Setzen Sie Ihren API-Schlüssel
openai.api_key = api_key


model_list = openai.Model.list()
model_names = [model['id'] for model in model_list['data']]


print(model_names)
