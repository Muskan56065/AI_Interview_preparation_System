
from django.shortcuts import render
from .models import InterviewQuestion


def question_list(request):

    questions = InterviewQuestion.objects.filter(is_active=True)

    selected_role = request.GET.get('role', '')
    selected_topic = request.GET.get('topic', '')
    selected_difficulty = request.GET.get('difficulty', '')

    if selected_role:
        questions = questions.filter(job_role=selected_role)

    if selected_topic:
        questions = questions.filter(topic=selected_topic)

    if selected_difficulty:
        questions = questions.filter(difficulty=selected_difficulty)

    roles = (
        InterviewQuestion.objects
        .filter(is_active=True)
        .values_list('job_role', flat=True)
        .distinct()
    )

    topics = (
        InterviewQuestion.objects
        .filter(is_active=True)
        .values_list('topic', flat=True)
        .distinct()
    )

    context = {
        'questions': questions,
        'roles': roles,
        'topics': topics,
        'selected_role': selected_role,
        'selected_topic': selected_topic,
        'selected_difficulty': selected_difficulty,
    }

    return render(request, 'question_list.html', context)
