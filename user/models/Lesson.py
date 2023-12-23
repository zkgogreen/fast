from django.db import models
from django.contrib.auth.models import User as user_root
import datetime
from user.models.User import Users

class UserCourse(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_course_user")
    kelas       = models.ForeignKey('teacher.Kelas',blank=True, null=True,on_delete=models.CASCADE, related_name="user_kelas")
    pelajaran   = models.ForeignKey('teacher.Pelajaran',blank=True, null=True,on_delete=models.CASCADE, related_name="user_history_pelajaran") #mendapat histori pelajaran
    bab_kelas   = models.ForeignKey('teacher.Bab',blank=True, null=True,on_delete=models.CASCADE, related_name="user_history")                  # mendapat histori bab
    tanggal     = models.DateField(auto_now_add=True)
    finish      = models.BooleanField(default=False)
    like        = models.IntegerField(default=0)
    feed        = models.CharField(blank=True, null=True, max_length=225)
    feedback    = models.CharField(blank=True, null=True, max_length=225)
    enroll      = models.BooleanField(default=False)
    def __str__(self):
        return "{} take {}".format(self.user, self.kelas)
    def lesson(self):
        return UserLesson.objects.filter(userCourse=self)
    def percent(self):
        lesson = UserLesson.objects.filter(userCourse=self)
        bab = UserBab.objects.filter(userCourse=self)
        return round(((lesson.filter(isdone=True).count()+bab.filter(isdone=True).count())/(lesson.count()+bab.count()))*100)

# lesson yang sudah dikerjakan
class UserLesson(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_lesson_user")
    kelas       = models.ForeignKey('teacher.Kelas',blank=True, null=True,on_delete=models.CASCADE, related_name="user_kelas_lesson")
    bab_kelas   = models.ForeignKey('teacher.Bab',blank=True, null=True,on_delete=models.CASCADE, related_name="user_bab_kelas_lesson")
    pelajaran   = models.ForeignKey('teacher.Pelajaran',blank=True, null=True,on_delete=models.CASCADE, related_name="user_pelajaran")
    userCourse  = models.ForeignKey('user.UserCourse',blank=True, null=True,on_delete=models.CASCADE, related_name="usercourse_lesson")
    isdone      = models.BooleanField(default=False)
    question    = models.CharField(max_length=225, blank=True, null=True)
    answer      = models.CharField(max_length=225, blank=True, null=True)
    tgl         = models.DateField(auto_now_add=False, blank=True, null=True)
    def __str__(self):
        return "{} take {} by {}".format(self.id, self.user, self.pelajaran)

    def user_info(self):
        return Users.objects.get(user=self.user)
    
class UserBab(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_bab_user")
    kelas       = models.ForeignKey('teacher.Kelas',blank=True, null=True,on_delete=models.CASCADE, related_name="user_kelas_bab")
    bab_kelas   = models.ForeignKey('teacher.Bab',blank=True, null=True,on_delete=models.CASCADE, related_name="userbab_bab")
    userCourse  = models.ForeignKey('user.UserCourse',blank=True, null=True,on_delete=models.CASCADE, related_name="usercourse_bab")
    isdone      = models.BooleanField(default=False)
    tgl         = models.DateField(auto_now_add=False, blank=True, null=True)
    def __str__(self):
        return "{} take {} by {}".format(self.id, self.user, self.bab_kelas)

    def prev(self):
        return UserLesson.objects.filter(user=self.user, bab_kelas=self.bab_kelas, isdone=True).order_by("urutan")
    def next(self):
        return UserLesson.objects.filter(user=self.user, bab_kelas=self.bab_kelas, isdone=False).order_by("urutan")

    def pelajaran(self):
        return UserLesson.objects.filter(user=self.user, bab_kelas=self.bab_kelas)

#pertanyaan lesson yang sudah diselesaikan
class UserQuestion(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_question_user")
    questions   = models.ForeignKey('teacher.Questions',blank=True, null=True,on_delete=models.CASCADE, related_name="UserQuestion_Question")
    kelas       = models.ForeignKey('teacher.Kelas',blank=True, null=True,on_delete=models.CASCADE, related_name="UserQuestion_kelas")
    bab_kelas   = models.ForeignKey('teacher.Bab',blank=True, null=True,on_delete=models.CASCADE, related_name="userbab_Question")
    latihan     = models.ForeignKey('user.UserLatihan',blank=True, null=True,on_delete=models.CASCADE, related_name="user_latihan")
    selected    = models.CharField(max_length=225, blank=True, null=True)
    right       = models.BooleanField(default=False)
    tanggal     = models.DateField(auto_now_add=True)
    def __str__(self):
        return "{} {}{}".format(self.id, self.user, self.questions)

#games yang sudah di selesaikan
class UserGames(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_games_user")
    games       = models.ForeignKey('teacher.Games',blank=True, null=True,on_delete=models.CASCADE, related_name="Usergames_Games")
    kelas       = models.ForeignKey('teacher.Kelas',blank=True, null=True,on_delete=models.CASCADE, related_name="Usergames_kelas")
    bab_kelas   = models.ForeignKey('teacher.Bab',blank=True, null=True,on_delete=models.CASCADE, related_name="userbab_games")
    right       = models.IntegerField(default=0) #jumlah benar
    wrong       = models.IntegerField(default=0)  #jumlah salah
    failed      = models.IntegerField(default=0) #jumlah orang yg skip
    def __str__(self):
        return "{} {}{}".format(self.id, self.user, self.games)
    
class UserLatihan(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_latihan_user")
    kelas       = models.ForeignKey('teacher.Kelas',blank=True, null=True,on_delete=models.CASCADE, related_name="user_kelas_latihan")
    pelajaran   = models.ForeignKey('teacher.Pelajaran',blank=True, null=True,on_delete=models.CASCADE, related_name="user_latihan_pelajaran")
    bab_kelas   = models.ForeignKey('teacher.Bab',blank=True, null=True,on_delete=models.CASCADE, related_name="user_latihan")
    is_last     = models.BooleanField(default=False)
    is_finish   = models.BooleanField(default=False)
    nilai       = models.IntegerField(blank=True, null=True)
    tanggal     = models.DateTimeField(auto_now_add=True)
    countdown   = models.TimeField(default="00:10:00")
    countdownNow= models.TimeField(default="00:10:00")
    def __str__(self):
        return "{}{}".format(self.user, self.nilai)

    def soal(self):
        return UserQuestion.objects.filter(latihan=self)