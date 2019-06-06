from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, default="")
    age = models.PositiveIntegerField()
    secret = models.CharField(max_length=30, default="")
    country = models.ForeignKey('Country', null=True, default=None, on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
