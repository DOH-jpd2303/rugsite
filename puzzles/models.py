from django.db import models
import datetime
from django.utils import timezone

# A class for each puzzle question
class Question(models.Model):
	question_title = models.CharField(max_length = 100)
	question_text = models.TextField(max_length = 2000)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return(self.question_title)
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days = 31)
	
class Player(models.Model):
	username = models.CharField(max_length = 100)
	created_on = models.DateTimeField('account created on', auto_now_add = True)
	def __str__(self):
		return self.username
	
class Submissions(models.Model):
	player_id = models.ForeignKey(Player, on_delete = models.CASCADE)
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	submission_date = models.DateTimeField('submission date', auto_now_add = True, blank = True)
	answer = models.CharField(max_length = 1000)
	correct = models.IntegerField(default=0)
	def __str__(self):
		return self.correct
	

