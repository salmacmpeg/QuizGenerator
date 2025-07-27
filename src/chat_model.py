from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory


class ChatModel:
    def __init__(self, vectorstore, model_name: str = 'llama3.2'):
        self.llm_model = Ollama(model=model_name)
        self.vectorstore = vectorstore
        self.retriever = self.retriever = self.vectorstore.as_retriever()
        self.chain = None
        self.mode = None

    def init_chat(self, mode: str = 'memoryless'):
        if mode == 'memoryless':
            self.mode = mode
            self.chain = RetrievalQA.from_chain_type(self.llm_model,
                                                     chain_type="stuff",
                                                     retriever=self.retriever)
        else:
            self.mode = 'memory'
            memory = ConversationBufferMemory(memory_key="chat_history",
                                              output_key="answer",
                                              llm=self.llm_model,
                                              return_messages=True)
            self.chain = ConversationalRetrievalChain.from_llm(
                llm=self.llm_model,
                verbose=True,
                retriever=self.retriever,
                memory=memory)

    def get_response(self, user_message: str):
        if self.mode == 'memoryless':
            result = self.chain.invoke({"query": user_message})
            return result["result"]
        else:
            result = self.chain.invoke({"question": user_message})
            return result["answer"]
