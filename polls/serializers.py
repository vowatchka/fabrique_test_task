from rest_framework import serializers

from .models import Poll, Question, Choice, Answer


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ("id", "choice_text", "question")

    def validate_question(self, question):
        if question.question_type == "text":
            raise serializers.ValidationError("choices not allowed for questions with text answer")
        return question


class QuestionSerializer(serializers.ModelSerializer):
    choices = serializers.SerializerMethodField("get_choices", read_only=True)

    class Meta:
        model = Question
        fields = ("id", "question_text", "question_type", "choices", "poll")

    def get_choices(self, obj):
        return ChoiceSerializer(obj.choices, many=True).data


class PollSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField("get_questions", read_only=True)

    class Meta:
        model = Poll
        fields = ("id", "title", "description", "start_date", "end_date", "questions")

    def get_questions(self, obj):
        return QuestionSerializer(obj.questions, many=True).data


class AnswerChoicesSerializer(serializers.Serializer):
    choice = serializers.IntegerField()


class AnswersSerializer(serializers.Serializer):
    question = serializers.IntegerField()
    answer_text = serializers.CharField(max_length=500, allow_blank=False, required=False)
    answer_choices = AnswerChoicesSerializer(many=True, required=False)


class PollAnswersSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    poll = serializers.IntegerField()
    answers = AnswersSerializer(many=True)

    def save(self, **kwargs):
        saved_answer = dict()

        saved_answer["customer_id"] = self.data["customer_id"]
        saved_answer["poll"] = Poll.objects.filter(id=self.data["poll"]).first()

        answers = self.data["answers"]
        for answer in answers:
            # Если ранее уже отвечали на вопрос в рамках опроса, то удаляем данный ранее ответ и будем сохранять новый
            qs = Answer.objects.filter(customer_id=self.data["customer_id"], poll__id=self.data["poll"], question__id=answer["question"])
            if qs.count() > 0:
                qs.all().delete()

            saved_answer["question"] = Question.objects.filter(id=answer["question"]).first()
            if "answer_text" in answer:
                saved_answer["answer_text"] = answer["answer_text"]
                Answer(**saved_answer).save()
            elif "answer_choices" in answer:
                answer_choices = answer["answer_choices"]
                for choice in answer_choices:
                    saved_answer["choice"] = Choice.objects.filter(id=choice["choice"]).first()
                    Answer(**saved_answer).save()

class AnswersReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"