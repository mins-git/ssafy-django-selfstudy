from django.urls import path
from . import views


urlpatterns = [
    path('libraries/', views.book_list),
    path('libraries/<int:book_pk>/', views.book_detail),
    path('libraries/<int:book_pk>/review/', views.create_review),
    path('libraries/review/<int:review_pk>/', views.review_detail),
    path('libraries/review/', views.review),
]
