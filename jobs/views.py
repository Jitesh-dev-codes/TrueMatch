from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from .models import Job, Feedback
from .serializers import JobSerializer, FeedbackSerializer
from .match_jobs import extract_text_from_pdf, calculate_match_score

class JobList(generics.ListAPIView):
    serializer_class = JobSerializer
    
    def get_queryset(self):
        # Fetch only active jobs, ordered by newest first
        return Job.objects.filter(is_active=True).order_by('-posted_at')

class SubmitFeedback(generics.CreateAPIView):
    serializer_class = FeedbackSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ResumeMatchView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        resume_file = request.FILES.get('resume')
        
        if not resume_file:
            return Response({"error": "No resume file provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        resume_text = extract_text_from_pdf(resume_file)
        if not resume_text:
            return Response({"error": "Could not extract text from PDF"}, status=status.HTTP_400_BAD_REQUEST)
        
        score = calculate_match_score(resume_text, job.description)
        
        return Response({
            "job_title": job.title,
            "company": job.company_name,
            "match_score": score
        }, status=status.HTTP_200_OK)