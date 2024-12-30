from django.urls import path
from .views import GenerateQuizView, ChatWithContentView, GenerateSummaryView, ConvertToArticleView

urlpatterns = [
    path('generate-quiz/', GenerateQuizView.as_view(), name='generate-quiz'),
    path('chat-with-content/', ChatWithContentView.as_view(), name='chat-with-content'),
    path('generate-summary/', GenerateSummaryView.as_view(), name='generate-summary'),
    path('convert-to-article/', ConvertToArticleView.as_view(), name='convert-to-article'),
]
