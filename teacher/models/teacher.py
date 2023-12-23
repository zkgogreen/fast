from django.db import models
from django.contrib.auth.models import User as user_root
from dashboard.models.account import Master

class Teacher(models.Model):
    user        = models.ForeignKey(user_root,blank=True, null=True,on_delete=models.CASCADE, related_name="user_of_teacher")
    link        = models.CharField(max_length=50, null=True, default="https://zoom.us/")
    password    = models.CharField(max_length=50, null=True, blank=True)
    credits     = models.IntegerField(default=0)
    api_key     = models.CharField(max_length=50, null=True)
    secret_key  = models.CharField(max_length=50, null=True)
    mastered    = models.ForeignKey(Master,blank=True, null=True,on_delete=models.CASCADE, related_name="Master_of_teacher")
    desc        = models.CharField(max_length=225, null=True)
    def __str__(self):
        return " {}".format(self.user)
    
# narik duit
class Withdrow(models.Model):
    user        = models.ForeignKey(user_root,blank=True, null=True, on_delete=models.CASCADE, related_name="user_withdrow")
    jumlah      = models.IntegerField(default=0)
    bank        = models.CharField(max_length=30)
    no_bank     = models.CharField(max_length=18)
    penerima    = models.CharField(max_length=50)
    tgl         = models.DateField(auto_now_add=False)
    approve     = models.BooleanField(default=False)
    
    def __str__(self):
        return "{}.{}".format(self.user, self.jumlah)
    
