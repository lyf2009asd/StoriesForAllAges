from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.story_list, name="story_list"),
    url(r'^create/', views.story_create, name="story_create"),
    url(r'^(?P<id>\d+)/edit/$', views.story_edit, name="story_edit"),
    url(r'^(?P<id>\d+)/delete/$', StoryDelete.as_view(), name="story_delete"),
    url(r'^(?P<id>\d+)/$', views.story_detail, name="story_detail"),
    url(r'^reading/$', views.reading_list, name="reading_list"),
    url(r'^reading/create/', views.reading_create, name="reading_create"),
    url(r'^reading/(?P<id>\d+)/edit/$', views.reading_edit, name="reading_edit"),
    url(r'^reading/(?P<id>\d+)/delete/$', views.reading_delete, name="reading_delete"),
    url(r'^reading/(?P<id>\d+)/$', views.reading_detail, name="reading_detail"),
    url(r'^rdercreate/', views.reader_create, name="reader_create"),
    url(r'^reader/(?P<id>\d+)/$', views.reader_detail, name="reader_detail"),
    url(r'^topread/', views.top_read, name="top_read"),
]