from django.contrib import admin

# Register your models here.

from .models import Professor, Subject, Textbook

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age')
    list_filter = ('first_name', 'last_name', 'age')
    search_fields = ('first_name', 'last_name', )
    readonly_fields = ('id',)
    list_display_links = ('first_name',)    

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name', )
    search_fields = ('name', )
    readonly_fields = ('id',)
    list_display_links = ('name',)        

@admin.register(Textbook)
class TextBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subject')
    list_filter = ('title', 'subject')
    search_fields = ('title', 'subject', )
    readonly_fields = ('id',)
    list_display_links = ('title',)            

