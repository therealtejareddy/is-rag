from langchain_ollama import OllamaEmbeddings, OllamaLLM, ChatOllama

from .utils import get_ollama_server_url

llm_model = OllamaLLM(
    base_url=get_ollama_server_url(),
    model="mistral",
    temperature=0.1,
    max_tokens=2048,
    streaming=True
)

embedding_model = OllamaEmbeddings(
    base_url=get_ollama_server_url(),
    model="nomic-embed-text"
)

chat_model = ChatOllama(
    base_url=get_ollama_server_url(),
    model="mistral",
    temperature=0.1,
    max_tokens=2048,
    streaming=True
)