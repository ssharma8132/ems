from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.TextField(null=True, blank=True)
    status = models.CharField(default = 'inactive', max_length=10)
    creted_by = models.ForeignKey(User, on_delete='models.CASCADE', null=True,blank=True)

    start_date = models.DateTimeField(null = True, blank = True)
    end_date  = models.DateTimeField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Choice(models.Model):
    question = models.ForeignKey('poll.Question', on_delete='models.CASCADE')
    text = models.TextField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
