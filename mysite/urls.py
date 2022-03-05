from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns 
from django.conf.urls.static import static
from django.conf import settings

from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path("", views.home, name="home"),
    path("blog/", include('blog.urls')),
    path("i18n/", include("django.conf.urls.i18n")),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)