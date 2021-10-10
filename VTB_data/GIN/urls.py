from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.authorization, name='home'),
    path('about', views.about, name='about-project'),
  # path('authorization', views.auth, name='authorize'),
  # path('upload', views.upload, name='upload'),
    path('sorting', views.sort, name='sort-datasets'),
  # path('accounts_login', views.auth, name='accounts_login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
