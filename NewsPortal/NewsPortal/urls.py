
from django.urls import path

from .views import *

urlpatterns = [
    path('news/', NewsList.as_view(), name='post_list'),
    path('news/<int:pk>/', NewsDetail.as.view(), name='post_detail'),
    path('news/create/', NewsCreate.as_view(), name='post_search'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='post_search'),
    path('news/<int:pk>/delete'), NewsDelete.as_view(), name='post_search'),
    path('articles/create/', NewsSearch.as_view(), name='post_search'),
    path('articles/<int:pk>/edit', NewsSearch.as_view(), name='post_search'),
    path('articles/<int:pk>/delete/', NewsSearch.as_view(), name='post_search')
]