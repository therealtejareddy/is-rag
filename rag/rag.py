from .vector_helper import search_vector_store
from .models import chat_model
from langchain_core.vectorstores import InMemoryVectorStore
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama




def rag_chat(question: str, vector_store: InMemoryVectorStore):
    search_results = search_vector_store(vector_store, question)
    prompt = {
        "question": question,
        "context": search_results
    }
    chain = get_chain(chat_model)
    for chunk in chain.stream(prompt):
        yield chunk

def get_chain(chat_model: ChatOllama):
    prompt = get_prompt()
    print(f"Prompt: {prompt}")
    chain = prompt | chat_model | StrOutputParser()
    return chain


def get_prompt():
    prompt_template = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            "Hello! You are a helpful assistant that answers questions based on the provided context. "
            "When the user starts a conversation, greet them warmly with a short, polite welcome message. "
            "Don't answer questions that are not related to the context."
        ),
        HumanMessagePromptTemplate.from_template("{question}"),
        AIMessagePromptTemplate.from_template("Here is the information I found: {context}")
    ])
    return prompt_template