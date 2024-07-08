from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="news")
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "news"
        verbose_name_plural = "news"