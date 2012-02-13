from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from blog.wrappers import render_response
from blog.decorators import staff_only
from django.contrib import messages
from blog.posts.models import Article, ArticleForm

def index(request):
    all_articles = Article.objects.all().order_by('-publish_date')
    paginator = Paginator(all_articles, 3)
    page = request.GET.get('page')
    try:
        articles_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles_list = paginator.page(paginator.num_pages)
    return render_response(request, 'index.html', {'articles' : articles_list})

def article(request, slug):
    selected_article = get_object_or_404(Article, slug=slug)
    return render_response(request, 'article.html', {'article' : selected_article})

@staff_only
def edit_article(request, slug=None):
    if slug is None: # New Article
        success_message = 'Your article was created successfully!'
        selected_article = Article(author=request.user)
    else: # Edit existing article
        success_message = 'Your article was edited successfully!'
        selected_article = get_object_or_404(Article, slug=slug)
        if selected_article.author != request.user:
            raise HttpResponseForbidden()
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=selected_article)
        if form.is_valid(): 
            new_article = form.save()
            messages.info(request, success_message)
            return HttpResponseRedirect(reverse('article', args=[new_article.slug]))
    else:
        form = ArticleForm(instance=selected_article)
    return render_response(request, 'edit-article.html', {'form': form,})

@staff_only
def delete_article(request, slug=None):
    selected_article = get_object_or_404(Article, slug=slug)
    if selected_article.author != request.user:
        raise HttpResponseForbidden()
    
    selected_article.delete()
    messages.info(request, 'Your article was deleted successfully!')
    return HttpResponseRedirect(reverse('index'))