from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from blog.wrappers import render_response
from django.contrib.auth.decorators import login_required
from blog.posts.models import ArticleForm

def index(request):
    return render_response(request, 'index.html')

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ArticleForm()
    return render_response(request, 'create-article.html', {'form': form,})