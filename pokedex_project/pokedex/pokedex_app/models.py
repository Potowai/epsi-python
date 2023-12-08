from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()
    height = models.TextField(default="0")
    weight = models.TextField(default="0")
    pokeid = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

