from django.urls import path
from .views import views, message, kelas, bootcamp, upgrade

urlpatterns = [
    path('', views.index, name="index"),
    path('checkuser', views.checkuser, name="checkuser"),
    path('changeteacher', views.teacher, name="changeteacher"),

    #message
    path('message', message.index, name="message"),

    #kelas
    path('kelas', kelas.index.as_view(), name="kelas"),
    path('kelas/<str:slug>', kelas.index.as_view(), name="koridor"),
    path('kelas/subscribe/<str:slug>', kelas.index.as_view(), name="subscribe"),

    path('kelas/<str:slug>/<int:urutan_bab>/<int:urutan_pelajaran>', kelas.pelajaran.as_view(), name="pelajaran"),
    path('kelas/<int:id_pelajaran>', kelas.pelajaran.as_view(), name="komentar"),
    path('kelas/soal/pembahasan/<int:id>', kelas.pembahasan, name="pembahasan"),
    path('kelas/soal/waktu', kelas.waktu, name="waktu"),
    path('kelas/soal/select', kelas.select, name="select"),
    path('kelas/soal/<str:slug>/<int:urutan_bab>', kelas.soal, name="soal"),
    path('kelas/soal/<str:slug>', kelas.soal_kelas, name="soal_kelas"),
    path('kelas/rangkuman/<str:slug>/<int:urutan_bab>', kelas.rangkuman, name="rangkuman"),
    path('kelas/rangkuman/<str:slug>', kelas.rangkuman_kelas, name="rangkuman_kelas"),
    path('kelas/koridor-soal/<str:slug>/<int:urutan_bab>', kelas.koridor_soal, name="koridor_soal"),
    path('kelas/koridor-soal-kelas/<str:slug>', kelas.koridor_soal_kelas, name="koridor_soal_kelas"),

    #bootcamp
    path('bootcamp', bootcamp.index, name="bootcamp"),
    path('bootcamp/jadwal', bootcamp.jadwal, name="jadwal"),
    path('bootcamp/coming', bootcamp.coming, name="coming_bootcamp"),
    path('bootcamp/purchase', bootcamp.purchase_bootcamp, name="purchase_bootcamp"),
    path('bootcamp/confirm/<int:id>', bootcamp.confirm, name="confirm_bootcamp"),
    path('bootcamp/confirm/thank', bootcamp.thank, name="thank"),
    path('bootcamp/confirm/callback/<int:ref_id>', bootcamp.notify, name="notify"),

    # upgrade
    path('upgrade', upgrade.index, name="upgrade"),
    path('upgrade/purchase', upgrade.upgrade, name="purchase_upgrade"),
]