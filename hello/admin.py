from django.contrib import admin
from .models import Citations, Lectures, Lecturer, Presentations, ResearchPaper
# Register your models here.
from django import forms


@admin.register(Citations)
class CitationsAdmin(admin.ModelAdmin):
    list_display = ('body', 'author')
    list_filter = ('author', 'body')
    search_fields = ('author', 'body')

@admin.register(Lectures)
class LecturesAdmin(admin.ModelAdmin):
    list_display = ('title', 'faculty','lecturer', 'semester', 'typeOfStudies')
    list_filter = ('faculty', 'typeOfStudies', 'semester', 'lecturer')
    search_fields = ('faculty', 'typeOfStudies', 'semester', 'lecturer')

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('scientificType', 'firstname', 'secondname')
    list_filter = ('scientificType', 'secondname')
    search_fields = ('firstname', 'secondname')

@admin.register(Presentations)
class PresentationsAdmin(admin.ModelAdmin):
    list_display = ('title', 'eventName', 'year')
    list_filter = ('eventName', 'year')

@admin.register(ResearchPaper)
class ResearchPaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'journal', 'year', 'submitted', 'inpress', 'published')
    list_filter = ('year', 'submitted', 'inpress', 'published')