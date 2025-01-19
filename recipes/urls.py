from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='recipe-home'),
    path('recipe/<int:id>/', views.recipe, name='recipe-detail'),
]
