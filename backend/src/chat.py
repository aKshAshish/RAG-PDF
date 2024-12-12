from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from prompt import get_prompt
from process_doc import (get_vector_store, get_embedding_model)
from constants import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT_NAME,
    AZURE_OPENAI_API_VERSION
)


def get_llm():
    llm = AzureChatOpenAI(
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        azure_deployment=AZURE_OPENAI_DEPLOYMENT_NAME,
        api_version=AZURE_OPENAI_API_VERSION,
        api_key=AZURE_OPENAI_API_KEY
    )
    return llm


def get_retriever(index_name):
    embedding_model = get_embedding_model()
    vector_store = get_vector_store(embedding_model, index_name)
    return vector_store.as_retriever(search_type="hybrid", k=7)


def get_reply(query, index_name):
    prompt = get_prompt(query)
    retriever = get_retriever(index_name)
    llm = get_llm()

    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    response = ''.join([chunk for chunk in rag_chain.stream(query)])

    return response

# Test
# print(get_reply("What is Google File System?", 'gfspdf-index'))