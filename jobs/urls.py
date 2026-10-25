from django.urls import path
from .views import JobList, SubmitFeedback, ResumeMatchView

urlpatterns = [
    path('jobs/', JobList.as_view(), name='job-list'),
    path('feedback/', SubmitFeedback.as_view(), name='submit-feedback'),
    path('match/<int:job_id>/', ResumeMatchView.as_view(), name='resume-match'),
]