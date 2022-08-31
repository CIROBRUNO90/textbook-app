from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
import rest_framework.mixins as mixins

from .models import *
from .serializers import *

class ProfessorViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():
            self.perform_update(serializer)        
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class SubjectViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)    

        if serializer.is_valid():
            self.perform_update(serializer)        
        return Response(serializer.data)            

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class TextBookViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    queryset = Textbook.objects.all()
    serializer_class = TextbookSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)    

        if serializer.is_valid():
            self.perform_update(serializer)        
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
