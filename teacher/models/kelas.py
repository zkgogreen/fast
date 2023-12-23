from django.db import models
from django.contrib.auth.models import User as user_root
from ckeditor.fields import RichTextField
from dashboard.models.account import Kategori, Level

Language = [
        ('EN', 'English'),
        ('JP', 'Japan'),
        ('SA', 'Arab'),
        ('CN', 'China'),
    ]

class Kelas(models.Model):
    kelas       = models.CharField(max_length=224)
    bahasa      = models.CharField(max_length=3,choices=Language, blank=True)
    slug        = models.SlugField(max_length=30, null=True)
    photo       = models.FileField(upload_to='kelas', max_length=100, default="kelas/default.jpg")
    kategori    = models.ForeignKey(Kategori,blank=True, null=True,on_delete=models.CASCADE, related_name="kategori_kelas")
    level       = models.ForeignKey(Level,blank=True, null=True,on_delete=models.CASCADE, related_name="level_kelas")
    keterangan  = models.CharField(blank=True,max_length=224)
    rangkuman   = RichTextField(blank=True, null=True)
    defaultget  = models.BooleanField(default=False)
    biaya       = models.IntegerField(default=0)
    discount    = models.IntegerField(default=0)
    premium     = models.BooleanField(default=False)
    mahkota     = models.IntegerField(default=0)
    dilihat     = models.IntegerField(default=0)
    certificate = models.BooleanField(default=False)
    rilis       = models.BooleanField(default=False)
    urutan      = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return " {}".format(self.kelas)


# perubahan kelas yang ajukan oleh guru
class Creator(models.Model):
    user        = models.ForeignKey(user_root,blank=True, null=True,on_delete=models.CASCADE, related_name="user_creator")
    Kelas       = models.ForeignKey(Kelas,blank=True, null=True,on_delete=models.CASCADE, related_name="kelas_creator")
    perubahan   = models.CharField(max_length=225)
    approve     = models.BooleanField(default=False)
    date        = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{}-{}".format(self.user, self.Kelas)

# bab pada lesson
class Bab(models.Model):
    kelas       = models.ForeignKey(Kelas,blank=True, null=True,on_delete=models.CASCADE, related_name="kelas_bab")
    bab         = models.CharField(max_length=50)
    urutan      = models.IntegerField(blank=True, null=True)
    rangkuman   = RichTextField(blank=True, null=True)
    premium     = models.BooleanField(default=False)
    def __str__(self):
        return "{}-{}".format(self.kelas, self.bab)
    
class Pelajaran(models.Model):
    kelas       = models.ForeignKey(Kelas,blank=True, null=True,on_delete=models.CASCADE, related_name="kelas_pelajaran")
    urutan      = models.IntegerField(blank=True, null=True)
    bab_kelas   = models.ForeignKey(Bab,blank=True, null=True,on_delete=models.CASCADE, related_name="bab_kelas")
    judul       = models.CharField(max_length=224)
    keterangan  = models.CharField(max_length=224, default="belum ada keterangan")
    vidio       = models.URLField(max_length=200, null=True, blank=True)
    text        = RichTextField()
    date        = models.DateField(auto_now_add=True, blank=True)
    approve     = models.BooleanField(default=False)
    def __str__(self):
        return "{}-{}".format(self.id, self.judul)
    
class Questions(models.Model):
    category    = models.ForeignKey(Kategori,blank=True, null=True,on_delete=models.CASCADE, related_name="quest_kategori")
    level       = models.ForeignKey(Level,blank=True, null=True,on_delete=models.CASCADE, related_name="quest_level")
    kelas       = models.ForeignKey(Kelas,blank=True, null=True,on_delete=models.CASCADE, related_name="quest_kelas")
    bab_kelas   = models.ForeignKey(Bab,blank=True, null=True,on_delete=models.CASCADE, related_name="bab_question")
    lesson      = models.ForeignKey(Pelajaran,blank=True, null=True,on_delete=models.CASCADE, related_name="quest_pelajaran")
    soal        = models.CharField(max_length=224)
    answer      = models.CharField(max_length=224)
    wrong1      = models.CharField(max_length=224)
    wrong2      = models.CharField(max_length=224)
    wrong3      = models.CharField(max_length=224)
    penjelasan  = models.TextField(default="Belum ada penjelasan")
    user        = models.ForeignKey(user_root,blank=True, null=True,on_delete=models.CASCADE, related_name="user_question")
    approve     = models.BooleanField(default=False)
    def __str__(self):
        return "{}.{}".format(self.soal, self.lesson)
    
class Games(models.Model):
    level       = models.IntegerField()
    soal        = models.CharField(max_length=224)
    answer      = models.CharField(max_length=224)
    dummy       = models.CharField(max_length=224)
    penjelasan  = models.TextField(default="Belum ada penjelasan")
    pelajaran   = models.ForeignKey(Pelajaran,blank=True, null=True,on_delete=models.CASCADE, related_name="games_pelajaran")
    kelas       = models.ForeignKey(Kelas,blank=True, null=True,on_delete=models.CASCADE, related_name="Games_kelas")
    bab_kelas   = models.ForeignKey(Bab,blank=True, null=True,on_delete=models.CASCADE, related_name="bab_games")
    user        = models.ForeignKey(user_root,blank=True, null=True,on_delete=models.CASCADE, related_name="user_games")
    approve     = models.BooleanField(default=False)
    def __str__(self):
        return "level {} - {}".format(self.level, self.soal)
    
#grup vocabulary seperti nama buah, pekerjaan, part of speech
class VocabGroup(models.Model):
    english     = models.CharField(max_length=50)
    indo        = models.CharField(max_length=50)
    level       = models.ForeignKey(Level,blank=True, null=True, on_delete=models.CASCADE, related_name="vocab_group_level")
    img         = models.FileField(upload_to='media/vocabgroup', max_length=100, default="media/vocabgroup/default.jpg")
    def __str__(self):
        return "{}.{}-{}".format(self.id, self.english, self.indo)

#penjabaran dari vocab grup seperti buah = anggur, jeruk dll
class Vocab(models.Model):
    group       = models.ForeignKey(VocabGroup,blank=True, null=True, on_delete=models.CASCADE, related_name="vocab_group")
    english     = models.CharField(max_length=50)
    indo        = models.CharField(max_length=50)
    success     = models.IntegerField(default=0)
    failed      = models.IntegerField(default=0)
    def __str__(self):
        return "{}.{}-{}".format(self.id, self.english, self.indo)
    