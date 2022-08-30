import imp
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView)
from rest_framework import status
from rest_framework.response import Response

from .models import *
from .serializers import *


class ProfessorView(ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView):

    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class SubjectView(ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class TextBookView(ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView):

    queryset = Textbook.objects.all()
    serializer_class = TextbookSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
