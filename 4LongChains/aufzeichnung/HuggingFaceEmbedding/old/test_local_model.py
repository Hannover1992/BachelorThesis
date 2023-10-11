from langchain.text_splitter import PythonCodeTextSplitter
from langchain.vectorstores import Chroma
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

query_embedding = model.encode('How big is London')
passage_embedding = model.encode(['London has 9,787,426 inhabitants at the 2011 census',
                                  'London is known for its finacial district'])

print("Similarity:", util.dot_score(query_embedding, passage_embedding))


with open('../all_txt.txt', 'r') as file:
    text = file.read()

# Split text into words
python_splitter = PythonCodeTextSplitter(chunk_size=500, chunk_overlap=0)
docs = python_splitter.create_documents([text])
splitted_text = python_splitter.split_text(text)

db = Chroma.from_documents(documents=docs, embedding=model, persist_directory='HuggingFaceDB')
