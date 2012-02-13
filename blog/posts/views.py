from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from blog.wrappers import render_response
from django.contrib.auth.decorators import login_required
from blog.posts.models import Article, ArticleForm

def index(request):
    all_articles = Article.objects.all().order_by('-publish_date')
    return render_response(request, 'index.html', {'articles' : all_articles})

def article(request, slug):
    selected_article = get_object_or_404(Article, slug=slug)
    return render_response(request, 'article.html', {'article' : selected_article})

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=Article(author=request.user))
        if form.is_valid():
            
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ArticleForm()
    return render_response(request, 'create-article.html', {'form': form,})