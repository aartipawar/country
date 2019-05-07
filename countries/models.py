from django.db import models


class Country(models.Model):
    country = models.CharField(max_length=50)
    def __str__ (self):
        return '%s' % (self.country)

class State(models.Model):
    state = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,default=''
        )
    def __str__ (self):
        return '%s' % (self.state)

class City(models.Model):
    city = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE, default='')
    def __str__ (self):
        return '%s' % (self.city)

