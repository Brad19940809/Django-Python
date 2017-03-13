from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone

# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python 2
class Question(models.Model):

    def __str__(self):
        return self.question_text

    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # def was_published_recently(self):
        # now = timezone.now()
        # return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

@python_2_unicode_compatible  # only if you need to support Python 2
class Choice(models.Model):

    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Photo(models.Model):
    photo = models.ImageField(upload_to="brad")
    name = models.CharField(max_length=20)