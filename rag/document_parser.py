import io
import docx
import PyPDF2
import os
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path



def read_text_file(file):
    """Read content from a text file"""
    stringio = io.StringIO(file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    return string_data

def read_pdf_file(file):
    """Read content from a PDF file"""
    text = ""
    with io.BytesIO(file) as open_pdf_file:
        pdf_reader = PyPDF2.PdfReader(open_pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
    return text

def read_docx_file(file):
    """Read content from a Word document"""
    with io.BytesIO(file) as open_pdf_file:
        doc = docx.Document(open_pdf_file)
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    return text


def read_document(file):
    file_extension = Path(file.name).suffix.lower()
    if file_extension == '.txt':
        return read_text_file(file)
    elif file_extension == '.pdf':
        return read_pdf_file(file.read())
    elif file_extension == '.docx':
        return read_docx_file(file.read())
    else:
        raise ValueError(f"Unsupported file format: {file_extension}")

def read_st_document(uploaded_file):
    if uploaded_file is not None:
        return read_document(uploaded_file)
