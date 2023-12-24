from django.contrib import admin

# Register your models here.
from user.models.Course import Cart, UserVocab,  UserMeeting, UserMentor, UserSchadule
from user.models.Lesson import UserCourse, UserLesson, UserQuestion, UserGames, UserLatihan, UserBab
from user.models.User import Users, Premium

admin.site.register(Cart)
admin.site.register(UserCourse)
admin.site.register(UserLesson)
admin.site.register(Users)
admin.site.register(UserVocab)
admin.site.register(UserQuestion)
admin.site.register(UserGames)
admin.site.register(UserMeeting)
admin.site.register(UserMentor)
admin.site.register(UserSchadule)
admin.site.register(UserLatihan)
admin.site.register(UserBab)
admin.site.register(Premium)