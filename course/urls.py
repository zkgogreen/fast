from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.index, name='index'),
    path('user/', include(('user.urls', 'user'), namespace='user')),
    path("begin/", views.begin, name='begin'),
    path("delete/", views.delall),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
