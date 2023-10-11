import os
from langchain.llms import OpenAI
import streamlit as st
from langchain.vectorstores import Chroma
from dotenv import load_dotenv

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.9)

prompt = st.text_input('Niebo gwazdziste nademna, prawo moralne we mnie. A ty, czym jesteś?Jestem twoją wolnością. Jestem tym, co masz, czego się trzymasz, czym możesz zdecydować i dążyć do tego, co uważasz za słuszne. Jestem tym, co możesz zmienić i wpłynąć na życie innych. Jestem tym, co jest w twojej ręce.')

class Document:
    def __init__(self, content):
        self.page_content = content

def load_and_split_file(filename, chunk_size=5000):
    with open(filename, 'r') as file:
        text = file.read()
    # Create a list of Document objects, each containing a chunk of text
    return [Document(text[i:i + chunk_size]) for i in range(0, len(text), chunk_size)]

text_data_chunks = load_and_split_file('Wissenschaftliche_Methoden/all_txt.txt')

store = Chroma.from_documents(text_data_chunks, collection_name='Wissenschaftliche Methoden')

MIN_SCORE_THRESHOLD = 0.75  # adjust as needed

if prompt:
    with st.expander('Document Similarity Search'):
        search = store.similarity_search_with_score(prompt)

        # Only show top 10 results above the threshold
        filtered_search = [(chunk, score) for chunk, score in search if score > MIN_SCORE_THRESHOLD]
        sorted_search = sorted(filtered_search, key=lambda x: x[1], reverse=True)[:10]

        for chunk, score in sorted_search:
            st.write(f"Chunk: {chunk[:100]}... Score: {score}")  # Display the first 100 characters of each chunk and its score
