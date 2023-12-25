from utils.app import auth, kelas
from user.models.User import Users
from user.models.Lesson import UserCourse
from user.models.Course import UserMeeting, UserSchadule
from teacher.models.kelas import Pelajaran
from teacher.models.course import Room
from django.shortcuts import redirect, render
import datetime
# Create your views here.

context = {}
def checkuser(request):
    user = Users.objects.filter(user=request.user.id)
    if not user.exists():
        Users.objects.create(user=request.user)
        return redirect("user:index")
    
    if user.first().teacher == True:
        return redirect("teacher:index")
    
    return redirect("user:index")

def index(request):
    course              = UserCourse.objects.filter(user=request.user, enroll=True)
    schadule            = UserSchadule.objects.filter(user=request.user)
    mentor              = UserMeeting.objects.filter(user=request.user).first()
    if request.method == 'POST':
        room = Room.objects.get(id=request.POST["id_room"])
        UserSchadule.objects.filter(id=request.POST['id_userroom']).update(tgl=datetime.datetime.now().date(), mentor=room.mentor, room=room)

    context['today']    = schadule.filter(tanggal=datetime.date.today()).first()
    context['pass']     = schadule.filter(tanggal__lt=datetime.date.today()).first()
    context['coming']   = schadule.filter(tanggal__gt=datetime.date.today()).first()
    context['mentor']   = mentor
    context["kelas"]    = course
    context["user"]     = Users.objects.get(user=request.user)
    return render(request, 'user/index.html', context)

def teacher(request):
    user = Users.objects.filter(id=request.user.id)
    if user[0].teacher:
        user.update(status=2)
        return redirect("teacher:index")
    else:
        return redirect("user:index")