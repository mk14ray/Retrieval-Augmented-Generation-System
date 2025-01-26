from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

class VectorStore:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.vector_store = Chroma(embedding_function=self.embeddings,)

    def add_documents(self, documents):
        self.vector_store.add_documents(documents)

    def retrieve(self, query: str, k: int = 4):
        return self.vector_store.similarity_search(query, k=k)