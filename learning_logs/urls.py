"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # show all topics
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic
    # path('topics/(?p<topic_id>/d+)/', views.topic, name='topic')
    # or
    path('topics/<int:topic_id>/', views.topic, name='topic')
]
