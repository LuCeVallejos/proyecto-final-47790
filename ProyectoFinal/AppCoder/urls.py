from django.urls import path
from AppCoder.views import cursos_view, inicio_view

urlpatterns = [
    path('cursos/', cursos_view),
    path('inicio/', inicio_view),
]
