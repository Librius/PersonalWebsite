__author__ = 'bonnie'

from django.conf.urls import patterns, url, include
from blog import views

urlpatterns = patterns('',
                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', views.index, name='blog_index'),
                       url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
                       url(r'^article/(?P<article_title_slug>[\w\-]+)/$', views.article, name='article'),
                       )
