from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import Poll, Question, Choice, Answer
from .serializers import PollSerializer, QuestionSerializer, ChoiceSerializer, PollAnswersSerializer, AnswersReportSerializer
from .schemas import poll_answers


class PollList(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def get_queryset(self):
        active = self.request.query_params.get("active", "false").lower()
        if active == "true":
            return Poll.objects.filter(end_date__isnull=True).all()
        return Poll.objects.all()

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter(
            name="active",
            in_=openapi.IN_QUERY,
            description="Получить только активные опросы",
            type=openapi.TYPE_BOOLEAN,
        )
    ], operation_summary="Получить список опросов")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Создать новый опрос")
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PollDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    @swagger_auto_schema(operation_summary="Получить опрос")
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Редактировать опрос")
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Удалить опрос")
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class QuestionList(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @swagger_auto_schema(operation_summary="Получить список вопросов")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Создать новый вопрос")
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class QuestionDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @swagger_auto_schema(operation_summary="Получить вопрос")
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Редактировать вопрос")
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Удалить вопрос")
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ChoiceList(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    @swagger_auto_schema(operation_summary="Получить список вариантов ответов")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Создать новый вариант ответа")
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ChoiceDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    @swagger_auto_schema(operation_summary="Получить вариант ответа")
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Редактирвоать вариант ответа")
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Удалить вариант ответа")
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PollAnswer(APIView):
    @swagger_auto_schema(request_body=poll_answers, responses={201: poll_answers}, operation_summary="Сохранить результат опроса")
    def post(self, request):
        serializer = PollAnswersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AnswerReportList(ListModelMixin, GenericAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswersReportSerializer

    def get_queryset(self):
        customer_id = self.request.query_params.get("customer_id")
        if customer_id and customer_id.isdigit():
            return Answer.objects.filter(customer_id=int(customer_id)).all()
        return Answer.objects.all()

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter(
            name="customer_id",
            in_=openapi.IN_QUERY,
            description="ID пользователя",
            type=openapi.TYPE_INTEGER,
        )
    ], operation_summary="Статистика по опросам")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)