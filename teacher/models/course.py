from django.db import models
from django.contrib.auth.models import User as user_root
from ckeditor.fields import RichTextField
from dashboard.models.account import LevelAkun

Language = [
        ('EN', 'English'),
        ('JP', 'Japan'),
        ('SA', 'Arab'),
        ('CN', 'China'),
    ]
jam = [
    (0,'07:30'),
    (1,'09:00'),
    (2,'10:30'),
    (3,'13:00'),
    (4,'14:30'),
    (5,'16:00'),
    (6,'18:30'),
    (7,'20:00'),
]
hari = [
    (0, 'minggu'),
    (1, 'senin'),
    (2, 'selasa'),
    (3, 'rabu'),
    (4, 'kamis'),
    (5, 'jumat'),
    (6, 'sabtu')
]

jadwal = [
    (0, 'senin,  rabu, jum\'at'),
    (1, 'selasa,  kamis, sabtu'),
    (2, 'jum\'at,  sabtu, minggu')
]

class Room(models.Model):
    mentor      = models.ForeignKey(user_root,blank=True, null=True,on_delete=models.CASCADE,related_name="teacher_room")
    bahasa      = models.CharField(choices=Language, blank=True, max_length=3, default=1)
    level       = models.ForeignKey(LevelAkun,blank=True, null=True,on_delete=models.CASCADE, related_name="level_akun_room")
    time        = models.IntegerField(choices=jam, blank=True, default=1)
    mulai       = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    jadwal      = models.IntegerField(choices=jadwal, blank=True, default=1)

class Schadule(models.Model):
    room        = models.ForeignKey(Room,blank=True, null=True,on_delete=models.CASCADE, related_name="teacher_schadule_room")
    mentor      = models.ForeignKey(user_root,blank=True, null=True,on_delete=models.CASCADE,related_name="mentor_schadule")
    terlaksana  = models.BooleanField(default=False)
    time        = models.IntegerField(choices=jam, blank=True, default=1)
    level       = models.ForeignKey(LevelAkun,blank=True, null=True,on_delete=models.CASCADE, related_name="level_akun_schadule")
    tanggal     = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    def __str__(self):
        return "{} {}".format(self.room, self.tanggal)