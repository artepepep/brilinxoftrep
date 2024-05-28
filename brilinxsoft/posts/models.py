from django.db import models
from .choices import POST_SECTIONS

class Post(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    section = models.OneToOneField(on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Post name:{self.name}, section of the post: {self.section}"


class Category(models.Model):
    name = models.CharField(max_length=105)
    