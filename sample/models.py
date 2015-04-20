from django.db import models

# Create your models here.


class Wireless(models.Model):
    id = models.IntegerField(max_length=3, primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=6, unique=True)


class RoomID(models.Model):
    id = models.IntegerField(max_length=3, primary_key=True)
    wireless = models.ForeignKey(Wireless)
    name = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.name

    def __int__(self):
        return self.id

    def __unicode__(self):
        return self.name


class Appliances(models.Model):
    id = models.IntegerField(max_length=3, primary_key=True)
    name = models.CharField(max_length=25, unique=True)
    status = models.BooleanField(default=False, blank=False)
    roomid = models.ForeignKey(RoomID)

