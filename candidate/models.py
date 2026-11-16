from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class CandidateProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    education = models.CharField(max_length=150)

    experience = models.IntegerField(default=0)

    skills = models.TextField()

    target_role = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
