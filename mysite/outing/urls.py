from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('json/', views.json, name='json'),
    path('api/form/save', views.form_save, name='json')
]
