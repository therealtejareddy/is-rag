import streamlit as st
import random
import time
from rag.models import llm_model, embedding_model
from rag.rag import rag_chat
from rag.vector_helper import handle_upload_file
from htbuilder import p, styles


st.set_page_config(layout="wide", page_title="RAG Chat App", page_icon=":speech_balloon:")


st.title("RAG chat")

with st.sidebar:
    st.title("Upload Document")
    uploaded_file = st.file_uploader(
        "Upload a document (PDF, DOCX, TXT, etc.)",
        type=["pdf", "docx", "txt"],
        help="Upload a document to chat with it.",
        label_visibility="collapsed",
        accept_multiple_files=False,
        key="file_uploader",
        on_change=lambda: st.session_state.messages.clear(),
    )
    if uploaded_file is not None:
        vector_store = handle_upload_file(embedding_model, uploaded_file)
    p_styles = styles(
        position="fixed",
        bottom="0",
        left="50px",
        width="100%",
        padding="10px",
    )
    body = p("Made with ❤️ by Yuvateja Reddy", style=p_styles)
    st.markdown(body,unsafe_allow_html=True)


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask anything"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        # response = st.write_stream(llm_model.stream(prompt))
        # response = rag_chat(prompt, vector_store)
        response = st.write_stream(rag_chat(prompt, vector_store))

        # response = llm_model.invoke(prompt)
        # # Create an empty container to hold the streaming text
        # output = st.empty()
        # streamed_text = ""

        # for word in response.split("\n"):  # or character-by-character: `for char in response:`
        #     streamed_text += word + " "
        #     output.markdown(streamed_text)
        #     time.sleep(0.05)  # adjust delay as needed
        
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

