from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    fields = ['choice_text']


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields':['question_text']}),
        ('Date published',  {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]  # adds choices

    # choose which columns will be shown in panel with all questions
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # choose by what to filter data in right panel
    list_filter = ['pub_date']

    # fields by which to search
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

