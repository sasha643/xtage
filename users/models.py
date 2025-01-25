

'''
from neomodel import StructuredNode, StringProperty, RelationshipTo
from django.contrib.auth.hashers import make_password

class User(StructuredNode):
    username = StringProperty(unique_index=True, required=True)
    email = StringProperty(unique_index=True, required=True)
    password = StringProperty(required=True)
    @property
    def saved_places(self):
        from places.models import Place
        return RelationshipTo(Place, "SAVED")

    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

    def check_password(self, password):
        from django.contrib.auth.hashers import check_password
        return check_password(password, self.password)
'''


from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add any custom fields here if needed
    # The default fields (username, email, password, etc.) are already available through AbstractUser

    def __str__(self):
        return self.username


