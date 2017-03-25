from django.db import models


# Create your models here.
class Brad(models.Model):
    title = models.CharField(max_length=255)  # my blog
    category = models.CharField(max_length=50, blank=True)  # blog tag
    date_time = models.DateTimeField(auto_now_add=True)  # blog date
    content = models.TextField(blank=True, null=True)  # blog text

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']


class Master(models.Model):
    name = models.CharField(max_length=32)
    age = models.CharField(max_length=16)

    def animals(self):
        return list(self.animal_set.all())


class Animal(models.Model):
    master = models.ForeignKey(Master)  # add this field to test.
    name = models.CharField(max_length=32)
    sound = models.CharField(max_length=32)
