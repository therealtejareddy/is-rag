from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

def chat_response(chat_model: ChatOllama, state):
    prompt = get_prompt()
    print(f"Prompt: {prompt}")
    chain = prompt | chat_model | StrOutputParser()
    response = chain.invoke(state)
    print(f"Response: {response}")
    return response


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
