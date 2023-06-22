from django.urls import path, include
from django.conf import settings
from .views import (
    ArticleList,
    ArticleDetail,
    about,
    CategoryList,
    AuthorList,
    ArticlePreview,
    SearchList,
)
app_name="blog"
urlpatterns = [
# path('page/<int:page>', home, name='home'),
path('', ArticleList.as_view(), name='home'),
path('page/<int:page>', ArticleList.as_view(), name='home'),
path('article/<slug:slug>/', ArticleDetail.as_view(), name='detail'),
path('preview/<int:pk>/', ArticlePreview.as_view(), name='preview'),
path('about.html',about,name='about'),
path('category/<slug:slug>/', CategoryList.as_view(), name='category'),
path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name='category'),
path('author/<slug:username>/', AuthorList.as_view(), name='author'),
path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name='author'),
path('search/', SearchList.as_view(), name='search'),
path('search/page/<int:page>', SearchList.as_view(), name='search'),
    ]