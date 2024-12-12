import os

from langchain.document_loaders import PyMuPDFLoader
from langchain_openai import AzureOpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.azuresearch import AzureSearch
from azure.search.documents.indexes.models import (
    SearchableField,
    SimpleField,
    SearchFieldDataType,
    SearchField
)

from constants import (
    PATH_TO_UPLOADS,
    VECTOR_STORE_ENDPOINT,
    VECTORE_STORE_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_EMBED_MODEL_VERSION,
    AZURE_OPENAI_EMBED_MODEL_NAME
)

def get_embedding_model():
    embeddings = AzureOpenAIEmbeddings(
        azure_deployment=AZURE_OPENAI_EMBED_MODEL_NAME,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_version=AZURE_OPENAI_EMBED_MODEL_VERSION,
        api_key=AZURE_OPENAI_API_KEY,
    )
    return embeddings


def initialize_vector_store(embedding_model):
    fields = [
        SimpleField(
            name="id",
            type=SearchFieldDataType.String,
            key=True,
            filterable=True,
        ),
        SearchableField(
            name="content",
            type=SearchFieldDataType.String,
            searchable=True,
        ),
        SearchField(
            name="content_vector",
            type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
            searchable=True,
            vector_search_dimensions=len(embedding_model.embed_query("Text")),
            vector_search_profile_name="myHnswProfile",
        ),
        SearchableField(
            name="metadata",
            type=SearchFieldDataType.String,
            searchable=True,
        ),
        # Additional field to store the title
        SearchableField(
            name="source",
            type=SearchFieldDataType.String,
            searchable=True,
        ),
        SearchableField(
            name="page",
            type=SearchFieldDataType.Int32,
            searchable=True
        )
    ]

    return fields

def get_vector_store(embedding_model, index_name):
    vector_store = AzureSearch(
        azure_search_endpoint=VECTOR_STORE_ENDPOINT,
        azure_search_key= VECTORE_STORE_KEY,
        index_name=index_name,
        embedding_function=embedding_model.embed_query,
    )

    return vector_store


def process_pdf_to_splits(filename):
    path = os.path.join(PATH_TO_UPLOADS, filename)
    loader = PyMuPDFLoader(path)
    # Create chunks
    chunk_size = 2000
    chunk_overlap = 200
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )

    splits = loader.load_and_split(text_splitter)
    for split in splits:
        split.metadata = {
            "source": filename,
            "page": split.metadata['page'],
            "total_pages": split.metadata['total_pages']
        }

    return splits


def index_file(filename):
    splits = process_pdf_to_splits(filename)
    embedding_model = get_embedding_model()
    initialize_vector_store(embedding_model)
    vector_store = get_vector_store(embedding_model, index_name=f'{filename.replace('.', '')}-index')

    vector_store.add_documents(splits)
    print(f'[INFO] - Document upload complete: {filename}')

