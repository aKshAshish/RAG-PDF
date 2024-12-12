import os
from dotenv import load_dotenv

load_dotenv()

# Constants
PATH_TO_UPLOADS = '../data'
ALLOWED_EXTENSIONS = ['pdf']
UPLOAD_FOLDER = 'UPLOAD_FOLDER'

# Initialize Azure Search db constants
VECTOR_STORE_ENDPOINT = os.environ.get("VECTOR_STORE_ENDPOINT")
VECTORE_STORE_KEY = os.environ.get("VECTORE_STORE_KEY")
# Initialize Azure Open AI constants
AZURE_OPENAI_ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.environ.get("AZURE_OPENAI_API_KEY")
OPENAI_MODEL_NAME = os.environ.get("OPENAI_MODEL_NAME")
OPENAI_API_VERSION = os.environ.get("OPENAI_API_VERSION")
AZURE_OPENAI_EMBED_MODEL_NAME = os.environ.get("AZURE_OPENAI_EMBED_MODEL_NAME")