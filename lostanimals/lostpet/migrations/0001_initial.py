# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lostpet.models
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('species', models.CharField(max_length=3, choices=[(b'CAT', b'gato'), (b'DOG', b'cachorro')])),
                ('photo', models.ImageField(upload_to=lostpet.models.get_image_path)),
                ('address', django_google_maps.fields.AddressField(max_length=200)),
                ('geolocation', django_google_maps.fields.GeoLocationField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
