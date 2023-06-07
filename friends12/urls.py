from django.urls import path
from friends12 import views

urlpatterns = [
    path('friends12/', views.ProfileList.as_view()),
]