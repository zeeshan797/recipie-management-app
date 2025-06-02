from django.db import models

# Create your models here.
class Recipie(models.Model):
    recipie_name = models.CharField(max_length=50)
    recipie_ingrediants = models.TextField()
    recipie_description = models.TextField()
    recipie_image = models.FileField(upload_to='recipie_img/', default='default.jpg')

    def __str__(self):
        return self.recipie_name