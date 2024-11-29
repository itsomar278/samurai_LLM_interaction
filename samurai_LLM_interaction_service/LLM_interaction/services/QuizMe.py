from .openai_client import user_input
from ..utils.vector_similarity_search import perform_similarity_search


def generate_quiz(selected_index, user_id, total_questions, hard_questions, additional_notes):
    """
    Generate a quiz based on the video content tailored to the user request.
    """

    quiz_generator_role = "You are an expert quiz creator specializing in generating diverse," \
                          " engaging questions based on YouTube video transcripts."

    prompt = f'''
    Based on the provided video transcript, generate a quiz with the following requirements:
    - The quiz should have a total of {total_questions} multiple-choice questions (MCQs), each with exactly 4 options and only one correct answer.
    - Out of these, {hard_questions} questions should be marked as "hard" if the number is greater than 0. Clearly indicate the difficulty level.
    - For each question, include a mark for the correct answer.
    - The quiz should be related to the key ideas, facts, and themes of the video content.
    - Incorporate any relevant insights or preferences provided in the additional notes: {additional_notes}.

    Use the following JSON format for the quiz:
    [
        {{
            "question": "Question text here",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "correct_answer": "Option X",
            "difficulty": "hard" or "normal"
        }},
        ...
    ]

    Ensure that:
    - Hard questions focus on nuanced, complex, or less obvious aspects of the content.
    - All questions are accurate, clear, and well-structured.
    - there should be variety of the questions topics
    '''

    docs = perform_similarity_search(selected_index, prompt, quiz_generator_role)

    context = "\n\n".join([doc.page_content for doc in docs])

    quiz_questions = user_input(prompt, quiz_generator_role, context)
    return quiz_questions
