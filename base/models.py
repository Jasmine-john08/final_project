from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    category_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category_name

status_choice=[
    ('draft','Draft'),('published','Published')
]

class Article(models.Model):
    title=models.CharField(max_length=1000)
    slug=models.SlugField(max_length=1000)
    short_description=models.TextField(max_length=10000)
    detail_description=models.TextField(max_length=10000)
    author=models.ForeignKey(to=User,on_delete=models.CASCADE)
    category=models.ForeignKey(to=category,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='contentcanvas/media')
    status=models.CharField(choices=status_choice)
    is_trending=models.BooleanField(default=False)