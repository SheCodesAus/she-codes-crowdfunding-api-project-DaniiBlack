from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# example: path('projects/', views.ProjectList.as_view()), will add the view at that address
urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# created a list of patterns for the urls in our projects app whihc is one app in our crowdfunding app