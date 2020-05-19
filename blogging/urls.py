"""blogging URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from bloggers import views as blog_v
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog_v.landing),
    path('accounts/',include('django.contrib.auth.urls')),
    path('postblog/',blog_v.post_blog),
    path('viewblog/',blog_v.view_blog),
    path('signup/',blog_v.signuppage),
    path('read_blog/',blog_v.read_blog),
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)