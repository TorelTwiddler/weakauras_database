from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class WeakAura(models.Model):
    """
    A WeakAura is the container for images and data entries,
    along with information about the WeakAura.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    datetime_created = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    tags = TaggableManager()

    def __str__(self):
        return self.title


class WeakAuraData(models.Model):
    """
    A WeakAuraData contains the actual string for the
    WeakAura in WoW.
    """
    parent = models.ForeignKey(WeakAura)
    data = models.CharField(max_length=1000)
    version = models.CharField(max_length=20)
    datetime_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.parent.title + " - " + self.version


class Category(models.Model):
    """
    Categories organize WeakAuras into related groups.
    Examples would be "Abilities", "Buff/Debuff Timers"
    """
    name = models.CharField(max_length=15)
