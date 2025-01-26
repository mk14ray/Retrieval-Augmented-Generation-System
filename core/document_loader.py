from langchain_community.document_loaders import WebBaseLoader, TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

#handle the document basis of filetype.
def load_document(file_path: str, file_type: str):
    if file_type == "text":
        loader = TextLoader(file_path)
    elif file_type == "pdf":
        loader = PyPDFLoader(file_path)
    elif file_type == "url":
        loader = WebBaseLoader(file_path)
    else:
        raise ValueError("Unsupported file type")
    
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return text_splitter.split_documents(documents)