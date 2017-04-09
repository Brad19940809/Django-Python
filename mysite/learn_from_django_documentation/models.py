from django.db import models


################# ManyToManyField ##################
# class Publication(models.Model):
#     title = models.CharField(max_length=30)
#
#     def __str__(self):  # __unicode__ on Python 2
#         return self.title
#
#     class Meta:
#         ordering = ('title',)
#
#
# class Article(models.Model):
#     headline = models.CharField(max_length=100)
#     publications = models.ManyToManyField(Publication)
#
#     def __str__(self):  # __unicode__ on Python 2
#         return self.headline
#
#     class Meta:
#         ordering = ('headline',)



###################ManyToOneField####################

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):  # __unicode__ on Python 2
        return "%s %s" % (self.first_name, self.last_name)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField(null=True, blank=True)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE, null=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('headline',)


############################## OneToOneField ############################

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):  # __unicode__ on Python 2
        return "%s the place" % self.name


class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):  # __unicode__ on Python 2
        return "%s the restaurant" % self.place.name


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):  # __unicode__ on Python 2
        return "%s the waiter at %s" % (self.name, self.restaurant)


########################### Aggregation ###########################

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


class Publisher(models.Model):
    name = models.CharField(max_length=300)
    num_awards = models.IntegerField()


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    pubdate = models.DateField()


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    registered_users = models.PositiveIntegerField()
