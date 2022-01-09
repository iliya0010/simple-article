from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from articles.views import ArticleListView

urlpatterns = [
    path("ckeditor/", include("ckeditor_uploader.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path("", ArticleListView.as_view(), name="list"),
    path("admin/", admin.site.urls),
    path("article/", include("articles.urls"), name="article"),
)
