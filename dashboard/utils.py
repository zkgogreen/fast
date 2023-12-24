from dashboard.models.setting import Setting
from user.models.User import Users, Premium
from datetime import datetime, date

def is_date_in_range(request):
    premium = Premium.objects.filter(user=request.user)
    if not premium.exists():
        return False
    return premium.premium_start <= datetime.now() <= premium.premium_end
    
def config(request):
    context = {}
    context['config']   = Setting.objects.get()
    context['me']       = Users.objects.get(user=request.user)
    context['premium']  = is_date_in_range(request)
    context['mentorlist']   = Users.objects.filter(teacher=True)
    return context