from django.urls import path
from friends12 import views

urlpatterns = [
    path('friends12/', views.ProfileList.as_view()),
    path('friends12/<int:pk>/', views.ProfileDetail.as_view()),
]