import nested_admin

from django.contrib import admin

from .models import Poll, Question, Choice


class ChoiceInline(nested_admin.NestedStackedInline):
    model = Choice
    extra = 0


class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 0

    inlines = (ChoiceInline,)


@admin.register(Poll)
class PollAdmin(nested_admin.NestedModelAdmin):
    readonly_fields = ("start_date",)
    list_display, list_display_links = (("title", "description", "start_date", "end_date"),) * 2

    inlines = (QuestionInline,)


@admin.register(Question)
class QuestionAdmin(nested_admin.NestedModelAdmin):
    list_display, list_display_links = (("question_text", "question_type", "poll"),) * 2

    inlines = (ChoiceInline,)


@admin.register(Choice)
class ChoiceAdmin(nested_admin.NestedModelAdmin):
    list_display, list_display_links = (("choice_text", "question"),) * 2
