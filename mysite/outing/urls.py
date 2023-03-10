from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('json/', views.json_return, name='json'),
    path('api/form/save', views.form_save, name='form'),
    path('api/form/delete', views.form_delete, name='form')
]
