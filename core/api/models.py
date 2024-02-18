from django.db import models


class MoneyImageModel(models.Model):
    image_file = models.ImageField(upload_to='api/post_images')

