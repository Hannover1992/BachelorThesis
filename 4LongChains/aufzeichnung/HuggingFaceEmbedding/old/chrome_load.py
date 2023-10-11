import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

chroma_client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./db" # Optional, defaults to .chromadb/ in the current directory
))


model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

collection = chroma_client.get_collection(name="WisMet", embedding_function=model)


results = collection.query(
    query_texts=["Die Praktische erfahrung ist sehr wichtig"],
    n_results=2
)

for x in results:
    print(x)

