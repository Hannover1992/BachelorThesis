import openai
import os
import streamlit as st

api_key = os.environ.get('OPENAI_API_KEY')
if not api_key:
    raise ValueError("API-Schlüssel nicht gefunden!")
openai.api_key = api_key

model_list = openai.Model.list()
# Filtere Modelle, um nur diejenigen anzuzeigen, die "gpt" in ihrem Namen haben
model_names = [model['id'] for model in model_list['data'] if 'gpt' in model['id']]

st.title('GPT-3 Streamlit App')

# Dropdown zur Auswahl des Modells
selected_model = st.selectbox("Wählen Sie ein Modell aus:", model_names)

# Neues Textfeld für "Instruction"
instruction_text = st.text_area("Geben Sie die Anweisung ein:")

user_input = st.text_area("Geben Sie Ihren Text (Prompt) ein:")

max_tokens_slider = st.slider(
    "Maximale Tokenanzahl für die Antwort:", 
    min_value=1, 
    max_value=2048, 
    value=150,  # Standardwert ist 150
    step=1
)

def gpt_turbo_resp(prompt_text, model_name, instruction="", max_tokens=150):
    if "turbo" in model_name:
        messages = [{"role": "system", "content": "You are a helpful assistant."}]
        
        if instruction:
            messages.append({"role": "system", "content": instruction})

        messages.append({"role": "user", "content": prompt_text})

        response = openai.ChatCompletion.create(
            model=model_name,
            messages=messages,
            max_tokens=max_tokens
        )
        return response['choices'][0]['message']['content'].strip()
    else:
        response = openai.Completion.create(
            engine=model_name,
            prompt=prompt_text,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()

if user_input:
    response = gpt_turbo_resp(user_input, selected_model, instruction_text, max_tokens_slider)
    st.text_area("Antwort:", response)
