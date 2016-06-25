from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [

url(r'^$', views.home, name='home'),
url(r'^login/$', views.login_user, name='login'),
url(r'^logout/$', views.logout_user, name='logout'),

#publishers
url(r'^publishers/$',views.publisher_index, name='publisher.index'),
url(r'^publishers/create/$',views.publisher_new, name='publisher.create'),
url(r'^publishers/(?P<id>\d+)/$',views.publisher_detail, name='publisher.detail'),
url(r'^publishers/(?P<id>\d+)/edit/$',views.publisher_update, name='publisher.edit'),
url(r'^publishers/(?P<id>\d+)/delete/$',views.publisher_delete, name='publisher.delete'),
#authors
url(r'^authors/$',views.author_index, name='author.index'),
url(r'^authors/create/$',views.author_new, name='author.create'),
url(r'^authors/(?P<id>\d+)/$',views.author_detail, name='author.detail'),
url(r'^authors/(?P<id>\d+)/edit/$',views.author_update, name='author.edit'),
url(r'^authors/(?P<id>\d+)/delete/$',views.author_delete, name='author.delete'),
#books
url(r'^books/$',views.book_index, name='book.index'),
url(r'^books/create/$',views.book_new, name='book.create'),
url(r'^books/(?P<id>\d+)/$',views.book_detail, name='book.detail'),
url(r'^books/(?P<id>\d+)/edit/$',views.book_update, name='book.edit'),
url(r'^books/(?P<id>\d+)/delete/$',views.book_delete, name='book.delete'),
#Issue
url(r'^issues/$',views.issue_index, name='issue.index'),
url(r'^issues/create/$',views.issue_new, name='issue.create'),

]