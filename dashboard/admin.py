from django.contrib import admin

# Register your models here.
from dashboard.models.account import LevelAkun, Langganan, Level, Kategori, Master
from dashboard.models.earn import Transaksi, Earn
from dashboard.models.setting import Advance, Setting
from dashboard.models.website import Event, Artikel, Ask, Improve, Promo, QnA, Report,UserEvent

admin.site.register(Event)
admin.site.register(Advance)
admin.site.register(Artikel)
admin.site.register(Ask)
admin.site.register(Improve)
admin.site.register(Kategori)
admin.site.register(Setting)
admin.site.register(Level)
admin.site.register(LevelAkun)
admin.site.register(Master)
admin.site.register(Promo)
admin.site.register(QnA)
admin.site.register(Report)
admin.site.register(Transaksi)
admin.site.register(UserEvent)
admin.site.register(Earn)
admin.site.register(Langganan)