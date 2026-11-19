
from django.db import models

class InterviewQuestion(models.Model):

    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    job_role = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    question_text = models.TextField()

    # New field
    answer_text = models.TextField(blank=True, default='')

    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        default='Easy'
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_role} - {self.topic}"
