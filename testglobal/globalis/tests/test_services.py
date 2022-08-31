from re import sub
from unicodedata import name
import pytest

from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse

from ..models import *


@pytest.mark.django_db
class TestAdminServices(APITestCase):


    def test_create_professor(self):

        data = {
            'first_name': 'test_name',
            'last_name': 'test_last_name',
            'age': 31
        }    

        resp = self.client.post(reverse('globalis_app:professor-list'), data, format='json')     
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)         
        self.assertEqual(resp.data['first_name'], data['first_name'])
        self.assertEqual(resp.data['last_name'], data['last_name'])
        self.assertEqual(resp.data['age'], data['age'])


    def test_create_subject(self):

        data = {
            'name': 'test_subject'
        }    

        resp = self.client.post(reverse('globalis_app:subject-list'), data, format='json')     
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)         
        self.assertEqual(resp.data['name'], data['name'])


    def test_create_textbook(self):

        subject = Subject.objects.create(
            name='test_textbook'
        )

        author = Professor.objects.create(
            first_name ='test_name_textbook',
            last_name='test_last_name_textbook',
            age = 31            
        )

        data = {
            'title': 'test_name',
            'subject': subject.id,
            'authors': [author.id]
        }    

        resp = self.client.post(reverse('globalis_app:textbook-list'), data, format='json')     
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)         
        self.assertEqual(resp.data['title'], data['title'])
        self.assertEqual(resp.data['subject'], data['subject'])
        self.assertEqual(resp.data['authors'][0], data['authors'][0])
