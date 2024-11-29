from .openai_client import user_input
from ..utils.vector_similarity_search import perform_similarity_search


def chat_with_content(selected_index, user_id, user_query, chat_history, additional_notes):
    """
    Chat with the content from the YouTube video content, while taking into
     consideration the chat history into the current context.
    """

    chat_role = "You are a helpful assistant who answers questions based on the provided video or document" \
                " content. You also take into account the ongoing conversation history."

    # Prepare the context by combining the video/document content with the chat history
    prompt = f'''
    Based on the video transcript and the following conversation history, answer the user's query:

    Chat History:
    {chat_history}

    User Query: {user_query}

    Additional Notes: {additional_notes}

    Provide a helpful, informative, and relevant response. Ensure that the response is coherent with the conversation and the content being discussed.
    '''

    docs = perform_similarity_search(selected_index, prompt, chat_role)

    context = "\n\n".join([doc.page_content for doc in docs])

    response = user_input(prompt, chat_role, context)

    updated_chat_history = chat_history + f"\nUser: {user_query}\nAssistant: {response}"

    return response, updated_chat_history
