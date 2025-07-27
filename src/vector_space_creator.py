import os
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from src.data_loader import DataLoader


class VectorSpaceCreator:
    def __init__(
            self,
            model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
            vectore_store_name: str = "./vector_db",
            DL: DataLoader = None
            ):
        self.embedding_model = HuggingFaceEmbeddings(model_name=model_name)
        self.vectore_store_name = vectore_store_name
        self.DL = DL
        self.vectorstore = None

    def create_vector_sapce(self):
        if os.path.exists(self.vectore_store_name):
            Chroma(persist_directory=self.vectore_store_name,
                   embedding_function=self.embedding_model).delete_collection()
        if self.DL is None:
            self.DL = DataLoader()
        chunks = self.DL.get_chunks()
        self.vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding_model,
            persist_directory=self.vectore_store_name
            )
        print("Vectorstore created"
              f"with {self.vectorstore._collection.count()} documents")

    def get_vector_store(self):
        if os.path.exists(self.vectore_store_name):
            self.vectorstore = Chroma(
                persist_directory=self.vectore_store_name,
                embedding_function=self.embedding_model
            )
        else:
            self.create_vector_sapce()
        return self.vectorstore
