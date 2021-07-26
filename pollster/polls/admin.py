from django.contrib import admin
from polls.models import Question, Choice

#site header
admin.site.site_header = "Pollster Admin"

#site title
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster Admin area"


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}), ]
    inlines = [ChoiceInLine]

admin.site.register(Question,QuestionAdmin)

