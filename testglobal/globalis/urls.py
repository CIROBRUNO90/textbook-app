from django.urls import path

from .views import *

app_name='globalis_app'

urlpatterns = [
    path(
        'professor/',
        ProfessorView.as_view(),
        name='professor_view'),
    path(
        'subject/',
        SubjectView.as_view(),
        name='subject_view'),        
    path(
        'textbook/',
        TextBookView.as_view(),
        name='textbook_delete'),                
]