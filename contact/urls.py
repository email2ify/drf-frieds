from django.urls import path
from .views import contactform


app_name = 'contact'

urlpatterns = [
    path('contact/', contactform.as_view(), name='contact-form'),
    ]