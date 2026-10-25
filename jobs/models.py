from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Job(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    job_url = models.URLField(unique=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.company_name}"

    @property
    def is_fresh(self):
        return self.posted_at >= timezone.now() - timedelta(days=3)


class Feedback(models.Model):
    STATUS_CHOICES = [
        ('APPLIED', 'Applied'),
        ('REPLIED', 'Got Reply'),
        ('GHOSTED', 'Ghosted')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='feedbacks')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='APPLIED')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'job')

    def __str__(self):
        return f"{self.user.username} - {self.job.company_name}"