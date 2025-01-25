
'''
from neomodel import StructuredNode, StringProperty, FloatProperty, RelationshipTo
from django.contrib.auth.models import User

class Place(StructuredNode):
    name = StringProperty(required=True)
    address = StringProperty()
    latitude = FloatProperty()
    longitude = FloatProperty()
    photo_reference = StringProperty()
    saved_by = RelationshipTo('User', 'SAVED_BY')
'''

# models.py (in your places app)

from django.conf import settings
from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    photo_reference = models.CharField(max_length=255, null=True)
    
    # Update the saved_by field to use settings.AUTH_USER_MODEL
    saved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # This will dynamically reference the custom User model
        on_delete=models.CASCADE,
        related_name='saved_places',
        null=True
    )

    def __str__(self):
        return self.name
