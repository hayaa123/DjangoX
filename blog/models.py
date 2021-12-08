from django.db import models
from django.db.models import deletion
from django.db.models.base import Model
from django.contrib.auth import get_user_model
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=62)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(get_user_model(),on_delete=deletion.CASCADE)

    def __str__(self) :
        return self.title