from rest_framework import serializers
from .models import Job, Feedback

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'title', 'company_name', 'description', 'job_url', 'posted_at', 'is_fresh']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'user', 'job', 'status', 'created_at']
        read_only_fields = ['user']