from django.shortcuts import redirect, render
from dashboard.models.account import LevelAkun, Level, Kategori, Master
from dashboard.models.setting import Setting
from dashboard.models.earn import Earn
from teacher.models.course import Room, Schadule
from teacher.models.kelas import Kelas, Bab, Pelajaran, Questions
from teacher.models.teacher import Withdrow
from user.models.Course import UserMeeting, UserSchadule
from user.models.User import Users
from user.models.Lesson import UserBab, UserCourse, UserLatihan, UserLesson
from django.contrib.auth.models import User as user_root

import datetime
x = datetime.datetime.now()
import random
from datetime import datetime, timedelta

def random_date(start_date, end_date):
    # Convert input strings to datetime objects
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    date_range = end_date - start_date

    random_days = random.randint(0, date_range.days)
    random_date_result = start_date + timedelta(days=random_days)

    return random_date_result

def index(request):
    context = {
        'user':Users.objects.filter(teacher=False).count(),
        'teacher':Users.objects.filter(teacher=True).count(),
        'module':Pelajaran.objects.all().count()
    }
    return render(request, 'index.html', context)

def home(request):
    return redirect("user:index")

def begin(request):
    # level akun
    levelakun1  = LevelAkun.objects.create(foto="level/free.png",people=50,meeting=30, name='free', keterangan='belajar bahasa inggris tidak butuh biaya',  nyawa=5, biaya=10000, discount=10000,promo=0,materi="GRAMMAR FOR SPEAKING, PRONUNCIATION, VOCABULARY, SPEAKING PRACTICE", bonus="Garansi mengulang, Free 60x Written Class, Free 10x Pronunciation Class, Gratis konsultasi langsung dengan tutor", ketentuan="Microphone wajib aktif ketika sesi praktek, Biaya tidak hangus jika tidak hadir, Bebas pilih jadwal atau merubah jadwal, Dilarang keras membahas isu politik atau SARA ketika praktek"),
    levelakun2  = LevelAkun.objects.create(foto="level/private.png",people=30,meeting=30, name='membersip', keterangan='belajar bahasa inggris dengan intensif',  nyawa=100, biaya=80000,discount=80000,promo=0,materi="GRAMMAR FOR SPEAKING, PRONUNCIATION, VOCABULARY, SPEAKING PRACTICE", bonus="Garansi mengulang, Free 60x Written Class, Free 10x Pronunciation Class, Gratis konsultasi langsung dengan tutor", ketentuan="Microphone wajib aktif ketika sesi praktek, Biaya tidak hangus jika tidak hadir, Bebas pilih jadwal atau merubah jadwal, Dilarang keras membahas isu politik atau SARA ketika praktek")
    levelakun3  = LevelAkun.objects.create(foto="level/premium.png",people=10,meeting=30, name='Premium', keterangan='belajar bahasa inggris tanpa batasan', nyawa=100, biaya=120000,discount=120000,promo=0,materi="GRAMMAR FOR SPEAKING, PRONUNCIATION, VOCABULARY, SPEAKING PRACTICE", bonus="Garansi mengulang, Free 60x Written Class, Free 10x Pronunciation Class, Gratis konsultasi langsung dengan tutor", ketentuan="Microphone wajib aktif ketika sesi praktek, Biaya tidak hangus jika tidak hadir, Bebas pilih jadwal atau merubah jadwal, Dilarang keras membahas isu politik atau SARA ketika praktek")
    levelakun4  = LevelAkun.objects.create(foto="level/private.png",people=1,meeting=30, name='Private', keterangan='belajar bahasa inggris tanpa batasan', nyawa=100, biaya=240000,discount=240000,promo=0,materi="GRAMMAR FOR SPEAKING, PRONUNCIATION, VOCABULARY, SPEAKING PRACTICE", bonus="Garansi mengulang, Free 60x Written Class, Free 10x Pronunciation Class, Gratis konsultasi langsung dengan tutor", ketentuan="Microphone wajib aktif ketika sesi praktek, Biaya tidak hangus jika tidak hadir, Bebas pilih jadwal atau merubah jadwal, Dilarang keras membahas isu politik atau SARA ketika praktek")
    levelakun5  = LevelAkun.objects.create(foto="level/foregn.png",people=1,meeting=30, name='Private with foregn', keterangan='belajar bahasa inggris tanpa batasan', nyawa=100, biaya=500000,discount=500000,promo=0,materi="GRAMMAR FOR SPEAKING, PRONUNCIATION, VOCABULARY, SPEAKING PRACTICE", bonus="Garansi mengulang, Free 60x Written Class, Free 10x Pronunciation Class, Gratis konsultasi langsung dengan tutor", ketentuan="Microphone wajib aktif ketika sesi praktek, Biaya tidak hangus jika tidak hadir, Bebas pilih jadwal atau merubah jadwal, Dilarang keras membahas isu politik atau SARA ketika praktek")
    
    level_akun_list = [levelakun1, levelakun2, levelakun3, levelakun4, levelakun5]
    #level
    level1      = Level.objects.create(name="Beginner", keterangan="kemampuan bahasa Inggris yang masih sangat dasar.")
    level2      = Level.objects.create(name="Elementary", keterangan="dapat berkomunikasi dengan bahasa Inggris, tetapi pembahasan hanya mencakup hal-hal tertentu yang telah dikuasai.")
    level3      = Level.objects.create(name="Intermediate", keterangan="berbahasa Inggris secara pasif dan aktif dengan topik yang lebih variatif.")
    level4      = Level.objects.create(name="Advanced", keterangan="menggunakan bahasa Inggris untuk kepentingan akademis dan profesional.")
    level5      = Level.objects.create(name="Expert", keterangan="setara dengan native speaker (penutur asli)")

    #kategori
    kategori1   = Kategori.objects.create(name="Speaking", keterangan="Kemampuan Berbicara ")
    kategori2   = Kategori.objects.create(name="Reading", keterangan="Kemampuan Membaca")
    kategori3   = Kategori.objects.create(name="Listening", keterangan="Keterampilan Menyimak")
    kategori4   = Kategori.objects.create(name="Writing", keterangan="Kemampuan Menulis")

    #master
    master1     = Master.objects.create(name="TOEFL", keterangan="Test of English as Foregn Language")
    master2     = Master.objects.create(name="Public Speaking", keterangan="Keterampilan berbicara dengan banyak orang")

    #kelas

    for k in range(3):
        kelas = Kelas.objects.create(kelas="Kelas ke-"+str(k), bahasa=1, slug="KelasKe-"+str(k), photo=f'kelas/banner{k}.jpg', kategori=kategori1, level=level1,keterangan="keterangan", rangkuman="rangkuman", urutan=k)
        for i in range(5):
            bab = Bab.objects.create(kelas=kelas, bab="kelas {} Bab {}".format(k, i), urutan=i, rangkuman="ini adalah rangkuman")
            for j in range(5):
                pelajaran = Pelajaran.objects.create(kelas=kelas, urutan=j, bab_kelas=bab, judul="kelas {} Bab {} judul {}".format(k,i, j), keterangan="ini adalah keterangan "+str(j), text="ini adalah text "+str(j), approve=True)
                for k in range(3):
                    Questions.objects.create(category=kategori1, level=level1, kelas=kelas, bab_kelas=bab, lesson=pelajaran, soal="kelas {} Bab {} judul {} question {}".format(k,i, j, k), answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)


    #Landing
    if not Setting.objects.all().exists():
        Setting.objects.create(title="Mahir SPEAKING di bulan pertama", sub="Kuasai Bahasa Inggris dengan Lebih Cepat: Speaking Sebagai Native Speaker dalam Sebulan Tanpa Hafalan!", icon="landing/icon.png", logo="landing/icon.png", foto="landing/jumbotron.png")
    
    user_list = []
    user_obj_list = []
    for u in range(20):
        user = user_root.objects.create_user(username="user_"+str(u), email="user_{}@localhost".format(u), first_name="user", last_name="ke-"+str(u), password="user1234")
        user_obj = Users.objects.create(user=user)
        user_list.append(user)
        user_obj_list.append(user_obj)
    
    mentor_list = []
    mentor_obj_list = []
    for u in range(5):
        mentor = user_root.objects.create_user(username="mentor_"+str(u), email="mentor_{}@localhost".format(u), first_name="mentor", last_name="ke-"+str(u), password="mentor1234")
        mentor_obj = Users.objects.create(user=mentor, teacher=True)
        mentor_list.append(mentor)
        mentor_obj_list.append(mentor_obj)

    for m in mentor_list:
        for u in user_list:
            get_random = random.randint(1,4)
            meeting = UserMeeting.objects.create(mentor=m, user=u,accountlevel=level_akun_list[get_random],end=x,meetremain=29,purchased=True)
            Earn.objects.create(user=meeting.user ,mentor=meeting.mentor, room=meeting.accountlevel,pemasukan=meeting.accountlevel.discount,pengeluaran=meeting.accountlevel.discount * .82, teacher=meeting.accountlevel.discount * .75, owner=meeting.accountlevel.discount * .18, developer=meeting.accountlevel.discount * .07, tgl=random_date("2023-01-01", "2023-12-29").strftime("%Y-%m-%d"))

    for m in mentor_list:
        for p in range(3):
            jumlah = random.randrange(50000,100000, 1000)
            Withdrow.objects.create(user=m, jumlah=jumlah, penerima="zakaria", tgl=random_date("2023-01-01", "2023-12-29").strftime("%Y-%m-%d"), approve=True)

    for m in mentor_list:
        level_akun = level_akun_list[random.randint(1,4)]
        room = Room.objects.create(mentor=m, bahasa=1, time=1, mulai=x, level=level_akun)
        for s in user_list:
            sch = Schadule.objects.create(room=room, mentor=m, level=levelakun2, tanggal=x)
            UserSchadule.objects.create(room=room, schadule=sch, user=s, tanggal=x)
    
    return redirect("home:home")


def delall(request):
    LevelAkun.objects.all().delete()
    Level.objects.all().delete()
    Kategori.objects.all().delete()
    Master.objects.all().delete()
    Setting.objects.all().delete()


    Kelas.objects.all().delete()
    Bab.objects.all().delete()
    Pelajaran.objects.all().delete()
    Questions.objects.all().delete()

    UserBab.objects.all().delete()
    UserCourse.objects.all().delete()
    UserLatihan.objects.all().delete()
    UserLesson.objects.all().delete()
    user_root.objects.all().delete()
    user_root.objects.create_superuser(username='jaka', email='inijakaganteng@gmail.com', password='jakaajah')
    
    return redirect("begin")