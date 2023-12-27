from langchain import hub
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain.schema import StrOutputParser


from consts import FAIS_STORAGE


def format_docs(docs):
    print(f"using {len(docs)} relevant docs")
    return "\n\n".join(doc.page_content for doc in docs)


def ask_question_from_llm(question: str) -> str:
    print(f"generating answer used saved embeddings {FAIS_STORAGE}")
    embeddings = OpenAIEmbeddings(
        show_progress_bar=True, retry_min_seconds=60, chunk_size=3
    )
    loaded_vectorstore = FAISS.load_local(FAIS_STORAGE, embeddings)
    prompt = hub.pull("rlm/rag-prompt")
    llm = ChatOpenAI(temperature=0)  # other option model='gpt-4-1106-preview'
    rag_chain = (
        {
            "context": loaded_vectorstore.as_retriever(search_kwargs={"k": 10})
            | format_docs,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain.invoke(question)
