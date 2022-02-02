from django.contrib import admin
from .models import Question, Player, Submission

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields': ['question_title']}),
	('Question Text', {'fields': ['question_text']}),
	('Date Published', {'fields': ['pub_date']})
	]



# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Player)
admin.site.register(Submission)

