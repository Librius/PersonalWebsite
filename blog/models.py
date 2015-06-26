from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.name

class Article(models.Model):
    category = models.ForeignKey(Category)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    text = models.TextField()
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):      # For Python 2, use __str__ on Python 3
        return self.title