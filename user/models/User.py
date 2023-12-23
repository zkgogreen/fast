from django.db import models
from django.contrib.auth.models import User as user_root
from dashboard.models.account import Level

getstatus = ((1, 'user'),(2, 'teacher'),(3, 'owner'))

class Users(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True ,on_delete=models.CASCADE, related_name="user_user")
    birth       = models.DateField(null=True, blank=True)
    address     = models.CharField(max_length=224, blank=True)
    photo       = models.FileField(upload_to='photo/profile', default='photo/profile/user.jpg')
    join        = models.DateField(auto_now_add=True)                           # kapan join 
    kelas       = models.IntegerField(default=1)
    testi       = models.TextField(blank=True)
    phone       = models.CharField(max_length=224, blank=True)
    promo       = models.BooleanField(default=False)
    def __str__(self):
        return "{} {}".format(self.id, self.user.username)
    
    def save(self, *args, **kwargs):
        try:
            this = Users.objects.get(id=self.id)
            if this.photo != self.photo:
                this.photo.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super().save(*args, **kwargs)

class Premium(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True ,on_delete=models.CASCADE, related_name="premium_user")
    premium_start= models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)          # akun premium
    premium_end= models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)          # akun premium
    def __str__(self):
        return "{} {}".format(self.user, self.premium_start)
    
class Status(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True ,on_delete=models.CASCADE, related_name="status_user")
    status      = models.IntegerField(choices=getstatus, default=1)
    teacher     = models.BooleanField(default=False)
    def __str__(self):
        return "{} {}".format(self.user, self.status)
    
class Progress(models.Model):
    xp          = models.IntegerField(default=0)
    nyawa       = models.IntegerField(default=0)
    game        = models.IntegerField(default=0)
    mahkota     = models.IntegerField(default=0)
    level       = models.ForeignKey(Level,to_field='name', default='Beginner',on_delete=models.CASCADE, related_name="progress_user")
    def __str__(self):
        return "{} {}".format(self.user, self.level)