from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

def index(request):
    return render_to_response('index.html', RequestContext(request))

@login_required
def create_article(request):
    return render_to_response('create-article.html', RequestContext(request))