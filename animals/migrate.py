import json
from django.http import HttpResponse
from django.utils.text import slugify
from .models import Animal


# Script to migrate data from Json to production database.
def migrate_animals(request):
    with open('animals_data.json') as file:
        animals_data = json.load(file)

    # Iterate over each animal in the data
    for animal_data in animals_data['animals']:
        # Extract the relevant fields
        name = animal_data['name']
        description = animal_data['description']
        image = animal_data['image']
        countries = animal_data['countries']
        slug = slugify(name)

        # Create a new Animal object
        animal = Animal(
            name=name,
            description=description,
            image=image,
            slug=slug,
            countries=countries
        )

        # Save the animal to the database
        animal.save()

    return HttpResponse('Data migration completed successfully.')
