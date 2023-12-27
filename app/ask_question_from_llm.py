
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI


from consts import FAIS_STORAGE


def ask_question_from_llm(question: str) -> str:
    print(f"generating answer used saved embeddings {FAIS_STORAGE}")
    embeddings = OpenAIEmbeddings(show_progress_bar=True, retry_min_seconds = 60, chunk_size=3)
    loaded_vectorstore = FAISS.load_local(FAIS_STORAGE, embeddings) 
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=0), chain_type="stuff", retriever=loaded_vectorstore.as_retriever()
    )
    return qa.run(question)
