from django.contrib import admin
from .models import InterviewQuestion


@admin.register(InterviewQuestion)
class InterviewQuestionAdmin(admin.ModelAdmin):

    list_display = (
        'job_role',
        'topic',
        'difficulty',
        'is_active',
    )

    list_filter = (
        'job_role',
        'topic',
        'difficulty',
        'is_active',
    )

    search_fields = (
        'job_role',
        'topic',
        'question_text',
    )

    fields = (
        'job_role',
        'topic',
        'question_text',
        'answer_text',
        'difficulty',
        'is_active',
    )