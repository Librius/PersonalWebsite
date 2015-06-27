from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.name

class Article(models.Model):
    category = models.ForeignKey(Category)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    text = models.TextField()
    views = models.IntegerField(default=0)

    def __unicode__(self):      # For Python 2, use __str__ on Python 3
        return self.title