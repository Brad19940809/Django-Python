from django.db import models

BOOK_TYPE = (('F', '科幻'), ('Y', '言情'), ('X', '小说'),)


class Owner(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()


class Book(models.Model):
    author = models.ManyToManyField(Owner)
    name = models.CharField(max_length=32)
    type = models.CharField(choices=BOOK_TYPE, default='F', max_length=1)


######################################################

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


################################################################

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(default='xiaoleluo@126.com')

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):  # __unicode__ on Python 2
        return self.headline


###################################################

class Husband(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()


class Wife(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
