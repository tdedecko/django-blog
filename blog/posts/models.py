from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.forms import ModelForm, ValidationError

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
        # Ensure unique slugs
        unique_slug_message = "Article title is similar to existing articles. Try something new!"
        if self.cleaned_data.has_key('title'):
            slug = slugify(self.cleaned_data['title'])
            articles_with_same_slug = Article.objects.filter(slug=slug).exclude(id=self.instance.id)
            if articles_with_same_slug:
                raise ValidationError(unique_slug_message)
        return self.cleaned_data
    
    class Meta:
        model = Article
        fields = ('title', 'body')
    