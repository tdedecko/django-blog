from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=220)
    author = models.ForeignKey(User)
    publish_date = models.DateTimeField('date published')
    modified_date = models.DateTimeField('date modified')
    body = models.TextField()
    