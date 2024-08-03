from django.db import models
from mongoengine import Document, StringField

class Image(models.Model):
    title = models.CharField(max_length=255)
    url=models.URLField(default='https://cdn-1.webcatalog.io/catalog/wext/wext-icon-filled-256.png?v=1714780999610')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class User(Document):
    username=StringField(required=True, unique=True)
    password=StringField(required=True)