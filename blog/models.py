from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=264,unique_for_date='publish')
    author= models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog_posts")
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering=('-publish',)
    
    def __str__(self):
        return self.title
    
    def get_abolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])
    

