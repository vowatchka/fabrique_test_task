from django.db import models


class Choice(models.Model):
    """
    Модель варианта ответа
    """
    choice_text = models.CharField(max_length=100, verbose_name="Текст варианта ответа")
    question = models.ForeignKey("Question", on_delete=models.CASCADE, verbose_name="Вопрос")

    class Meta:
        verbose_name = "вариант ответа"
        verbose_name_plural = "варианты ответов"

    def __str__(self):
        return self.choice_text[:20]


class Question(models.Model):
    """
    Модель вопроса
    """
    question_types = (
        ("text", "Ответ текстом"),
        ("radio", "Ответ с выбором одного варианта"),
        ("checkbox", "Ответ с выбором нескольких вариантов"),
    )

    question_text = models.TextField(max_length=1500, verbose_name="Текст вопроса")
    question_type = models.CharField(max_length=20, choices=question_types, default=question_types[0][0], verbose_name="Тип вопроса")
    poll = models.ForeignKey("Poll", on_delete=models.CASCADE, verbose_name="Опрос")

    class Meta:
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"

    def __str__(self):
        return self.question_text[:20] + " - " + self.question_type

    @property
    def choices(self):
        return Choice.objects.filter(question__id=self.id).all()


class Poll(models.Model):
    """
    Модель опроса
    """
    title = models.CharField(max_length=100, verbose_name="Название опроса")
    description = models.TextField(max_length=1500, blank=True, default="", verbose_name="Описание опроса")
    start_date = models.DateField(auto_now_add=True, verbose_name="Дата запуска опроса")
    end_date = models.DateField(blank=True, null=True, default=None, verbose_name="Дата окончания опроса")

    class Meta:
        verbose_name = "опрос"
        verbose_name_plural = "опросы"

    def __str__(self):
        return self.title

    @property
    def questions(self):
        return Question.objects.filter(poll__id=self.id).all()


class Answer(models.Model):
    """
    Модель ответов на опросы
    """
    customer_id = models.IntegerField(verbose_name="ID пользователя")
    poll = models.ForeignKey(Poll, on_delete=models.DO_NOTHING, verbose_name="Опрос")
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, verbose_name="Вопрос")
    choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING, null=True, verbose_name="Выбранный вариант ответа")
    answer_text = models.TextField(max_length=500, blank=True, null=True, verbose_name="Тектс ответа")

    class Meta:
        verbose_name = "ответ"
        verbose_name_plural = "ответы"

    def __str__(self):
        return self.answer_text[:20]

