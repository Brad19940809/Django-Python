from django.db import models

# Create your models here.
class Brad(models.Model):
    title=models.CharField(max_length=255) #my blog
    category=models.CharField(max_length=50,blank=True) #blog tag
    date_time=models.DateTimeField(auto_now_add=True) #blog date
    content=models.TextField(blank=True,null=True) #blog text

    def __unicode__(self):
        return self.title

    class Meta:
        ordering=['-date_time']


class Animal(models.Model):
    name = models.CharField(max_length=32)
    sound = models.CharField(max_length=32)
