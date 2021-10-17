from django.urls import path

from .views import PollList, PollDetail, QuestionList, QuestionDetail, ChoiceList, ChoiceDetail, PollAnswer, AnswerReportList


urlpatterns = [
    path("polls/", PollList.as_view(), name="polls"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("questions/", QuestionList.as_view(), name="questions"),
    path("questions/<int:pk>/", QuestionDetail.as_view(), name="questions_detail"),
    path("choices/", ChoiceList.as_view(), name="choices_detail"),
    path("choices/<int:pk>/", ChoiceDetail.as_view(), name="choices_detail"),

    path("polls/answers/", PollAnswer.as_view(), name="poll_answer"),
    path("polls/answers/report/", AnswerReportList.as_view(), name="answer_report"),
]