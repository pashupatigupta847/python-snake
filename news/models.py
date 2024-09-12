from django.db import models
from django.contrib.auth.models import User

"""
Category model
"""
class Category(models.Model):
    """ This is news category used in news"""
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ return the class name"""
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

"""
News model
"""
class News(models.Model):
    """ This model is used to store news"""
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="news_category")
    image = models.ImageField(upload_to="news")
    description = models.TextField()
    is_editorial =  models.BooleanField(default=False)
    views_count = models.PositiveIntegerField(default=0)
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="newsrepoter")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "news"
        verbose_name_plural = "news"

"""
ContactUs model
"""
class ContactUs(models.Model):
    """this model is used to stored contactus model"""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=255)
    phone = models.PositiveBigIntegerField()
    feedback_message = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"\

"""
Subcribe model
"""   
class Subcribe(models.Model):
    """ This model stores the email address of subcribe"""
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Subcribe"
        verbose_name_plural = "Subcribe"


"""
social media
"""
class SocialMedia(models.Model):
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()

    def __str__(self):
        return "Social Media"

    class Meta:
        verbose_name = "SocialMedia"
        verbose_name_plural = "SocialMedia"