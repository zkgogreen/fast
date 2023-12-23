from django.contrib import admin

# Register your models here.
from teacher.models.teacher import Teacher,  Withdrow
from teacher.models.course import Room, Schadule
from teacher.models.kelas import Kelas, Creator, Bab, Pelajaran, Questions, Games, Vocab, VocabGroup
class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("kelas",)}

admin.site.register(Teacher)
admin.site.register(Games)
admin.site.register(Kelas, SlugAdmin)
admin.site.register(Bab)
admin.site.register(Pelajaran)
admin.site.register(Questions)
admin.site.register(Vocab)
admin.site.register(VocabGroup)
admin.site.register(Withdrow)
admin.site.register(Room)
admin.site.register(Schadule)
admin.site.register(Creator)