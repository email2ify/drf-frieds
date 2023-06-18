from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model for User instance for wildlife image and countries with a 
    default image.url.
    """
    image_filter_choices = [

        ('al', 'Algeria'),
        ('an', 'Angola'),
        ('be', 'Benin'),
        ('bo', 'Botswana'),
        ('bu', 'Burkina Faso'),
        ('ce', 'Central African Republic (CAR)'),
        ('ca', 'Cameroon'),
        ('co', 'Comoros'),
        ('con', 'Congo, Democratic Republic of the'),
        ('cong', 'Congo, Republic of the'),
        ('dj', 'Djibouti'),
        ('eq', 'Equatorial Guinea'),
        ('eg', 'Egypt'),  
        ('er', 'Eritrea'),
        ('et', 'Ethiopia'),
        ('ga', 'Gabon'),
        ('gam', 'Gambia'),
        ('gh', 'Ghana'),
        ('gu', 'Guinea'),
        ('gui', 'Guinea-Bissau'),
        ('ke', 'Kenya'),
        ('li', 'Liberia'),
        ('lib', 'Libya'),
        ('ma', 'Madagascar'),
        ('mal', 'Malawi'),
        ('mali', 'Mali'),
        ('mau', 'Mauritania'),
        ('mo', 'Morocco'),
        ('moz', 'Mozambique'),
        ('na', 'Namibia'),
        ('ni', 'Niger'),
        ('nig', 'Nigeria'),
        ('rw', 'Rwanda'),
        ('se', 'Senegal'),
        ('si', 'Sierra Leone'),
        ('so', 'Somalia'),
        ('sou', 'South Africa'),
        ('sout', 'South Sudan'),
        ('su', 'Sudan'),
        ('ta', 'Tanzania'),
        ('to', 'Togo'),
        ('tu', 'Tunisia'),
        ('ug', 'Uganda'),
        ('za', 'Zambia'),
        ('zi', 'Zimbabwe'),


    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f'{self.id} {self.title}'