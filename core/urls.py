from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('404', views.not_found, name='not_found'),
    path('portfolio', views.portfolio, name='portfolio'),
]