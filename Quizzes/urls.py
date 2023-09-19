from django.urls import path
from Quizzes.views import health_check


urlpatterns = [
    path('', health_check, name='health_check'),
]
