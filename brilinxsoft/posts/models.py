from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    section = models.ForeignKey(Section ,on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Post name:{self.name}, section of the post: {self.section}"
    