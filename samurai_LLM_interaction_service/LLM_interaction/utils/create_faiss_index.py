import os
import traceback
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()
MY_OPENAI_API_KEY = os.getenv('openai_api_key')


def chunk_text(text, chunk_size=1500, overlap=100):
    try:
        if isinstance(text, bytes):
            text = text.decode("utf-8")
        print("Input text:", text)

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
        chunks = text_splitter.split_text(text)
        return chunks
    except Exception:
        print("An error occurred while chunking text.")
        traceback.print_exc()
        return []


def create_faiss_index(file_content, request_id):
    try:
        chunks = chunk_text(file_content)

        embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=MY_OPENAI_API_KEY)

        vector_store = FAISS.from_texts(chunks, embedding=embeddings)

        embeddings_dir = "Embeddings"
        os.makedirs(embeddings_dir, exist_ok=True)

        faiss_index_name = str(request_id)
        savedir = os.path.join(embeddings_dir, faiss_index_name)
        vector_store.save_local(folder_path=savedir, index_name=faiss_index_name)

        return faiss_index_name

    except Exception as e:
        return None