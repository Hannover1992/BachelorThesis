import os
from langchain.embeddings import HuggingFaceEmbeddings

from global_var import chunk, overlap
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import PythonCodeTextSplitter
from langchain.vectorstores import Chroma

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

with open('all_txt.txt', 'r') as file:
    text = file.read()

# Split text into words
python_splitter = PythonCodeTextSplitter(chunk_size=chunk, chunk_overlap=overlap)
docs = python_splitter.create_documents([text])
splitted_text = python_splitter.split_text(text)
embeddings = OpenAIEmbeddings()
embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

store = Chroma.from_documents(docs, embeddings, persist_directory='db')

store.persist()



