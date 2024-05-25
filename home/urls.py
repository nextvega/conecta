from django.urls import path
from home import views

urlpatterns =[
    # inicio
    path('', views.inicio, name="inicio"),
    path('in/', views.user, name="user"),
    path('network/', views.network, name="network"),
    path('jobs/', views.jobs, name="jobs"),



    # login
    path('login/', views.login, name="login"),
]