from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('发布日期')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,default=1)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)