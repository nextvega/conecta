from django.urls import path
from home import views

urlpatterns =[
    # inicio
    path('', views.inicio, name="inicio"),
    path('in/', views.user, name="user")
]