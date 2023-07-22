from django.urls import path 
from . import views
from rest_framework.authtoken.views import obtain_auth_token
  
urlpatterns = [ 
    path('', views.index, name="home"),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('menu/<int:pk>', views.MenuDetailView.as_view(), name='menu'),
    path('api-token-auth', obtain_auth_token)
]