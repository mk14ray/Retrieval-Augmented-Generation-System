from pydantic import BaseModel, HttpUrl
from typing import Union, List, Optional
from core.document_loader import load_document
from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from core.vector_store import VectorStore
from core.rag import RAGSystem

app = FastAPI()

#load the vector and ragsystem class
vector_store = VectorStore()
rag_system = RAGSystem(vector_store)

#API Params
class URLInput(BaseModel):
    url: Union[HttpUrl, None] = None

#this api for upload the data.
@app.post("/upload_data")
async def upload_file(url: Optional[str] = Form(None), file: Optional[UploadFile] = File(None)):
    if not file and not url:
        raise HTTPException(status_code=400, detail="Either a file or a URL must be provided.")

    documents: List = []
    if file:
        # Handle file upload
        file_path = f"data/{file.filename}"
        file_type = file.filename.split(".")[-1]

        if file_type not in ["txt", "pdf"]:
            raise HTTPException(status_code=400, detail="Unsupported file type. Only .txt and .pdf are allowed.")

        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        file_documents = load_document(file_path, file_type)
        documents.extend(file_documents)

    if url:
        # Handle URL input
        url_path = url
        file_type = "url"

        url_documents = load_document(url_path, file_type)
        documents.extend(url_documents)

    if documents:
        vector_store.add_documents(documents)
        return {"message": "Data uploaded and processed successfully"}
    else:
        raise HTTPException(status_code=400, detail="No valid data found to process")

#this api for ask questions related to data.
@app.post("/ask_query")
async def ask_question(query: str):
    response = rag_system.generate_response(query)
    return {"answer": response}