from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('welcome/', views.welcome, name='welcome'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('update_simulation/', views.update_simulation, name='update_simulation'),
]