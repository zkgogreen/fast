from django.db import models
from django.contrib.auth.models import User as user_root
from dashboard.models.account import LevelAkun

class Transaksi(models.Model):
    jumlah      = models.IntegerField(default=0)
    bulan       = models.IntegerField(default=0)
    keluar      = models.BooleanField(default=False)
    def __str__(self):
        return "bulan {} = {}".format(self.bulan, self.jumlah)
    
class Earn(models.Model):
    mentor      = models.ForeignKey(user_root,blank=True, null=True, on_delete=models.CASCADE, related_name="pendapatan_mentor")
    user        = models.ForeignKey(user_root,blank=True, null=True, on_delete=models.CASCADE, related_name="pendapatan_user")
    room        = models.ForeignKey(LevelAkun,blank=True, null=True, on_delete=models.CASCADE, related_name="room")
    pengeluaran = models.IntegerField(default=0)
    pemasukan   = models.IntegerField(default=0)
    teacher     = models.IntegerField(default=0)
    owner       = models.IntegerField(default=0)
    developer   = models.IntegerField(default=0)
    tgl         = models.DateField(auto_now_add=False)
    
    def __str__(self):
        return "{}.{}".format(self.mentor, self.tgl)