from django.urls import path

from . import views
from .migrate import migrate_animals

urlpatterns = [
    path('animals/', views.AnimalList.as_view(), name='animal-list'),
    path('animals/specie/<str:slug>/', views.AnimalDetail.as_view(), name='animal-detail'),
    path('animals/countries/', views.CountriesWithAnimalsList.as_view(), name='countries-list'),
    path('animals/countries/<str:country>/', views.AnimalsByCountryList.as_view(), name='animals-by-country'),
    path('get_data/', migrate_animals, name='get_data'),
]
