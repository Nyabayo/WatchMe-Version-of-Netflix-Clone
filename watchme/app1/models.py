from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Choices for age limits and movie types
AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids'),
)

MOVIE_CHOICES = (
    ('seasonal', 'Seasonal'),
    ('single', 'Single'),
)

class CustomUser(AbstractUser):
    # Adding related_name to avoid reverse accessor clashes with the default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Custom related name to avoid clash
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Custom related name to avoid clash
        blank=True
    )
    profiles = models.ManyToManyField('Profile', blank=True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    name = models.CharField(max_length=1000)
    age_limit = models.CharField(choices=AGE_CHOICES, max_length=10)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    type = models.CharField(choices=MOVIE_CHOICES, max_length=10)
    video = models.ManyToManyField('Video')
    image = models.ImageField(upload_to='covers')
    age_limit = models.CharField(choices=AGE_CHOICES, max_length=10)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=1000)
    file = models.FileField(upload_to='movies')

    def __str__(self):
        return self.title
