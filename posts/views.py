from django.views.generic import ListView,DetailView
from account.models import User
from account.mixins import AuthorAccessMixin
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
# from django.http import HttpResponse
from .models import Article
# Create your views here.
from .models import Category,Article,ArticleHit
from django.db.models import Q
# def home(request):
#     articles_list = Article.objects.published()
#     paginator = Paginator(articles_list, 4)
#     page_number = request.GET.get("page")
#     articles = paginator.get_page(page_number)
#     context = {
#         "articles": articles,
#     }
#     return render(request,'home.html',context)
class ArticleList(ListView):
    queryset = Article.objects.published()
    paginate_by = 4
    context_object_name = 'articles'
    template_name = 'article_list.html'
    # model = Article
# def detail(request,slug):
#     context = {
#         "article": get_object_or_404(Article.objects.published(), slug=slug)
#     }
#     return render(request,'details.html',context)
class ArticleDetail(DetailView):
    template_name = 'details.html'
    def get_object(self):
        slug = self.kwargs.get('slug')
        article = get_object_or_404(Article.objects.published(), slug=slug)

        ip_address = self.request.user.ip_address
        if not ip_address in article.hits.all():
            article.hits.add(ip_address)

        return article

class ArticlePreview(AuthorAccessMixin, DetailView):
    template_name = 'details.html'
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk)

def about(request):
    # context = {
    #     "articles": Article.objects.filter(status="P").order_by('-published')[:3]
    # }
    return render(request,'about.html')


# def category(request,slug,page=1):
#     category = get_object_or_404(Category, slug=slug, status=True)
#     articles_list = category.articles.published()
#     paginator = Paginator(articles_list, 4)
#     articles = paginator.get_page(page)
#     context = {
#         "category": category,
#         "articles": articles
#     }
#     return render(request,'category.html',context)
class CategoryList(ListView):
    paginate_by = 4
    template_name = 'category.html'
    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug,)
        return category.articles.published()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class AuthorList(ListView):
    paginate_by = 4
    template_name = 'author_list.html'
    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username,)
        return author.articles.published()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context
class SearchList(ListView):
    paginate_by = 1
    template_name = 'search_list.html'
    def get_queryset(self):
        search = self.request.GET.get('q')
        return Article.objects.filter(Q(description__icontains=search) | Q(title__icontains=search))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        return context