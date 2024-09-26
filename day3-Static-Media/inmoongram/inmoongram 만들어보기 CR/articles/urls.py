from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.create, name= 'create'),
    # path('update/', views.update, name = 'update'),
    path('<int:pk>/', views.detail, name = 'detail'),
]
