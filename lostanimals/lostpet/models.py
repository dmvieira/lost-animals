from django.db import models
from django_google_maps import fields as map_fields

# Create your models here.


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Pet(models.Model):

    SPECIES_CHOICE = (('CAT', 'gato'),
                      ('DOG', 'cachorro'))

    name = models.CharField(max_length=300)
    species = models.CharField(max_length=3,
                               choices=SPECIES_CHOICE)
    photo = models.ImageField(upload_to=get_image_path)

    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)