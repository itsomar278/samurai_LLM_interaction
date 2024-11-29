import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings , OpenAI
import openai

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def gpt_4_generate(messages):
    """
    Function to generate a response using GPT-4 based on a list of messages.
    """
    return openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=1.0,
        max_tokens=2000,
    )


def get_embeddings():
    """
    Function to get OpenAI embeddings.
    """
    embeddings = OpenAIEmbeddings(
        model="text-embedding-ada-002",
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    return embeddings


def user_input(user_question, role, docs):
    """
    Handle user input by performing similarity search and generating a response.
    """
    messages = [
        {
            "role": "system",
            "content": f"{role}"
        },
        {
            "role": "user",
            "content": f"Context documents: {docs}. Question: {user_question}"
        }
    ]

    response = gpt_4_generate(messages)
    response_text = response.choices[0].message.content

    return response_text
