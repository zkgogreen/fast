from user.models.User import Users
from teacher.models.teacher import Teacher

def mentorlist():
    userlist = []
    user = Users.objects.filter(teacher=True)
    for i in user:
        user_root = i.user
        context = {
            'user':i,
            'teacher':Teacher.objects.get(user=user_root)
        }
        userlist.append(context)
    return userlist