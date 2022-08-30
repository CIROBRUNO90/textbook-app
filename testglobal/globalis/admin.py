from django.contrib import admin

# Register your models here.

from .models import Professor, Subject, Textbook

admin.site.register(Professor)
admin.site.register(Subject)
admin.site.register(Textbook)


