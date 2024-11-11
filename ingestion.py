from dotenv import load_dotenv
load_dotenv()

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import RetrievalMode
import os
from uuid import uuid4
from bs4 import BeautifulSoup
from langchain.schema import Document
import requests



os.environ["USER_AGENT"] = "MyCustomAgent/1.0"
def read_files(file_paths):
    docs_list = []
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text_content = f.read()
            doc = Document(
                metadata={"source": file_path, "title": os.path.basename(file_path)},
                page_content=text_content
            )
            docs_list.append(doc)
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")

    return docs_list


def delete_collection(client, collection_name):
    client.delete_collection(collection_name)

def create_collection(client,collection_name,vector_size):
    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
    )

"""
Now upload it to Qdrant
"""

os.getenv('OPENAI_API_KEY')
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# List of file paths



legal_doc_path=['D:/12.Python Scrypts/44.ADVANCED_CONTRACT/txt/conduct_scenarios.txt']
docs_list=read_files(legal_doc_path)
# Split documents into chunks using a text splitter with a specified chunk size and overlap
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=500, chunk_overlap=0
)

doc_splits=text_splitter.split_documents(docs_list) # Split documents into chunks

"""
print("Split Documents:")
for idx, doc in enumerate(doc_splits):
    print(f"Split Document {idx+1} Metadata: {doc.metadata}")
    print(f"Split Document {idx+1} Content Snippet:\n{doc.page_content[:200]}")
    print("-" * 50)
"""


"""
Retriever and Collection for the legal doc analyzed
"""

# Connect to the Qdrant client (adjust the host and port if necessary)

client = QdrantClient(path="/qdrant/")
collection_name = "legal_doc_to_analyze"
vector_size = 3072  # Adjust based on your embedding model's output si

# Connect to the Qdrant client (adjust the host and port if necessary)

try:
    delete_collection(client,collection_name)
    print(f"Collection '{collection_name}' has been deleted successfully.")
except:
    print(f"Collection '{collection_name}' could not be deleted.")

try:
    create_collection(client,collection_name,vector_size)
    print(f"Collection '{collection_name}' has been created successfully.")
except:
    print(f"Collection '{collection_name}' could not be created.")

qdrant = QdrantVectorStore(
    client=client,
    collection_name=collection_name,
    embedding=embeddings,
)

# Generate unique IDs for each document
ids = [str(uuid4()) for _ in doc_splits]

# Add documents to the vector store
qdrant.add_documents(documents=doc_splits, ids=ids)

# Convert Qdrant instance to a retriever for information retrieval
retriever_legal_doc = qdrant.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 10}
)
"""
sample_query = "What means confidential information"

# Invoke the retriever with the sample query
retrieved_documents = retriever_legal_doc.invoke(sample_query)

# Print retrieved documents to check relevance and diversity
print("Retrieved Documents for Sample Query:")
for idx, doc in enumerate(retrieved_documents[:]):  # Limit to first 5 results
    print(f"Document {idx+1} Metadata: {doc.metadata}")
    print(f"Document {idx+1} Content Snippet: {doc.page_content[:]}")  # Show first 300 characters of content
    print("-" * 50)
"""

"""
Now the rest of the legal docs
"""

# List of file paths

other_docs_path=['D:/12.Python Scrypts/44.ADVANCED_CONTRACT/txt/Acceptability_criteria.txt','D:/12.Python Scrypts/44.ADVANCED_CONTRACT/txt/NDA.txt' ]
docs_list=read_files(other_docs_path)
# Split documents into chunks using a text splitter with a specified chunk size and overlap
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=500, chunk_overlap=0
)

doc_splits=text_splitter.split_documents(docs_list) # Split documents into chunks



print("Split Documents:")
for idx, doc in enumerate(doc_splits):
    print(f"Split Document {idx+1} Metadata: {doc.metadata}")
    print(f"Split Document {idx+1} Content Snippet:\n{doc.page_content[:200]}")
    print("-" * 50)



collection_name = "other_legal_docs"
vector_size = 3072  # Adjust based on your embedding model's output si

# Connect to the Qdrant client (adjust the host and port if necessary)

try:
    delete_collection(client,collection_name)
    print(f"Collection '{collection_name}' has been deleted successfully.")
except:
    print(f"Collection '{collection_name}' could not be deleted.")

try:
    create_collection(client,collection_name,vector_size)
    print(f"Collection '{collection_name}' has been created successfully.")
except:
    print(f"Collection '{collection_name}' could not be created.")

qdrant_other = QdrantVectorStore(
    client=client,
    collection_name=collection_name,
    embedding=embeddings,
)

# Generate unique IDs for each document
ids = [str(uuid4()) for _ in doc_splits]

# Add documents to the vector store
qdrant_other.add_documents(documents=doc_splits, ids=ids)

# Convert Qdrant instance to a retriever for information retrieval
retriever_other = qdrant_other.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 10}
)


sample_query = "acceptability clauses"

# Invoke the retriever with the sample query
retrieved_documents = retriever_other.invoke(sample_query)

# Print retrieved documents to check relevance and diversity
print("Retrieved Documents for Sample Query:")
for idx, doc in enumerate(retrieved_documents[:]):  # Limit to first 5 results
    print(f"Document {idx+1} Metadata: {doc.metadata}")
    print(f"Document {idx+1} Content Snippet: {doc.page_content[:]}")  # Show first 300 characters of content
    print("-" * 50)
