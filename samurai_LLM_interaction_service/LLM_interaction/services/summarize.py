from .openai_client import user_input
from ..utils.vector_similarity_search import perform_similarity_search


def generate_summary(selected_index, user_id, summary_length, additional_notes):
    """
    Generate a summary based on the video content tailored to the user's request.
    """

    summary_generator_role = "You are an expert summarizer specializing in condensing YouTube video transcripts " \
                             "into concise, coherent summaries."

    prompt = f'''
    Based on the provided video transcript, generate a summary with the following requirements:
    - The summary should be no longer than {summary_length} words.
    - The summary should capture the key ideas, facts, and themes of the video content.
    - Incorporate any relevant insights or preferences provided in the additional notes: {additional_notes}.
    - The summary should be clear, concise, and provide an overall understanding of the video.

    Use the following format for the summary:
    "Summary text here"

    Ensure that:
    - The summary captures the essence of the video in a way that makes sense without the full transcript.
    - All key ideas should be included while omitting unnecessary details.
    - The summary should be well-structured and easy to understand.
    '''

    docs = perform_similarity_search(selected_index, prompt, summary_generator_role)

    context = "\n\n".join([doc.page_content for doc in docs])

    summary_text = user_input(prompt, summary_generator_role, context)
    return summary_text
