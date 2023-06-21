"""
URL configuration for pr2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from Scripts.activate_this import lib
# from account import views
from django.contrib import admin
from account.views import ArticleList,ArticleCreate
from django.urls import path,include, re_path
from posts.views import ArticleList,ArticleDetail,CategoryList,Article
from django.conf import settings
from account.views import Login, Register, activate
app_name = "post"
urlpatterns = [

    path('',include('posts.urls')),
    path('', include('django.contrib.auth.urls')),
    path("login/", Login.as_view(), name="login"),
    path("register/", Register.as_view(), name="register"),
    # url(r'^signup/$', views.signup, name='signup'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$', activate, name='activate'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
    # path('account/',ArticleList.as_view()),
    path("article/create", ArticleCreate.as_view(), name="article-create"),
    path('comment/', include('comment.urls')),
]
# from django.conf.urls.static import static
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
