from django.db import models

class Pokemon(models.Model):
    pokeid = models.TextField(default="0")
    name = models.CharField(max_length=100)
    url_link = models.URLField(default="https://play.pokemonshowdown.com/teambuilder")
    height = models.TextField(default="0")
    weight = models.TextField(default="0")
    abilities = models.TextField(default="0")
    types = models.TextField(default="0")
    moves = models.TextField(default="0")
    stats = models.TextField(default="0")
    sprites = models.TextField(default="0")
    base_experience = models.TextField(default="0")
    
    def __str__(self):
        return self.name