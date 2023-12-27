import os

from langchain.document_loaders import TelegramChatFileLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI


from app.consts import FAIS_STORAGE


if __name__ == "__main__":
    print(f"generating answer used saved embeddings {FAIS_STORAGE}")
    embeddings = OpenAIEmbeddings(show_progress_bar=True, retry_min_seconds = 60, chunk_size=3)
    loaded_vectorstore = FAISS.load_local(FAIS_STORAGE, embeddings) 
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(), chain_type="stuff", retriever=loaded_vectorstore.as_retriever()
    )
    res = qa.run("Give me the gist of ReAct in 3 sentences")
    print(res)
