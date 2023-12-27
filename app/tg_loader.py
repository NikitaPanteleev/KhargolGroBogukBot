import os
import pickle

from langchain.document_loaders import TelegramChatFileLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

from consts import FAIS_STORAGE


if __name__ == "__main__":
    print(f"Storing embeddings to {FAIS_STORAGE}")
    chat_folder = '/Users/nikita/Workspace/KhargolGroBogukBot/data/result.json'
    loader = TelegramChatFileLoader(chat_folder) 
    documents = loader.load()
    text_splitter = CharacterTextSplitter(separator="\n\n", chunk_size=512, chunk_overlap=20)
    docs = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings(show_progress_bar=True, retry_min_seconds = 60, chunk_size=3)
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(FAIS_STORAGE)
    print('SUCCESS')  
