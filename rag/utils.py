import os

def get_ollama_server_url():
    if "OLLAMA_SERVER_URL" in os.environ:
        return os.environ["OLLAMA_SERVER_URL"]
    else:
        raise ValueError("OLLAMA_SERVER_URL environment variable is not set. Please set it to the URL of your Ollama server.")