from langchain.text_splitter import PythonCodeTextSplitter
from langchain.vectorstores import Chroma
from sentence_transformers import SentenceTransformer, util
import chromadb
from chromadb.config import Settings

with open('../all_txt.txt', 'r') as file:
    text = file.read()

# Split text into words
python_splitter = PythonCodeTextSplitter(chunk_size=1000, chunk_overlap=0)
# docs = python_splitter.create_documents([text])
splitted_text = python_splitter.split_text(text)

model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = model.encode(splitted_text)
embeddings = embeddings.tolist()

# db = Chroma.from_texts(texts=splitted_text, embedding=model, persist_directory='HuggingFaceDB')
chroma_client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./db" # Optional, defaults to .chromadb/ in the current directory
))

collection = chroma_client.create_collection(name="WisMet")




ids = [str(i) for i in range(len(embeddings))]
collection.add(ids=ids, embeddings=embeddings, documents=splitted_text, increment_index=True)



collection = chroma_client.get_collection(name="WisMet", embedding_function=model)


results = collection.query(
    query_texts=["Die Praktische erfahrung ist sehr wichtig"],
    n_results=2
)

for x in results:
    print(x)
