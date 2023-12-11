from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    image_url = models.URLField()
    height = models.TextField(default="0")
    weight = models.TextField(default="0")
    pokeid = models.PositiveIntegerField(default=0)
    abilities = models.Field()
    types = models.TextField(default="0")
    moves = models.TextField(default="0")
    stats = models.TextField(default="0")
    sprites = models.TextField(default="0")
    base_experience = models.TextField(default="0")
    def __str__(self):
        return self.name