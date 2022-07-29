from django.db import models


# Create your models here.

class Section(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    price = models.IntegerField(default=0)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, related_name='item', null=True)

    def __str__(self):
        return self.title


class Modifiers(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    item = models.ManyToManyField(Item, related_name='modifiers', blank=True)

    def __str__(self):
        return self.title
