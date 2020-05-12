from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


#telling admin that Question objects have an admin interface
class QuestionAdmin(admin.ModelAdmin):
    #first element of each tuple in fieldsets is the title of the fieldset
    #below is customizing the admin change list
    fieldsets = [(None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInLine]
    
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date']
    #this adds a search box
    search_fields = ['question_text']

#the pattern to follow is creating a model admin class
#then pass it as the second argument to admin.site.register()
admin.site.register(Question, QuestionAdmin)
