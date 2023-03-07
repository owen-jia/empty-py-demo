from django.contrib import admin
from .models import Question
from .models import Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
