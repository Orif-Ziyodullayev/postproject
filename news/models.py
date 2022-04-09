from django.db import models

# Create your models here.
from django.urls import reverse


class Post(models.Model):
    date = models.DateTimeField(auto_now=False,auto_now_add=False)
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=200,null=True,blank=True)
    info = models.TextField()
    author = models.CharField(max_length=50)
    

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.pk)])
