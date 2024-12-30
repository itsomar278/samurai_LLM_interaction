import markdown
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.chat_with_content import chat_with_content
from .services.summarize import generate_summary
from .services.youtube2Medium import convert_to_article
from .services.QuizMe import generate_quiz


class GenerateQuizView(APIView):
    def post(self, request):
        data = request.data
        try:
            quiz = generate_quiz(
                selected_index=data["selected_index"],
                user_id=data["user_id"],
                total_questions=data["total_questions"],
                hard_questions=data["hard_questions"],
                additional_notes=data.get("additional_notes", "")
            )
            return Response({"quiz": quiz}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ChatWithContentView(APIView):
    def post(self, request):
        data = request.data
        try:
            response, updated_chat_history = chat_with_content(
                selected_index=data["selected_index"],
                user_id=data["user_id"],
                user_query=data["user_query"],
                chat_history=data.get("chat_history", ""),
                additional_notes=data.get("additional_notes", "")
            )
            return Response({"response": response, "chat_history": updated_chat_history}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class GenerateSummaryView(APIView):
    def post(self, request):
        data = request.data
        try:
            summary = generate_summary(
                selected_index=data["selected_index"],
                user_id=data["user_id"],
                summary_length=data["summary_length"],
                additional_notes=data.get("additional_notes", "")
            )
            return Response({"summary": summary}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ConvertToArticleView(APIView):
    def post(self, request):
        data = request.data
        try:
            article_md = convert_to_article(
                selected_index=data["selected_index"],
                user_id=data["user_id"]
            )

            return Response(
                article_md,
                status=status.HTTP_200_OK,
                content_type='text/markdown'
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

