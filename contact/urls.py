
from django.urls import path
# Internal
from .views import ContactCreateAPIView


app_name = 'contact'

urlpatterns = [
    path('contact/', ContactCreateAPIView.as_view(), name='contact-create'),
]
