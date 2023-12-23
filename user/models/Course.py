from django.db import models
from django.contrib.auth.models import User as user_root
import datetime
from user.models.User import Users
from teacher.models.kelas import Kelas, VocabGroup
from teacher.models.course import Room, Schadule
from dashboard.models.website import Promo
from dashboard.models.account import LevelAkun

#keranjang untuk semua layanan
class Cart(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_cart_user")
    kelas       = models.ForeignKey(Kelas,blank=True, null=True,on_delete=models.CASCADE, related_name="cart_kelas")
    promo       = models.ForeignKey(Promo, blank=True, null=True, on_delete=models.CASCADE, related_name="cart_promo")
    bukti       = models.FileField(upload_to='media/bukti', blank=True)
    approve     = models.BooleanField(default=False)
    favorite    = models.BooleanField(default=False)
    tgl         = models.DateField(auto_now_add=True)
    def __str__(self):
        return "{} take {}".format(self.user, self.kelas)

#vocab yang sudah di kerjakan
class UserVocab(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_vocab_user")
    vocab       = models.ForeignKey(VocabGroup, blank=True, null=True,on_delete=models.CASCADE, related_name="vocab")
    level       = models.IntegerField(default=0)
    benar       = models.IntegerField(default=0)
    salah       = models.IntegerField(default=0)
    isdone      = models.BooleanField(default=False)
    def __str__(self):
        return "{}-{}".format(self.user, self.vocab)
    
class UserMeeting(models.Model):
    mentor      = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="mentor_meeting")
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_meeting")
    room        = models.ForeignKey(Room, blank=True, null=True,on_delete=models.CASCADE, related_name="user_meeting")
    accountlevel= models.ForeignKey(LevelAkun, blank=True, null=True,on_delete=models.CASCADE, related_name="user_meeting")
    start       = models.DateField(auto_now_add=True)
    end         = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    meetremain  = models.IntegerField(default=0)
    purchased   = models.BooleanField(default=False)
    trx_id      = models.IntegerField(default=0)
    via         = models.CharField(max_length=50, null=True)
    status      = models.CharField(max_length=50, null=True)
    SessionID   = models.CharField(max_length=50)
    def __str__(self):
        return "{}. {}-{}".format(self.id, self.user, self.meetremain)
    
#jika sudah di mentor langsung 
class UserMentor(models.Model):
    mentor      = models.ForeignKey(user_root,blank=True, null=True,on_delete=models.CASCADE,related_name="user_teacher")
    user        = models.ForeignKey(user_root,blank=True, null=True,on_delete=models.CASCADE,related_name="user_mentor")
    isMentored  = models.BooleanField(default=False)
    start       = models.DateField(auto_now=False, auto_now_add=False)
    end         = models.DateField(auto_now=False, auto_now_add=False)
    like        = models.IntegerField(blank=True, null=True)
    message     = models.CharField(max_length=224, blank=True)
    def __str__(self):
        return "{} - {}.{}".format(self.user, self.mentor, self.like)
    
#user yang mendaftar
class UserSchadule(models.Model):
    room        = models.ForeignKey(Room,blank=True, null=True,on_delete=models.CASCADE, related_name="room_room")
    schadule    = models.ForeignKey(Schadule,blank=True, null=True,on_delete=models.CASCADE, related_name="room_schadule")
    user        = models.ForeignKey(user_root,blank=True, null=True,on_delete=models.CASCADE,related_name="user_room")
    meeting     = models.ForeignKey(UserMeeting,blank=True, null=True,on_delete=models.CASCADE,related_name="user_meeting")
    hadir       = models.BooleanField(default=False)
    feedback    = models.CharField(max_length=225, blank=True, null=True)
    performance = models.IntegerField(blank=True, null=True)
    tanggal     = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    def __str__(self):
        return "{} {}".format(self.room, self.tanggal)
    
        
