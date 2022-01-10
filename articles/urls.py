from django.urls import path
from .views import ArticleDetailView, SearchArticleView, ArticleListView

urlpatterns = [
    path("search/", SearchArticleView.as_view(), name="search_results"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="detail"),
    path("", ArticleListView.as_view(), name="list"),
]
