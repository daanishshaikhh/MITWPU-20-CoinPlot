# coinplot_app/urls.py
from django.urls import path
from .views import index, generate_graph

urlpatterns = [
    path('', index, name='index'),
    path('generate_graph/', generate_graph, name='generate_graph'),
]