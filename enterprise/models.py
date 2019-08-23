from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    linked_companies = models.ManyToManyField(Company)

    def __str__(self):
        return self.name