from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.forms import ModelForm

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    author = models.ForeignKey(User)
    publish_date = models.DateTimeField('date published')
    modified_date = models.DateTimeField('date modified')
    body = models.TextField()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'body')
    