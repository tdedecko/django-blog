from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'blog.posts.views.index', name='index'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^actions/new/post/', 'blog.posts.views.edit_article', name='create-article'),
    url(r'^posts/(?P<slug>[-\w]+)/edit/$','blog.posts.views.edit_article', name='edit-article'),
    url(r'^posts/(?P<slug>[-\w]+)/delete/$','blog.posts.views.delete_article', name='delete-article'),
    url(r'^posts/(?P<slug>[-\w]+)/$','blog.posts.views.article', name='article'),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()