import os
from langchain import hub
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_openai import ChatOpenAI

#load the dotenv.
load_dotenv()

class RAGSystem:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.llm = ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'), model="gpt-4o-mini")
        self.prompt = hub.pull("rlm/rag-prompt")

    def format_docs(self, docs):
        retriever_data = "\n\n".join(doc.page_content for doc in docs)
        rag_prompt = """Your task is to provide relevant information based on the user's question and respond using the given data. If the user's query cannot be answered using the provided data, respond with: 'Sorry, I did not find the relevant data."""
        return rag_prompt+retriever_data

    def generate_response(self, query: str):
        # Retrieve relevant documents
        retriever = self.vector_store.retrieve(query)

        # Create the RAG chain
        rag_chain = (
            {
                "context": RunnableLambda(lambda x: self.format_docs(retriever)),
                "question": RunnablePassthrough() 
            }
            | self.prompt  
            | self.llm 
            | StrOutputParser()
        )

        # Invoke the RAG chain with the query
        return rag_chain.invoke(query)