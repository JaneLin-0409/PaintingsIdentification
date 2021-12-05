"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from djangoproject import views
from django.conf.urls import url, include
from django.urls import path


urlpatterns = [
    path('', views.page1, name='Home'),
    path('2', views.page2, name='person'),
    path('3', views.page3, name='family'),
    path('4', views.page4, name='trip'),
    path('5', views.page5, name='map'),
    path('6', views.page6, name='photo'),
    path('7', views.page7, name='photo'),
    path('8', views.page8, name='photo'),
    path('9', views.page9, name='photo'),
    path('admin/', admin.site.urls),
    url(r'^sims/', include('sims.urls')),
    # path('page/<int:article_id>', views.page, name="Page"),
    # path('api/', include(('index.urls', 'index'), namespace='Index')),
    re_path(r'.*?', views.redirect_home, name='reHome'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
