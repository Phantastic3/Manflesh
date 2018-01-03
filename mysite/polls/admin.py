from django.contrib import admin

from .models import Question, List, Word

admin.site.register(Question)
admin.site.register(List)
admin.site.register(Word)