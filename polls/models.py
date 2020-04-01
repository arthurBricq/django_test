from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
     
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

# Test for the app

# Companies have names and different services, we want to be able to retrieve this from a special link

class Company(models.Model):
    name = models.CharField(max_length=200)



class Service(models.Model):
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    company = models.ForeignKey(Company, on_delete = models.CASCADE)

