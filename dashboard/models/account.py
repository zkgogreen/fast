from django.db import models
from django.contrib.auth.models import User as user_root


class Langganan(models.Model):
    durasi      = models.IntegerField(default=1)
    harga       = models.IntegerField(default=50000)
    diskon      = models.IntegerField(default=40000)
    def __str__(self):
        return "{} by {}".format(self.durasi, self.diskon)
    
class LevelAkun(models.Model):
    name        = models.CharField(max_length=224,  unique=True)
    foto        = models.FileField(upload_to='photo/level', max_length=100, null=True, blank=True)
    keterangan  = models.CharField(max_length=224)
    nyawa       = models.IntegerField(default=0)
    biaya       = models.IntegerField(default=0)
    discount    = models.IntegerField(default=0)
    promo       = models.IntegerField(default=0)
    bestseller  = models.BooleanField(default=False)
    meeting     = models.IntegerField(default=0)
    people      = models.IntegerField(default=0)
    duration    = models.IntegerField(default=1)
    mengulang   = models.BooleanField(default=False)
    ketentuan   = models.CharField(max_length=225, blank=True, null=True)
    materi      = models.CharField(max_length=225, blank=True, null=True)
    bonus       = models.CharField(max_length=225, blank=True, null=True)
    langganan   = models.ForeignKey(Langganan,blank=True, null=True,  on_delete=models.CASCADE, related_name="langganan")
    def __str__(self):
        return "{}".format(self.name)
    
    def ketentuans(self):
        return self.ketentuan.split(",")
    def materis(self):
        return self.materi.split(",")
    def bonuses(self):
        return self.bonus.split(",")

class Level(models.Model):
    name        = models.CharField(max_length=224,  unique=True)
    keterangan  = models.CharField(max_length=224)
    def __str__(self):
        return "{} by {}".format(self.name, self.keterangan)

class Kategori(models.Model):
    name        = models.CharField(max_length=224,  unique=True)
    keterangan  = models.CharField(max_length=224)
    def __str__(self):
        return "{} by {}".format(self.name, self.keterangan,  unique=True)

class Master(models.Model):
    name        = models.CharField(max_length=224,  unique=True)
    keterangan  = models.CharField(max_length=224)
    def __str__(self):
        return "{} by {}".format(self.name, self.keterangan)
