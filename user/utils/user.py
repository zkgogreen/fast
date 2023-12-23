from user.models.User import Premium, Status
from datetime import datetime

def is_premium(request):
    date = Premium.objects.filter(user=request.user).first()
    if not date:
        return False
    return date.premium_start <= datetime.now() <= date.premium_end
