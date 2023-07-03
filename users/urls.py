from django.urls import path
from users import views

urlpatterns = [
    path('users/', views.User1List.as_view()),
    path('users/<int:pk>/', views.User1Detail.as_view())
]