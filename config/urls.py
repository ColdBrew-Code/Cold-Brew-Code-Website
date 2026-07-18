from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from django.contrib.staticfiles.storage import staticfiles_storage
from core.views import not_found

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon/favicon.ico'), permanent=False)),
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]

handler404 = not_found
