from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(blank=True, upload_to = 'uploaded_files/') # pillow 설치 필요.
    image = models.ImageField(blank=True)