from django.urls import path
from .views import ArticleDetailView, SearchArticleView

app_name = "articles"

urlpatterns = [
    path("<int:pk>/", ArticleDetailView.as_view(), name="detail"),
    path("search/", SearchArticleView.as_view(), name="search_results"),
]
