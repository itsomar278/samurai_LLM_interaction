from .openai_client import user_input
from ..utils.vector_similarity_search import perform_similarity_search
def convert_to_article(selected_index, user_id):
    """
    Convert the content from the video to a Medium-style article.
    """

    article_role = "You are an expert content writer and editor skilled in creating high-quality, engaging articles." \
                   " Your task is to transform the content of a YouTube video into a professional," \
                   " Medium-style article formatted in Markdown."
    prompt = '''
    Follow these guidelines: 
    Structure: Start with a captivating title and an engaging introduction. Organize the content with clear, descriptive headings and subheadings. Ensure smooth transitions between sections.
    Tone and Style: Use a professional yet conversational tone that aligns with Medium's writing style. Keep sentences concise and paragraphs short for readability.
    Content: Extract key ideas and insights from the video, ensuring the information is accurate, clear, and logically structured. Add depth and examples where necessary to enhance the reader's understanding.
    Formatting: Use Markdown syntax for headings, bold text, italics, bullet points, numbered lists, and links where appropriate. Include code blocks if technical content is involved.
    Engagement: Write an impactful conclusion and include a call-to-action if applicable (e.g., encouraging readers to explore more or reflect on the content).
    Focus on maintaining the quality and coherence of the article to match the standards of top-performing Medium posts.
    '''
    docs = perform_similarity_search(selected_index, prompt, article_role)

    context = "\n\n".join([doc.page_content for doc in docs])

    article_content = user_input(prompt, article_role, context)
    return article_content
