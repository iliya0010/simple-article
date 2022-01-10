from django.views.generic import DetailView, ListView
from django.utils.translation import gettext as _
from django.shortcuts import render
from .models import Article


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/article_detail.html"


class ArticleListView(ListView):

    model = Article
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        all_articles = self.model.objects.filter(status="P")
        return render(
            request,
            "articles/article_list.html",
            {
                "articles": all_articles,
            },
        )


class SearchArticleView(ListView):
    model = Article
    template_name = "articles/search_results.html"

    def get_queryset(self):
        print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFf")
        query = self.request.GET.get("q")
        object_list = Article.objects.filter(tags__name__icontains=query)
        return object_list
