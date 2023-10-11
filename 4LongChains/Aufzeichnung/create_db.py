import os
from embedding import create_embedding
from langchain.embeddings import HuggingFaceEmbeddings

from global_var import chunk, overlap
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import PythonCodeTextSplitter
from langchain.vectorstores import Chroma

# Function to read all text files in a directory and return their concatenated content
def read_all_txt_files_in_folder(folder_path):
    merged_text = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), 'r') as file:
                merged_text += file.read() + "\n"  # Add a newline after each file's content
    return merged_text

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Read all text files in 'aufzeichnung' folder and concatenate their contents
merged_text = read_all_txt_files_in_folder('./aufzeichnung')

# Split text into words
python_splitter = PythonCodeTextSplitter(chunk_size=chunk, chunk_overlap=overlap)
docs = python_splitter.create_documents([merged_text])
splitted_text = python_splitter.split_text(merged_text)
# embeddings = OpenAIEmbeddings()

embeddings = create_embedding()

store = Chroma.from_documents(docs, embeddings, persist_directory='db')

store.persist()
