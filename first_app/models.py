from django.db import models
from imagekit.models import ProcessedImageField
from django.urls import reverse

# Create your models here.
class Post(models.Model):
  title = models.TextField(blank = False, null= False)
  image = ProcessedImageField(
    upload_to = 'static/image/post',
    format = 'JPEG',
    options = {'quality' :100},
    blank = True,
    null = True,
  )

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("post detail", args=[str(self.id)])