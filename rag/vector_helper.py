from langchain_core.vectorstores import InMemoryVectorStore
from .document_parser import read_st_document
from .text_splitter import split_text
from streamlit.runtime.uploaded_file_manager import UploadedFile


def create_vector_store(embeddings):
    return InMemoryVectorStore(embeddings)

def add_documents_to_vector_store(vector_store: InMemoryVectorStore, documents, embeddings) -> InMemoryVectorStore:
    return vector_store.from_documents(documents, embeddings)

def search_vector_store(vector_store, query, k=4):
    return vector_store.similarity_search(query, k=k)

def handle_upload_file(embeddings, uploaded_file: UploadedFile) -> InMemoryVectorStore:
        document_content = split_text(read_st_document(uploaded_file))
        vector_store = create_vector_store(embeddings)
        return add_documents_to_vector_store(vector_store, document_content, embeddings)