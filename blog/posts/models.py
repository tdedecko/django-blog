from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.forms import ModelForm, ValidationError
from django.db import IntegrityError

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    author = models.ForeignKey(User)
    publish_date = models.DateTimeField('date published', auto_now_add=True)
    modified_date = models.DateTimeField('date modified', auto_now=True)
    body = models.TextField()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
            

class ArticleForm(ModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.has_key('title'):
            slug = slugify(cleaned_data['title'])
            if Article.objects.filter(slug=slug):
                raise ValidationError("Article title is similar to existing articles. Try something new!")
        return cleaned_data
    
    class Meta:
        model = Article
        fields = ('title', 'body')
    