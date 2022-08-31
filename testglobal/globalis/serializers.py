from pyexpat import model
from rest_framework import serializers

from .models import *

class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'


class TextbookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Textbook
        fields = '__all__'

