from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pizza/', include('pizza.urls')),
    path('drinks/', include('drinks.urls')),
    path('', TemplateView.as_view(template_name="index.html")),
]

urlpatterns += staticfiles_urlpatterns()
