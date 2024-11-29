from ..services.openai_client import get_embeddings
from langchain_community.vectorstores import FAISS
import os


def perform_similarity_search(selected_index, user_question, role, k=7):
    """
    Perform the similarity search using FAISS and enriched user question ( role + prompt).
    """
    enriched_question = f"{role}\nUser Question: {user_question}"

    index_path = f"C:\\Users\\omar\\PycharmProjects\\samurai_LLM_interaction\\samurai_LLM_interaction_service\\Embeddings\\{selected_index}"
    embeddings = get_embeddings()
    new_db = FAISS.load_local(folder_path=index_path,index_name=selected_index, embeddings=embeddings,
                              allow_dangerous_deserialization=True)

    docs = new_db.similarity_search(enriched_question, k=k)
    return docs
